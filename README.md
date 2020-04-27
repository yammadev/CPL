## About
CPL - Cartagena Potholes Locator

## Development Guide
### Requirements
- [Python](https://www.python.org/)
- [NPM](https://www.npmjs.com/)

### Build
```sh
  # Install dependencies
  $ npm install

  # Run for dev purposes
  $ npm run dev

  # Or watch for changes (in standalone console)
  # $ npm run watch

  # Or run for production
  # $ npm run prod
```

### Prepare
```sh
  # Install virtual environment
  $ python3 -m venv venv

  # (On Windows)
  $ py -3 -m venv venv

  # Activate virtual environment
  $ . venv/bin/activate

  # (On Windows)
  $ venv\Scripts\activate

  # Install Requirements
  $ pip install -U -r requirements.txt
```

### Run
```sh
  # Setting
  $ export FLASK_APP=application.py

  # (On Windows)
  $ set FLASK_APP=application.py

  # Debug mode
  $ export FLASK_ENV=development

  # (On Windows)
  $ set FLASK_ENV=development

  # Run
  $ flask run

  # Go to http://127.0.0.1:5000
```

## Changelog
All notable changes to this project are documented in this part of the file. The format is based on [Keep a Changelog](http://keepachangelog.com/).

#### [x.y.z] - YYYY-MM-DD
- **x** for major release related to major additions or changes.
- **y** for minor release related to minor additions or changes in current major release.
- **z** for minor release related to minor additions or changes in current minor release.

#### Extras
- **Added** for new features.
- **Modified** for changes in existing functionality.
- **Deprecated** for soon-to-be removed features.
- **Removed** for removed features.
- **Fixed for** any bug fixes.
- **Security** in case of vulnerabilities.

### [1.0.1] - 2020-04-26
#### Modified
- `requirements` added. 

### [1.0.0] - 2020-04-04
#### Added
- Application propossed structure to fit `MVC` pattern.
```txt
  /
    /controllers    <- Controllers
    /database       <- Database
    /models         <- Models
    /resources      <- Files
    /static         <- Compiled files
    /templates      <- Views
  application.py    <- Main App
  webpack.mix.js    <- Asset compiler
```
- `Webpack` implemented using `Laravel-mix` to compile and mix assets
- Initial commit
