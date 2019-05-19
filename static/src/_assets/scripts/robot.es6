const Robot = {
    endpoint: 'http://phoebe.tano.si:8080/api/robot',
    init: function() {
        $('#button-start').click(Robot.start);
        $('#button-stop').click(Robot.stop);
    },
    start: function() {
        console.log('Request: Start');
        $.get(Robot.endpoint + '/start');
    },
    stop: function() {
        console.log('Request: Stop');
        $.get(Robot.endpoint + '/stop');
    }
}
