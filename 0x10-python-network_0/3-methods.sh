#!/bin/bash
# This script displays all HTTP methods the server will accept for the specified URL.
curl -sI -X OPTIONS "$1" | grep -i "allow" | cut -d ':' -f2- | tr -d ' '
