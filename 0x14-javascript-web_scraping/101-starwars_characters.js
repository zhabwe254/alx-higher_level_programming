#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) return console.error(error);

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) return console.error(err);

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
