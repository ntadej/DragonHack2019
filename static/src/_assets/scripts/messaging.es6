const Messaging = {
    endpoint: 'http://localhost:5000/api/stream',
    eventSource: null,
    init: function () {
        Messaging.eventSource = new EventSource(Messaging.endpoint);
        Messaging.eventSource.addEventListener('chat', Messaging.chatHandler);
        Messaging.eventSource.addEventListener('telemetry', Messaging.telemetryHandler);

        Messaging.chatEl = $("#chat");
    },
    chatEl: null,
    chatHandler: function(e) {
        let obj = JSON.parse(e.data);
        if (Messaging.chatEl.find('p').length >= 10) {
            Messaging.chatEl.find('p').first().remove();
        }
        Messaging.chatEl.append(`<p>${obj.message}</p>`);
    },
    telemetryHandler: function(e) {
        let obj = JSON.parse(e.data);
        console.log(obj);
    }
};
