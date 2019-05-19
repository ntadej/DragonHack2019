const MapCanvas = {
    canvas: null,
    robot: null,
    init: function () {
        console.log('Canvas');

        $('#test-button').click(MapCanvas.test);

        let size = 300;
        let radius = 10;

        MapCanvas.canvas = new fabric.StaticCanvas('map', { backgroundColor: "#fff" });
        let canvas = MapCanvas.canvas;
        canvas.setHeight(size);
        canvas.setWidth(size);

        // create a rectangle object
        MapCanvas.robot = new fabric.Circle({
            left: size / 2 - radius / 2,
            top: size / 2 - radius / 2,
            fill: 'blue',
            radius: radius
        });

        // "add" rectangle onto canvas
        canvas.add(MapCanvas.robot);
    },
    move: function (data) {
        let delta = Number(data['delta']) / 1000 * 15;
        let angle = Math.random() * Math.PI;

        console.log(delta, angle);

        MapCanvas.robot.animate('left', MapCanvas.robot.left + delta * Math.cos(angle), {
            onChange: MapCanvas.canvas.renderAll.bind(MapCanvas.canvas),
            duration: Number(data['delta'] * 2)
        });
        MapCanvas.robot.animate('top', MapCanvas.robot.top + delta * Math.sin(angle), {
            onChange: MapCanvas.canvas.renderAll.bind(MapCanvas.canvas),
            duration: Number(data['delta'] * 2)
        });
    }
};
