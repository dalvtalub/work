$(document).ready(function () {
    $('[name=send]').click(function (e) {
        e.preventDefault();
        const team = $('[id=team_input]').val();
        if (team === "") {

        } else {
            $.ajax({
                cache: false,
                headers: {
                    'X-CSRF-TOKEN': $('[name=csrfmiddlewaretoken]')
                    'Content-Type': 'application/json',
                },
                type: 'post',
                url: '/',
                data: {'team': team},
                success: function (data) {

                },
                dataType: 'json',
            });
        }
    });
});
