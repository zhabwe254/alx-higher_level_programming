#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // https://swapi.dev/api/films/

request(url, (error, response, body) => {
  if (error) return console.error(error);

  const data = JSON.parse(body);
  let wedgeCount = 0;

  data.results.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes('18/')) { // Character ID 18 is Wedge Antilles
        wedgeCount++;
      }
    });
  });

  console.log(wedgeCount);
});
