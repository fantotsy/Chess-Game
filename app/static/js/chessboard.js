$(document).ready(function() {
    $('.square').click(function(e) {
        $('.square').removeClass('target')
        if(e.target.innerHTML !== '') {
            $.post( "/targets", {'position': e.target.className.split(' ')[2]},
                function(data) {
                    for (i = 0; i < data.targets.length; i++) {
                        $('.' + data.targets[i]).addClass('target')
                    }
                }
            )
        }
    });
});