# selenium-facebook

## Intro

Parse facebook group 1st page with `Python` and `Selenium`. Will get text from first post and attached image(s).

## Development prerequisites 

1. Python >= 3.11.2

1. Requirements

       pip install -r requirements.txt

## Installation

### Docker

    docker compose up -d

### Standalone

1. Install Python requirements

       pip install -r requirements.txt

1. Install browser driver:

    `Chrome`:

    * linux64)


          wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip

          unzip chromedriver_linux64.zip 

    * arm64)
        
          sudo apt-get update

          sudo apt-get install chromium-chromedriver
        
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

### Flask docker

* Request example:
    
      curl --location 'http://127.0.0.1:5000/facebook-parse' \
      --header 'Content-Type: application/json' \
      --data '{
         "url": "https://www.facebook.com/radiorestoran/"
      }'

* Response example:

      {
       "group_name": "Radio", 
       "text": "T\u00e4na pakume l\u00f5unaks: \nVeiselihasupp p\u00e4rlkuskussiga 8.- \nKr\u00f5be seak\u00f5ht tatra, hautatud kapsa ja kreemise sinepikastmega 8,5 \nHead isu!", 
       "image": ["https://scontent-arn2-1.xx.fbcdn.net/v/t39.30808-6/375992353_1226713418233367_9090939920451904984_n.jpg?stp=cp6_dst-jpg_p526x296&_nc_cat=106&ccb=1-7&_nc_sid=49d041&_nc_ohc=TT0tIP3kyRcAX9gmTZf&_nc_ht=scontent-arn2-1.xx&oh=00_AfAVack443EulvG3-BjODURASJwzrleszkjKlgz0UXv0MA&oe=650957A4"]
      }

* Logs will be written to `stc/flask_output.log` file

## Tests

1. Edit `tests/groups.txt` file

1. Run `bash test.sh`
    
    Will overwrite `output.txt` on each run. 

## autopep8

1. Change style:

       autopep8 <filename.py> --in-place --aggressive
