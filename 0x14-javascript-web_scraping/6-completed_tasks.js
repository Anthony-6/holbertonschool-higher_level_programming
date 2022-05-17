#!/usr/bin/node

const axios = require('axios').default;
const myDict = {};
let i;

axios.get(process.argv[2])
  .then(function (response) {
    const todolist = response.data.length;
    for (i = 0; i < todolist; i++) {
      const donetask = response.data[i].completed;
      const user = response.data[i].userId;
      if (donetask === true) {
        if (myDict[user] === undefined) {
          myDict[user] = 0;
        }
        myDict[user] += 1;
      }
    }
    console.log(myDict);
  })
  .catch(function (error) {
    console.log(error);
  });
