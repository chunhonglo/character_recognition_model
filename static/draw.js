var canvas 
var context 
var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var paint = false;
var curColor = "#FF5733";

function drawCanvas() {
	canvas = document.getElementById('canvas');
	context = document.getElementById('canvas').getContext("2d");
	context.lineWidth = 30;
}


function addClick(x,y,dragging){
	clickX.push(x);
	clickY.push(y);
	clickDrag.push(dragging);
}

function redraw() {
	context.clearRect(0,0, context.canvas.width, context.canvas.height);

	for (var i = 0; i < clickX.length; i+=1)
	{
		if (!clickDrag[i] && i==0){
		context.beginPath();
		context.moveTo(clickX[i], clickY[i]);
		context.stroke();
	} else if (!clickDrag[i] && i> 0){
		context.closePath();
		context.beginPath();
		context.moveTo(clickX[i], clickY[i]);
		context.stroke();
	}
	else{
	context.lineTo(clickX[i], clickY[i]);
		context.stroke();
	}
	}
}

function drawNew(){
	var i = clickX.length - 1
	if (!clickDrag[i]){
		if (clickX.length == 0){
			context.beginPath();
			context.moveTo(clickX[i], clickY[i]);
			context.stroke();
		}
		else{
			context.closePath();

			context.beginPath();
			context.moveTo(clickX[i], clickY[i]);
			context.stroke();
		}
	}
	else{
	context.lineTo(clickX[i], clickY[i]);
	context.stroke();
	}
}

function mouseDownEventHandler(e){
	paint = true;
	var x = e.pageX - canvas.offsetLeft;
	var y = e.pageY - canvas.offsetTop;
	if (paint) {
		addClick(x, y, false);
		redraw();
	
	}

}

function mouseUpEventHandler(e){
	context.closePath();
	paint=false;
}

function mouseMoveEventHandler(e){
	var x = e.pageX - canvas.offsetLeft;
	var y = e.pageY - canvas.offsetTop;
	if (paint) {
		addClick(x,y,true);
		redraw();
	}
}

function save() {
	var image = new Image();
	var url = document.getElementById('url');
	image.id = "pic";
	image.src = canvas.toDataURL();
	url.value = image.src;
}

function test(){
	alert("test!");
}

