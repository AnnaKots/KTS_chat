const messageTemplate = ({ id, author, time, text }) => `
    <div class="message" data-id="${id}">
        <div class="message__author">
            <div class="message__avatar"></div>
            <div class="message__name">${author}</div>
            <div class="message__time">${time}</div>
        </div>
        <div class="message__text">${text}</div>
    </div>
`; /*вносим только обновления в чат*/

$(document).ready(function() {
    var form = $("#message-form");
    //var input = $('input[name=text]');
    var chat = $($('.chat')[0]);

    form.on('submit', function (e) {
        e.preventDefault();

        var formData = new FormData(e.target);
        /* сконструировали набор "ключ-значение", чтобы
        * передать пользовательские данные через
        * XMLHttpRequest*/

        $.post({
            // method: 'POST',
            url: '/chat/message_create/',
            data: formData,
            processData: false,
            contentType: false,

            success: result => {  // Фронтенд к views
                const chat=$('#chat');
                chat.prepend(result.renderedTemplate);
                form.find("input[type=text], textarea").val('');
                //input.val('');
                /*$('.chat').prepend(result['rendered_template']);
                $('#message_input').val("");*/
            }
        });
    });

    setInterval(function () {
        const lastId = $('.message').first().data("id");

            $.ajax({
            url: '/chat/messages/',
            data: {
                'last_id': lastId
            },

            success: result => {
                if (result !== ""){
                    chat.prepend(result);
                }
            }
        });

    }, 10000);
});