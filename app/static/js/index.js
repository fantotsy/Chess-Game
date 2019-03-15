$(document).ready(function() {

    $('.replay').click(function(e) {
        $.get('/replay', {'game': e.target.innerHTML},
            function(data) {
                for (i = 0; i < data.activity.length; i++) {
                    (function (data, i) {
                        setTimeout(performMovement, 2000 * i, data.activity[i]);
                    })(data, i);
                }
            }
        )
    });

    function performMovement(movement) {
        $('.' + movement[1])[0].innerHTML = $('.' + movement[0])[0].innerHTML
        $('.' + movement[0])[0].innerHTML = ''
    }
});