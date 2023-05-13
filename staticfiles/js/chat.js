/* Register function takes two arguments: username and password, for creating the user. */
function register(username, password) {
     //Post to '/api/users' for creating a user, the data in JSON string format.
    $.post('/api/users', '{"username": "'+ username +'", "password": "'+ password +'"}',
        function (data) {
        window.location = '/'; //Redirect to login page if success
        }).fail(function (response) {
            $('#id_username').addClass('invalid'); //Add class 'invalid' which will display "Username already taken" in the registration form if failed
        })
}

var text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
        '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' + 
        '{message}' +
        '</div>';
// Send takes three args: sender, receiver, message. sender & receiver are ids of users, and message is the text to be sent.
function send(sender, receiver, message) {
    //POST to '/api/messages', the data in JSON string format
    $.post('/api/messages', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You"); // Replace the text '{sender}' with 'You'
        box = box.replace('{message}', message); // Replace the text '{message}' with the message that has been sent.
        $('#board').append(box); // Render the message inside the chat-box by appending it at the end.
        scrolltoend(); // Scroll to the bottom of he chat-box
    })
}

function receive() {
    if (sender_id !== receiver_id){ 
    $.get('/api/messages/'+ sender_id + '/' + receiver_id, function (data) {
        console.log(data);
        if (data.length !== 0)
        {
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box = box.replace('right', 'left blue lighten-5');
                $('#board').html(box);
                scrolltoend();
            }
        }
    })
}
}


function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}