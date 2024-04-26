#!/usr/bin/node
const request = require('request');
const url_id = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];
let count = 0;

request.get(url, (error, response, body) => { // perform an HTTP GET request
  if (error) {
    return console.log(error);// Print the error if one occurred
  }
  const bod = JSON.parse(body);
  bod.results.forEach(film => {
    if (film.characters.includes(url_id)) {
      count++;
    }
});
  console.log(count); // Print the title of the movie if a response was received

});