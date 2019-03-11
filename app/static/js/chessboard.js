$(document).ready(function() {
    isWhiteTurn = true

    $('.square').click(function(e) {
        if($(this).hasClass('target')) {
            position = $('.position')[0]
            $.post('/movement', {
                    'position': position.className.split(' ')[2],
                    'target': e.target.className.split(' ')[2]
                },
                function(response) {
                    if(response.isCheck == true) {
                        $('.message')[0].innerHTML = 'Check!'
                    }
                    e.target.innerHTML = position.innerHTML
                    position.innerHTML = ''
                    isWhiteTurn = !isWhiteTurn
                    if(isWhiteTurn == true) {
                        $('.player')[0].innerHTML = '♔'
                    } else {
                        $('.player')[0].innerHTML = '♚'
                    }
                }
            )
            $('.square').removeClass('target')
            $('.square').removeClass('position')
        } else if(e.target.innerHTML !== '') {
            $('.square').removeClass('target')
            $('.square').removeClass('position')
            $(this).addClass('position')
            $.post('/targets', {'position': e.target.className.split(' ')[2]},
                function(data) {
                    for (i = 0; i < data.targets.length; i++) {
                        $('.' + data.targets[i]).addClass('target')
                    }
                }
            ).fail(function(error) {
                $('.message')[0].innerHTML = error.responseJSON
                $('.message').fadeIn();
                $('.message').fadeOut(3000);
            });
        }
    });
});