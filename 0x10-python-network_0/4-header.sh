#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of response with a custom header
curl -sH "X-School-User-Id: 98" "$1"
