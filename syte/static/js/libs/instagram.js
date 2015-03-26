/*
UI functions dedicated to the Instagram modal panel
*/

var instagram_api_user = 'https://api.instagram.com/v1/users/';
var instagram_api_media = '/media/recent';
var instagram_api_token = '/?access_token=';

var url = null;
var spinner = (new Spinner(spin_opts)).spin();
var template = null;
var instagram_data = {};

$('a[id^="Instagram-link"]').click(function (e)
{
    var url = prepare_link(e, this);
    adjustSelection("Instagram-link");
    remove_modal();
    showInstagram(url, this);
});

function showInstagram(e, t) {
    url = t.href;
    var instagram_profile = $("#instagram-profile");
    if (instagram_profile.length > 0) {
        instagram_profile.modal('show');
    }
    else {
        $("#Instagram-link").append(spinner.el);

        $.get('/theme/templates/instagram-view.html', function(data) {
            // Request succeeded, data contains HTML template, we can load data
            template = Handlebars.compile(data);
            var user_url = instagram_api_user+instagram_username+instagram_api_token+instagram_accesskey;

            try {
                $.ajax({
                    url: user_url,
                    dataType: "jsonp",
                    jsonpCallback: "readInstagramData",
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

function readInstagramData(result) {
    try {
        var user = result.data;
        user.media = numberWithCommas( user.counts.media );
        user.followed_by = numberWithCommas( user.counts.followed_by );
        user.follows = numberWithCommas( user.counts.follows );
        user.url = url;
        instagram_data['user'] = user

        var posts_url = instagram_api_user+instagram_username+instagram_api_media+instagram_api_token+instagram_accesskey;
        $.ajax({
            url: posts_url,
            dataType: "jsonp",
            jsonpCallback: "readPictures",
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

function readPictures(result) {
    try {
        var posts = result.data;
        for(var index = 0; index < posts.length; index++) {
            var post = posts[index];
            post.formated_date = moment.unix( parseInt( post.created_time ) ).fromNow();
        }
        instagram_data['media'] = posts

        var html = template(instagram_data);
        $('body').append(html);
        $("#instagram-profile").modal();
        spinner.stop();
    }
    catch (err) {
        window.location.href = url;
        spinner.stop();
    }
}
