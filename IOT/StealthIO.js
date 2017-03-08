var m = require('mraa'); //IO Library
var app = require('express')(); //Express Library
var server = require('http').Server(app); //Create HTTP instance
var ngrok = require('ngrok'); //ngrok
var engine = require('express-dot-engine'); //Template engine

var io = require('socket.io')(server); //Socket.IO Library

var blinkInterval = 1000; //set default blink interval to 1000 milliseconds (1 second)
var ledState = 1; //set default LED state
var ngrokURL = ''; //random public URL created by ngrok

var myLed = new m.Gpio(4); //LED hooked up to digital pin 4
myLed.dir(m.DIR_OUT); //set the gpio direction to output

x = new m.I2c(0)
x.address(0x62)
x.writeReg(0, 0)
x.writeReg(1, 0)

x.writeReg(0x08, 0xAA)
x.writeReg(0x04, 255)
x.writeReg(0x02, 255)

app.engine('dot', engine.__express);
app.set('views', __dirname); //location of the templates
app.set('view engine', 'dot'); //tell express to render with the dot template engine

app.get('/', function (req, res) {
    res.render('index',{url:ngrokURL}); //render index.html and interpolate the url variable
});

app.get('/lock', function (req, res) {
  res.send('Door locked!');
  blinkInterval = 50;
});

app.get('/unlock', function (req, res) {
  res.send('Door unlocked!');
  blinkInterval = 1000;
});

io.on('connection', function(socket){
    socket.on('changeBlinkInterval', function(data){ //on incoming websocket message...
        blinkInterval = data; //update blink interval
    });
});

server.listen(3000); //run on port 3000

ngrok.connect(3000, function(err, url){ //tell ngrok to bind to port 3000
    if(err){
        console.log(err);
    }else{
        ngrokURL = url;
        console.log(url);
    }
});



blink(); //start the blink function

function blink(){
    myLed.write(ledState); //write the LED state
    ledState = 1 - ledState; //toggle LED state
    setTimeout(blink,blinkInterval); //recursively toggle pin state with timeout set to blink interval
}