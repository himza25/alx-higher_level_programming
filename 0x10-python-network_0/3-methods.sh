#!/bin/bash
# This script displays all HTTP methods that a server will accept for a given URL.
curl -sI $1 | grep "Allow:" | cut -d " " -f2-
