#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response) => { // perform an HTTP GET request
  if (error) {
    console.log(error);// Print the error if one occurred
  } else {
    console.log('code:', response.statusCode); // Print the response status code if a response was received
  }
});
