$(document).ready(function() {

    $('.gameName').click(function(e) {
        $.get('/replay', {'game': e.target.innerHTML},
            function(data) {
                for (let i = 0; i < data.activity.length; i++) {
                    setTimeout(() => {performMovement(data.activity[i])}, 2000 * i);
                }
            }
        )
    });

    function performMovement(movement) {
        $('.' + movement[1])[0].innerHTML = $('.' + movement[0])[0].innerHTML
        $('.' + movement[0])[0].innerHTML = ''
    }
});