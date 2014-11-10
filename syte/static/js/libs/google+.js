/*
UI functions dedicated to the Google+ modal panel
*/

var gplus_api_user = 'https://www.googleapis.com/plus/v1/people/';
var gplus_api_posts = '/activities/public?maxResults=20';
var gplus_api_access = 'key='

var url = null;

$('a[id^="Google-link"]').click(function (e)
{
    var url = prepare_link(e, this);
    adjustSelection("Google-link");
    remove_modal();
    showGoogle(url, this);
});

function showGoogle(e, t) {
    url = t.href;
    var google_profile = $("#google-profile");
    if (google_profile.length > 0) {
        google_profile.modal('show');
    }
    else {
        var spinner = (new Spinner(spin_opts)).spin();

        $("#Google-link").append(spinner.el);

        $.get('/theme/templates/google-view.html', function(data) {
            // Request succeeded, data contains HTML template, we can load data
            var template = Handlebars.compile(data);
            var google_data = {};
            var user_url = gplus_api_user+google_username+'?'+gplus_api_access+google_accesskey;

            try {
                $.get(user_url, function(user) {
                    google_data['user'] = user

                    var posts_url = gplus_api_user+google_username+gplus_api_posts+'&'+gplus_api_access+google_accesskey;
                    $.get(posts_url, function(data) {
                        var posts = data.items;
                        var index = 0;
                        while(index < posts.length) {
                            var post = posts[index];
                            if(post.title == "") {
                                posts.splice(index,1)
                            }
                            else {
                                post.published = moment(post.published).fromNow();
                                post.plusoners = numberWithCommas(post.object.plusoners.totalItems);
                                post.resharers = numberWithCommas(post.object.resharers.totalItems);
                                if(typeof post.placeName !== "undefined" && post.placeName != "") {
                                    post.title = post.title+" (@"+post.placeName+")";
                                }
                                index++;
                            }
                        }
                        google_data['posts'] = posts

                        var html = template(google_data);
                        $('body').append(html);
                        $("#google-profile").modal();
                        spinner.stop();
                    })
                    .error(function() {
                        window.location.href = url;
                        spinner.stop();
                    });
                })
                .error(function() {
                    window.location.href = url;
                    spinner.stop();
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
