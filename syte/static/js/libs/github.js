/*
UI functions dedicated to the Github modal panel
*/

var github_api_user = 'https://api.github.com/users/';
var github_api_repos = '/repos';

var spinner = (new Spinner(spin_opts)).spin();
var template = null;
var url = null;
var github_data = {};

$('a[id^="Github-link"]').click(function (e)
{
    var url = prepare_link(e, this);
    adjustSelection("Github-link");
    remove_modal();
    showGithub(url, this);
});

function showGithub(e, t) {
    url = t.href;
    var github_profile = $("#github-profile");
    if (github_profile.length > 0) {
        github_profile.modal('show');
    }
    else {
        $("#Github-link").append(spinner.el);

        $.get('/theme/templates/github-view.html', function(data) {
            // Request succeeded, data contains HTML template, we can load data
            template = Handlebars.compile(data);
            var user_url = github_api_user+github_username;

            try {
                $.ajax({
                    url: user_url,
                    dataType: "jsonp",
                    jsonpCallback: "readGithubData",
                    error: function(s, statusCode, errorThrown) {
                        window.location.href = url;
                        spinner.stop();
                    }
                });
            }
            catch (err) {
                window.location.href = url;
                spinner.stop();
            }
        })
        .error(function() {
            window.location.href = url;
            spinner.stop();
        });
    }
}

function readGithubData(user) {
    try {
        github_data['user'] = user.data

        var repos_url = github_api_user+github_username+github_api_repos;
        $.ajax({
            url: repos_url,
            dataType: "jsonp",
            jsonpCallback: "readRepositories",
            error: function(s, statusCode, errorThrown) {
                window.location.href = url;
                spinner.stop();
            }
        });
    }
    catch (err) {
        window.location.href = url;
        spinner.stop();
    }
}

function readRepositories(repos) {
    try {
        github_data['repositories'] = repos.data

        var html = template(github_data);
        $('body').append(html);
        $("#github-profile").modal();
        spinner.stop();
    }
    catch (err) {
        window.location.href = url;
        spinner.stop();
    }
}
