#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');

axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, function (err) {
      if (err) console.log(err);
    });
  })
  .catch(function (error) {
    console.log(error);
  });
