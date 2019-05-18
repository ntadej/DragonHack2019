const MapCanvas = {
    canvas: null,
    init: function() {
        console.log('Canvas');

        $('#test-button').click(MapCanvas.test);

        MapCanvas.canvas = new fabric.Canvas('map');
        let canvas = MapCanvas.canvas;
        canvas.selection = false;
        canvas.hoverCursor = 'auto';

        // create a rectangle object
        var rect = new fabric.Rect({
            left: 100,
            top: 100,
            fill: 'blue',
            width: 20,
            height: 20,
            selectable: false
        });

        // "add" rectangle onto canvas
        canvas.add(rect);
    },
    test: function() {
        let canvas = MapCanvas.canvas;

        for (var obj of canvas.getObjects()) {
            console.log(obj)
            canvas.remove(obj);
        }

        // create a rectangle object
        var rect = new fabric.Rect({
            left: 100 * Math.random(),
            top: 100 *Math.random(),
            fill: 'blue',
            width: 20,
            height: 20,
            selectable: false
        });

        // "add" rectangle onto canvas
        canvas.add(rect);
    }
};
