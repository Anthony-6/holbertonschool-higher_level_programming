#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sd -H "X-School-User-Id=98" -X GET $1 