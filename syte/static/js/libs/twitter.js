/*
UI functions dedicated to the Twitter modal panel
*/

var twitter_api_user = 'https://twitter.com/users/';
var twitter_api_timeline = 'https://api.twitter.com/1/statuses/user_timeline.json?screen_name=';
var twitter_api_json = '.json';

var spinner = (new Spinner(spin_opts)).spin();
var template = null;
var url = null;
var twitter_data = {};

$('a[id^="Twitter-link"]').click(function (e)
{
    var url = prepare_link(e, this);
    adjustSelection("Twitter-link");
    remove_modal();
    showTwitter(url, this);
});

function showTwitter(e, t) {
    url = t.href;
    var twitter_profile = $("#twitter-profile");
    if (twitter_profile.length > 0) {
        twitter_profile.modal('show');
    }
    else {
        $("#Twitter-link").append(spinner.el);

        $.get('/theme/templates/twitter-view.html', function(data) {
            // Request succeeded, data contains HTML template, we can load data
            template = Handlebars.compile(data);
            var user_url = twitter_api_user+twitter_username+twitter_api_json;

            try {
                $.ajax({
                    url: user_url,
                    dataType: "jsonp",
                    jsonpCallback: "readTwitterData",
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

function readTwitterData(user) {
    try {
        user.statuses_count = numberWithCommas(user.statuses_count);
        user.friends_count = numberWithCommas(user.friends_count);
        user.followers_count = numberWithCommas(user.followers_count);
        user.description = twitterLinkify(user.description);
        twitter_data['user'] = user

        var tweets_url = twitter_api_timeline+twitter_username;
        $.ajax({
            url: tweets_url,
            dataType: "jsonp",
            jsonpCallback: "readTweets",
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

function readTweets(tweets) {
    try {
        for(var index = 0 ; index < tweets.length ; index++) {
            var tweet = tweets[index];
            tweet.formated_date = moment(tweet.created_at).fromNow();
            tweet.text = twitterLinkify(tweet.text);
        }
        twitter_data['tweets'] = tweets
        
        var html = template(twitter_data);
        $('body').append(html);
        $("#twitter-profile").modal();
        spinner.stop();
    }
    catch (err) {
        window.location.href = url;
        spinner.stop();
    }
}

function twitterLinkify(e) {
    return e = e.replace(/(https?:\/\/\S+)/gi, function (e) {
        return '<a href="' + e + '">' + e + "</a>"
    }), e = e.replace(/(^|) @(\w+)/gi, function (e) {
        return '<a href="http://twitter.com/' + e + '">' + e + "</a>"
    }), e = e.replace(/(^|) #(\w+)/gi, function (e) {
        return '<a href="http://search.twitter.com/search?q=' + e.replace(/#/, "%23") + '">' + e + "</a>"
    }), e
}
