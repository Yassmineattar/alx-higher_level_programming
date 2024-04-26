#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (error, response, body) => { // perform an HTTP GET request
  if (error) {
    console.log(error);// Print the error if one occurred
  } else {
    console.log(JSON.parse(body).title); // Print the title of the movie if a response was received
  }
});
