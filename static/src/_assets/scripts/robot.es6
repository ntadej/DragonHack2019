const Robot = {
    endpoint: 'http://phoebe.tano.si:8080/api/robot',
    status: false,
    messages: [
        'This is an interesting location 😮',
        "You will have to tell if it's safe for people 🤢",
        "Driving ...",
    ],
    init: function() {
        $('#button-start').click(Robot.start);
        $('#button-stop').click(Robot.stop);
        $('#button-drop').click(Robot.drop);
    },
    start: function() {
        console.log('Request: Start');
        Robot.status = true;
        $.get(Robot.endpoint + '/start');

        window.setTimeout(Robot.randomChat, 3000);
    },
    stop: function() {
        console.log('Request: Stop');
        Robot.status = false;
        $.get(Robot.endpoint + '/stop');

        window.clearTimeout(Robot.randomChat);
    },
    drop: function() {
        console.log('Request: Drop');
        Messaging.chatHandlerMsg({message:"Sensor dropped! 💣"})

        $.get(Robot.endpoint + '/drop/set?enable=1');
    },
    randomChat: function() {
        if (!Robot.status) {
            return;
        }

        let rand = Math.floor(Math.random() * Robot.messages.length);
        let msg = Robot.messages[rand];
        console.log(msg)
        Messaging.chatHandlerMsg({message:msg});

        window.setTimeout(Robot.randomChat, 3000);
    }
}
