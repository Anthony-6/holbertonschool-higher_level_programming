#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[1])
    .catch(function (error) {
        if (error.response) {
            console.log('code :', error.response.status);
        }
    });
