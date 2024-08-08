#!/usr/bin/node

// A script that prints all characters of a Star Wars movie

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.alx-tools.com/api/films/';

request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse the response body to get the list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Iterate through the list of character URLs
  for (const charURL of charURLList) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // Parse the charcter nformation and print the character's name Resolve the promise to indicate completion
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
