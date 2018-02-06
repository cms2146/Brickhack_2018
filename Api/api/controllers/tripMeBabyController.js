const request = require('request');

exports.getPlace = function (req, res){
	console.log(req.body);
	var hostname = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + req.body.location;

	if(req.body.radius != undefined){
		var radius = req.body.radius * 1609.34;
		radius = Math.round(radius);
		hostname += '&radius=' + radius;
	}

	if(req.body.budget != undefined){
		var budget = req.body.budget - 1;
		hostname += '&maxprice=' + budget;
	}

	if(req.body.tags != undefined && req.body.tags.length > 0){
 		var type = req.body.tags[0];
 		hostname += '&type=' + type;
	}

	hostname += '&key=AIzaSyDsTwS2d5yyNdU0HvNGuQ8W7kYvbDRCPLM';
	console.log(hostname);
	request.get(hostname, (err, response, body) => {
		var text_api_json = JSON.parse(body).results[0]; 
		var placesHostname = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + text_api_json.place_id + '&key=AIzaSyDsTwS2d5yyNdU0HvNGuQ8W7kYvbDRCPLM'
		request.get(placesHostname, (err2, response2, body2) => {
			detailedPlaceJSON = JSON.parse(body2).result;
			var toSend = {
				'name': detailedPlaceJSON.name,
				'phone': detailedPlaceJSON.formatted_phone_number,
				'address': detailedPlaceJSON.formatted_address,
				'price': detailedPlaceJSON.price_level + 1,
				'rating': detailedPlaceJSON.rating
			};
			res.send(toSend);
		});
	});
}