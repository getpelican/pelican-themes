import argparse
import logging
import subprocess
import os

from rich.logging import RichHandler
from rich.console import Console


FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(show_path=False, console=Console(force_terminal=True))]
)
logger = logging.getLogger()

HTML_HEADER = """\
<!DOCTYPE html>
<html>
<head>
<style>

h1 {
  margin 20px auto;
  text-align: center;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

li {
  width: 500px;
  min-width: fit-content;
  border: 1px solid gray;
  background-color: whitesmoke;
  border-radius: 5px;
  margin: 25px 50px;
  text-align: center;
}

li:hover {
  background-color: lightgray;
}

a {
  display: block;
  text-decoration: none;
  color: black;
  font-size: 1.5em;
}

img {
  max-width:450px;
  border-radius: 5px;
  margin: 25px auto;
  border: 1px solid black;
}

footer {
  margin: 20px auto;
  text-align: center;
  font-size: 1.1em;
}

footer a {
  display: inline;
  font-size: 1em;
}

footer a.success {
  color: green;
}

footer a.fail {
  color: red;
}
</style>
</head>
<body>
<h1>pelican-themes Preview</h1>
<ul>"""

HTML_FOOTER = """\
</ul>
<footer>
Successfully built <a href="index.html" class="success">{success} themes</a><br/>
Failed to build <a href="failed.html" class="fail">{fail} themes</a>
</footer>
</body>
</html>
"""


def setup_folders(args):
    theme_root = os.path.abspath(os.path.dirname(__file__))
    output_root = os.path.abspath(os.path.join(theme_root, args.output))
    samples_root = os.path.abspath(os.path.join(theme_root, args.samples))
    screenshot_root = os.path.abspath(os.path.join(output_root, "_screenshots"))

    # requires `getpelican/pelican` cloned in `_pelican` folder
    if os.path.exists(samples_root):
        os.makedirs(os.path.join(samples_root, "content", "images"), exist_ok=True)   # silence warning
    else:
        raise RuntimeError(
            f"Samples folder does not exist: {samples_root}. "
            "You can use `samples` from pelican by cloning it to `_pelican` folder"
        )
    # create output and screenshot folders
    os.makedirs(output_root, exist_ok=True)
    os.makedirs(screenshot_root, exist_ok=True)

    return theme_root, samples_root, output_root, screenshot_root


def build_theme_previews(theme_root, samples_root, output_root, screenshot_root):
    themes = [item for item in os.listdir(theme_root) if os.path.isdir(item) and not item.startswith((".", "_"))]
    logger.info(f"processing {len(themes)} themes...")

    # launch web server for taking screenshots
    server = subprocess.Popen(
        ["python", "-m", "http.server", "-d", output_root],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    fail = {}
    success = {}
    screenshot_processes = []

    for theme in sorted(themes, key=lambda x: x.lower()):
        theme_path = os.path.join(theme_root, theme)
        if os.path.exists(os.path.join(theme_path, theme, "templates")):
            # actual theme is in a subfolder
            theme_path = os.path.join(theme_path, theme)
        output_path = os.path.join(output_root, theme)
        try:
            process = subprocess.run([
                "pelican",
                os.path.join(samples_root, "content"),
                "--settings", os.path.join(samples_root, "pelican.conf.py"),
                "--extra-settings", f"SITENAME=\"{theme} preview\"",
                "--relative-urls",
                "--theme-path", theme_path,
                "--output", output_path,
                "--ignore-cache",
                "--delete-output-directory"
            ],
            check=True, capture_output=True, universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            logger.error(f"[red]failed to generate     : {theme}[/]", extra={"markup": True})
            fail[theme] = exc.stdout
            continue
        success[theme] = output_path
        screenshot_path = os.path.join(screenshot_root, f"{theme}.png")
        screenshot_processes.append(
            subprocess.Popen(
                ["shot-scraper", f"http://localhost:8000/{theme}", "-o", screenshot_path, "-w", "1280", "-h", "780", "--wait", "1000"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
        )
        logger.info(f"[green]successfully generated : {theme}[/]", extra={"markup": True})

    # cleanup
    logger.info("finalizing screenshots...")
    for process in screenshot_processes:
        process.wait()
    server.terminate()
    return success, fail


def write_index_files(output_root, success, fail):
    logger.info("generating index files...")
    with open(os.path.join(output_root, "index.html"), "w") as outfile:
        outfile.write(HTML_HEADER)
        for theme, theme_path in sorted(success.items(), key=lambda x: x[0].lower()):
            outfile.write(f'<li><a href="{theme}">{theme}<br><img src="_screenshots/{theme}.png"/></a></li>')
        outfile.write(HTML_FOOTER.format(success=len(success), fail=len(fail)))

    with open(os.path.join(output_root, "failed.html"), "w") as outfile:
        outfile.write(HTML_HEADER)
        for theme, reason in sorted(fail.items(), key=lambda x: x[0].lower()):
            outfile.write(f'<li><h2>{theme}</h2><pre>{reason}</pre></li>')
        outfile.write(HTML_FOOTER.format(success=len(success), fail=len(fail)))

    logger.info(f"built {len(success)} themes")
    logger.info(f"failed {len(fail)} themes")


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", required=False, default="_output",
        help="Output folder for generating the theme previews. Defaults to `_output` in themes folder root."
    )
    parser.add_argument(
        "--samples", required=False, default="_pelican/samples",
        help="Sample website used to generate theme previews. Defaults to `_pelican/samples` in themes folder root."
    )
    return parser.parse_args(argv)


def check_requirements():
    try:
        proc = subprocess.run(
            ["pelican", "--version"],
            check=True, capture_output=True, universal_newlines=True
        )
        logger.info("using pelican: {}".format(proc.stdout.strip()))
    except subprocess.CalledProcessError:
        raise RuntimeError("Requires `pelican`, see https://docs.getpelican.com")
    try:
        proc = subprocess.run(
            ["shot-scraper", "--version"],
            check=True, capture_output=True, universal_newlines=True
        )
        logger.info("using shot-scraper: {}".format(proc.stdout.strip()))
    except subprocess.CalledProcessError:
        raise RuntimeError("Requires `shot-scraper`, see https://shot-scraper.data")


def main(argv=None):
    check_requirements()
    args = parse_args(argv)
    theme_root, samples_root, output_root, screenshot_root = setup_folders(args)
    success, fail = build_theme_previews(theme_root, samples_root, output_root, screenshot_root)
    write_index_files(output_root, success, fail)


if __name__ == "__main__":
    main()