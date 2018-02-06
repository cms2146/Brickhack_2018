'use strict';
module.exports = function(app) {
  var tripMeBaby = require('../controllers/tripMeBabyController');

  // todoList Routes
  app.route('/getPlaces').post(tripMeBaby.getPlace);
};