/* eslint-disable  func-names */
/* eslint quote-props: ["error", "consistent"]*/

'use strict';

const Alexa = require('alexa-sdk');

const APP_ID = undefined;  // TODO replace with your app ID (OPTIONAL).

const handlers = {
    'StartPlanIntent': function(){
        this.emit(":tell", "starting plan")
    },
    'AMAZON.HelpIntent': function () {
    },
    'AMAZON.CancelIntent': function () {

    },
    'AMAZON.StopIntent': function () {
    
    },
};

exports.handler = function (event, context) {
    const alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    alexa.registerHandlers(handlers);
    alexa.execute();
};
