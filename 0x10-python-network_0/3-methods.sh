#!/bin/bash
# This script displays all HTTP methods the server will accept for the specified URL.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
