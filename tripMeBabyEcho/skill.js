/* eslint-disable  func-names */
/* eslint quote-props: ["error", "consistent"]*/

'use strict';

const Alexa = require('alexa-sdk');

const APP_ID = undefined;  // TODO replace with your app ID (OPTIONAL).

var http = require('http');

const handlers = {
  'LaunchRequest': function () {
    this.response.speak("I'm here to help you plan your trip!");
    this.emit(':responseReady');
  },
  'StartPlanIntent': function(){
    var filledSlots = delegateSlotCollection.call(this);
    var output = "Wow this trip sounds fun. You'll be in "
    var location = this.event.request.intent.slots.location.value;
    var radius = this.event.request.intent.slots.distance.value;
    var budget = this.event.request.intent.slots.budget.value;
    var startDate = this.event.request.intent.slots.startDate.value;
    var startTime = this.event.request.intent.slots.startTime.value;
    var endTime = this.event.request.intent.slots.endTime.value;
    var endDate = this.event.request.intent.slots.endDate.value;

    var postData = {};

    postData.location = location;
    postData.radius = radius;
    postData.budget = budget;
    postData.startDate = startDate;
    postData.startTime = startTime;
    postData.endDate = endDate;
    postData.endTime = endTime;



    const options = {
    hostname: '35.225.156.189',
    port: 80,
    path: '/rest/deserializer',
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = http.request(options, (res) => {
      console.log(`STATUS: ${res.statusCode}`);
      console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
      res.setEncoding('utf8');
      res.on('data', (chunk) => {
        console.log(`BODY: ${chunk}`);
      });
        res.on('end', () => {
        console.log('No more data in response.');
      });
    });

    req.write(JSON.stringify(postData));
    console.log("sent " + JSON.stringify(postData));
    req.end();

  },
  'AMAZON.HelpIntent': function () {
  },
  'AMAZON.CancelIntent': function () {

  },
  'AMAZON.StopIntent': function () {

  },
  'Unhandled': function () {
    this.emit(':tell', "Im sorry, i've encountered an error");
  },
};

exports.handler = function (event, context) {
  const alexa = Alexa.handler(event, context);
  alexa.APP_ID = APP_ID;
  alexa.registerHandlers(handlers);
  alexa.execute();
};


function delegateSlotCollection(){
  console.log("in delegateSlotCollection");
  console.log("current dialogState: "+this.event.request.dialogState);
  if (this.event.request.dialogState === "STARTED") {
    var updatedIntent=this.event.request.intent;
    this.emit(":delegate", updatedIntent);
  } else if (this.event.request.dialogState !== "COMPLETED") {
    this.emit(":delegate");
  } else {
    return this.event.request.intent;
  }
}

function randomPhrase(array) {
    // the argument is an array [] of words or phrases
    var i = 0;
    i = Math.floor(Math.random() * array.length);
    return(array[i]);
  }
  function isSlotValid(request, slotName){
    var slot = request.intent.slots[slotName];
    var slotValue;

        //if we have a slot, get the text and store it into speechOutput
        if (slot && slot.value) {
            //we have a value in the slot
            slotValue = slot.value.toLowerCase();
            return slotValue;
          } else {
            //we didn't get a value in the slot.
            return false;
          }
        }