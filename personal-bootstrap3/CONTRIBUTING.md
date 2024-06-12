# Guidelines For Contributing

- Create a new git branch specific to your change, as opposed to making your commits in the master branch.
- Don't put multiple fixes/features in the same branch / pull request.
- Give a proper description in your pull request of what you're trying to fix.
- First line of your commit message should start with present-tense verb, be 50 characters or less, and include the
relevant issue number(s) if applicable. Example: _Ensure proper PLUGIN_PATH behavior. Refs #428._ If the commit completely
fixes an existing issue or request on the tracker, please use `Fixes #585` or `Fix #585` syntax (so the relevant issue is automatically closed
upon PR merge).
- Make sure that new features are configurable using a theme variable (eg. `DISPLAY_CHUCKNORRIS_ADVICE`). Should default to
_False_, so users will not get any surprises when upgrading.
- If you introduce new theme variables, new behaviour or changes from the default Pelican behaviour, make sure you make
mention of it in the [README](README.md)
- Make sure changes do not break backwards compatibility, especially with regards to settings.
- Only changes that stand to benefit a majority of users or use cases are suitable for contributing back to the main repository. For tweaks that are likely specific to your site or likings, try using `CUSTOM_CSS`.
    - If doing so would require a CSS selector that isn't supported by the theme, create a patch that adds the necessary CSS selector, not the CSS tweak.
