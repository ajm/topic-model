# Client structure

All client files are located in `static` folder. The folder contains three major app folders:

* `app` folder contains the sankey visualization code.
* `statistics` folder contains the topic statistics visualization code.
* `tree` folder contains the topic tree visualization code.

All these scripts are minified with gulp task `scripts` to files `build.min.js` (sankey), `statistics.min.js` (statistics) and `tree.min.js` (topic tree).

There's also a `less` folder containing all the less code which will be compiled to the `css` folder by gulp task `less`. The `css` folder also contains other css-files.

All the templates files are located in the `templates` folder.

# Building

1. Install [Node.js](https://nodejs.org/en/).
2. Install gulp by running `npm install -g gulp`.
3. Install dependencies by running `npm install` and `bower install`.

* To build the minified script files, run `gulp scripts`.
* To compile less, run `gulp less`.

# Running

1. Go to the directory of where you put the code.
2. Type command `virtualenv env`.
3. Type command `source env/bin/active`.
4. Type command `python app.py`.
5. Click the link in the prompt to open the webpage. By default, it is `http://127.0.0.1:5000/`.
