# selenium-facebook

## Intro

Parse facebook group 1st page with `Python` and `Selenium`. Will get first post text and attached image(s).

## Prerequisites 

1. Python >= 3.11.2

1. Requirements

       pip install -r requirements.txt

## Installation

1. Install browser driver:

    `Chrome`:

    * linux64)


          wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip

          unzip chromedriver_linux64.zip 

    * arm64)
        
          sudo apt-get update

          sudo apt-get install chromium-browser
        
        chromedriver location: `/usr/lib/chromium-browser/chromedriver`

    `Firefox`:

    * linux64)

          wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz

          tar -xf geckodriver-v0.33.0-linux64.tar.gz
        
       Also Firefox binary is required (in `PATH`).

1. Create config:

       cp src/config.cfg.example src/config.cfg

1. Edit config
    
    And enter full path to the driver:

       driver_path=<full path to the driver>
    
    And change `browser_name`:
        
       browser_name=<Firefox|Chrome>

## Usage

### Standalone

* `$ ./facebook-parse.py`

       usage: facebook-parse.py [-h] [-u url] [-d debug]

       options:
       -h, --help            show this help message and exit
       -u url, --url url     Get facebook group 1st post text and attached image.
       -d debug, --debug debug
                                Debug output. Default False

### Flask

1. Linux service:

       sudo cp service/facebook-parse.service /etc/systemd/system/facebook-parse.service
    
    Edit `/etc/systemd/system/facebook-parse.service` and change values:

    1. `User=<username>` -- user to run the service

    1. `ExecStart=flask --app <path>/src/flask-app run` -- path to src folder

    1. `systemctl daemon-reload`

    1. `sudo systemctl start facebook-parse`

    1. `sudo systemctl enable facebook-parse`

* Request example:
    
      curl --location 'http://127.0.0.1:5000/facebook-parse' \
      --header 'Content-Type: application/json' \
      --data '{
         "url": "https://www.facebook.com/radiorestoran/"
      }'

## Tests

1. Edit `tests/groups.txt` file

1. Run `bash test.sh`
    
    Will overwrite `output.txt` on each run. 

## autopep8

1. Change style:

       autopep8 <filename.py> --in-place --aggressive
