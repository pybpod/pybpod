# How to write documentation on this project

*Pre-requisites: Python3 with packages: sphinx, sphinx-autobuild, sphinx-rtd-theme*

**The following commands should be run inside the "docs" folder.**

## Option A - Automatic building and local server with NodeJS

*Pre-requisites: install NodeJS*

	1. npm install 
	2. node docs-server.js
	3. open browser: http://localhost:8080/

## Option B - Manual building without web server

	1. make html
	2. open file on browser: //swp-docs/docs/build/html/index.html
	3. [optional] make clean


