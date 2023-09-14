# selenium-facebook

## Intro

Parse facebook group 1st page with `Python` and `Selenium`. Will get first post text and attached image(s).

## Prerequisites 

1. Python >= 3.11.2

1. Requirements

        pip install -r requirements.txt

## Installation

1. Install browser driver

    `Chrome` is used in the code:

    * linux64)


            wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip

            unzip chromedriver_linux64.zip 

    * arm64)

            sudo apt-get update

            sudo apt-get install chromium-browser

1. Enter full path to the chromedriver into the `src/config.cfg`:

        cp src/config.cfg.example src/config.cfg

        chromedriver_path=<full path to the chromedriver>

## Usage

* `$ ./facebook-parse.py`

        usage: facebook-parse.py [-h] [-u url] [-d debug]

        options:
        -h, --help            show this help message and exit
        -u url, --url url     Get facebook group 1st post text and attached image.
        -d debug, --debug debug
                                Debug output. Default False

### Tests

* `bash test.sh`
    
    Will overwrite `output.txt` on each run. 

## autopep8

1. Change style:

        autopep8 <filename.py> --in-place --aggressive
