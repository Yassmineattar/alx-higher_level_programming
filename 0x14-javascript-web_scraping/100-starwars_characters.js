#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(url, (error, response, body) => { // perform an HTTP GET request
  if (error) {
    return console.log(error);// Print the error if one occurred
  }
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (cerror, cresponse, cbody) {
      console.log(JSON.parse(cbody).name);
    });
  }
});
