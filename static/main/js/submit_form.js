$(document).ready(function () {
    $('[name=send]').click(function () {
        const team = $('[id=team_input]').val();
        var csrf = $('[name=csrfmiddlewaretoken]').val();
        if (team === "") {

        } else {
            $.ajax({
                cache: 'true',
                type: 'post',
                url: '/',
                data: {
                    team: team,
                    csrfmiddlewaretoken: csrf,
                },
                // show one team matches if team exists in db
                success: function (data) {
                    if (data.result) {
                        let matches_str = '';
                        let matches_now_str = '';
                        for (let res of data.result) {
                            let team1 = res.team_name1;
                            let team2 = res.team_name2;
                            let time = res.time;
                            let time_now = res.time_now;
                            let during_of_match = res.during_of_match;
                            // if now there is a match, added it to matches_now_str. if not, added it to matches_str
                            if (time <= time_now <= time + during_of_match){
                                time = time.substring(0, time.length - 1);
                                matches_now_str += '<h2 class="live"><a href="' + res.url + '" class="text matches"> ' + time + '  ' + team1
                                + '-' + team2 + '</a></h2>';
                            }
                            else {
                                time = time.substring(0, time.length - 1);
                                matches_str += '<h2 class="text"><a href="' + res.url + '" class="text matches"> ' + time + '  ' + team1
                                    + '-' + team2 + '</a></h2>';
                            }
                            $('#post-text').html('<h2 class="article_text">' + matches_now_str + matches_str + '</h2>');
                        }
                    } else {
                        $('#post-text').html('<h2 class="text">' + data.error + '</h2>');
                    }
                },
            });
        }
    });
});
