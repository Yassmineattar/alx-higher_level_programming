#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const file = process.argv[3];
const url = process.argv[2];

request.get(url, (error, res, body) => { // perform an HTTP GET request
  if (error) {
    console.log(error);// Print the error if one occurred
  } else {
    fs.writeFile(file, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
