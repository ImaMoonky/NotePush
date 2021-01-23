

const clearButton = document.querySelector('.clear');
const stroke_weight = document.querySelector('.stroke-weight');
const color_picker = document.querySelector('.color-picker');

console.log("Hello Wordl");
const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');

let isDrawing = false;

canvas.addEventListener('mousedown',start);
canvas.addEventListener('mousemove',draw);
canvas.addEventListener('mouseup',stop);

clearButton.addEventListener('click',clearCanvas) // this adds a listener to clearbutton and whene you click it changes

function start(e){
    isDrawing = true;
    draw(e);
}
// the code below {} uses whatever parameretr or object that you put in such as ClientX attribute of the mouse movemetn that
// we are using this for. We just do ClientX: random var name to avoid having to do e.ClientX later
function draw({clientX:x,clientY:y}){
    if (!isDrawing) return;
    ctx.lineWidth = stroke_weight.value;
    ctx.lineCap = "round";
    ctx.strokeStyle = color_picker.value;

    ctx.lineTo(x,y);
    ctx.stroke();
    // Without this code under the code would be all pixely
    ctx.beginPath();
    ctx.moveTo(x,y);
    // If the page ever resizes the Canvas will be cleared

}


function stop() {
isDrawing = false;
ctx.beginPath(); // This piece of code makes a new path everytime we have our mouse up without this the line would recconect at every point.
}

function clearCanvas() {
ctx.clearRect(0,0,canvas.width,canvas.height); // this code clears a rectange from start to end of what you put into the code.
}

window.addEventListener('resize', resizeCanvas);
function resizeCanvas () {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

resizeCanvas();