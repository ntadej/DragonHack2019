const Messaging = {
    endpoint: 'http://phoebe.tano.si:8080/api/stream',
    eventSource: null,
    init: function () {
        Messaging.eventSource = new EventSource(Messaging.endpoint);
        Messaging.eventSource.addEventListener('chat', Messaging.chatHandler);
        Messaging.eventSource.addEventListener('telemetry', Messaging.telemetryHandler);
        Messaging.eventSource.addEventListener('robot', Messaging.robotHandler);

        Messaging.chatEl = $("#chat");
    },
    chatEl: null,
    chatHandler: function(e) {
        let obj = JSON.parse(e.data);
        console.log(obj);
        if (Messaging.chatEl.find('p').length >= 10) {
            Messaging.chatEl.find('p').first().remove();
        }
        Messaging.chatEl.append(`<p>${obj.message}</p>`);
    },
    telemetryHandler: function(e) {
        let obj = JSON.parse(e.data);
        console.log(obj);
    },
    robotHandler: function(e) {
        let obj = JSON.parse(e.data);
        console.log(obj);
    }
};
