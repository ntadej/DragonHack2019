//= require messaging
//= require fabric
//= require robot
//= require plots

$(document).ready(() => {
    Messaging.init();
    MapCanvas.init();
    Robot.init();
    Plots.init();
});
