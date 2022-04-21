#!/bin/bash
# this script retrieve the size of the  body in bytes
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
