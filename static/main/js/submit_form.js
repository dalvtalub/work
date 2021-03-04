$(document).ready(function () {
    $('[name=send]').click(function () {
        // e.preventDefault();
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
                success: function (data) {
                    let matches_str = ''
                    for (let res of data.result) {
                        let team1 = res.team_name1;
                        let team2 = res.team_name2;
                        let time = res.time;
                        time = time.substring(0, time.length - 1);
                        matches_str += '<h2 class="text"><a href="' + res.url + '" class="text matches"> ' + time + '  ' + team1
                            + '-' + team2 + '</a></h2>'
                        $('#post-text').html('<h2 class="article_text">'+ matches_str + '</h2>');
                    }
                },
            });
        }
    });
});
