const Messaging = {
    endpoint: 'http://localhost:5000/api/robot/stream',
    eventSource: null,
    init: function () {
        Messaging.eventSource = new EventSource(Messaging.endpoint);
        Messaging.eventSource.onmessage = Messaging.event;
    },
    event: function(e) {
        console.log(e)
    }
};
