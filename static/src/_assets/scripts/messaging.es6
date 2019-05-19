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
        Messaging.chatHandlerMsg(obj);
    },
    chatHandlerMsg: function(obj) {
        if (Messaging.chatEl.find('p').length >= 20) {
            Messaging.chatEl.find('p').first().remove();
        }
        let time = moment(new Date()).format('HH:mm:ss');
        Messaging.chatEl.append(`<p><span class="tag is-info">${time}</span> ${obj.message}</p>`);
    },
    telemetryHandler: function(e) {
        let obj = JSON.parse(e.data);
        console.log(obj);
        Plots.addData(obj);
    },
    robotHandler: function(e) {
        let obj = JSON.parse(e.data);
        console.log(obj);
        if (obj['obstacle']) {
            MapCanvas.obstacle(obj);
        } else {
            MapCanvas.move(obj);
        }
    }
};
