from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CH_SERVICE
from selenium.webdriver.chrome.options import Options as CH_OPTIONS
from selenium.webdriver.firefox.service import Service as FF_SERVICE
from selenium.webdriver.firefox.options import Options as FF_OPTIONS

import time
import os
from pathlib import Path
#import json
import configparser

# Import functions
from functions._clear_div import *
from functions._print_debug import *

def parse_group(url: str, debug: bool=False):
    """
    Parse facebook group with Selenium

    Args:
        url (str): Url
        debug (bool): Show debug output

    Returns:
        dict: {'group_name': 'str', 
        'text': 'str',
        'image': ['link', 'link', 'link']}
    """

    if not url:
        raise ValueError("URL cannot be empty...")


    config = configparser.ConfigParser()

    sep = os.sep
    cfg_path = str(os.path.join(os.path.dirname(__file__), '..' + sep + 'config.cfg'))

    config.read(cfg_path)
    driver_path = config.get('browser', 'driver_path')
    browser_name = config.get('browser', 'browser_name')
    session_time = int(config.get('browser', 'session_time'))

    path = Path(driver_path)
    if path.is_file():
        if debug:
            print_debug(f"The file {path} exists")
    else:
        raise FileNotFoundError(f'The file {path} does not exist')

    options = None
    if browser_name == 'Chrome':
        service = CH_SERVICE(executable_path=driver_path)
        options = CH_OPTIONS()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service, options=options)  # init browser
    elif browser_name == 'Firefox':
        service = FF_SERVICE(executable_path=r''+driver_path)
        options = FF_OPTIONS()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=service, options=options)  # init browser
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    try:
        driver.get(url)  # open page
        time.sleep(session_time)
        response = driver.page_source  # get page
    except Exception as e:
        raise Exception(f"An error occurred while fetching the page: {e}")
    
    driver.close()  # close browser

    soup = BeautifulSoup(response, 'html.parser')

    # x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld <- entire post
    # xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a   <- post text xu06os2 x1ok221b
    # x10l6tqk x13vifvy <- image

    text = soup.find_all(
        "span", {
            "class": "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"})
    
    # try to get multiple images firstly
    images = soup.find_all(
        "div", {
            "class": "x78zum5 x1iyjqo2 x5yr21d x1qughib x1pi30zi x1swvt13"})
    if images == []:
        if debug:
            print_debug("No multiple images.. Trying single image...")
        # this will always get 1st image in the post, so it should be after
        images = soup.find_all(
            "div", {
                "class": "x6s0dn4 x1jx94hy x78zum5 xdt5ytf x6ikm8r x10wlt62 x1n2onr6 xh8yej3"})
        
    group_name = soup.find_all(
        "h1", {"class": "x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"})

    if debug:
        print_debug("group_name = " + str(group_name))
        print_debug("text = " + str(text))
        print_debug("images = " + str(images))

    # Clear stuff from divs and create dictionary
    clean_group_name = clear_div(str(group_name), "group_name")
    clean_text = clear_div(str(text), "text")
    clean_image = clear_div(str(images), "image")
    d = clean_group_name | clean_text | clean_image

    if debug:
        print_debug("clean_group_name = " + str(clean_group_name))
        print_debug("clean_text = " + str(clean_text))
        print_debug("clean_image = " + str(clean_image))
        print_debug("d = " + str(d))

    return d

    #json_object = json.dumps(d, indent=4)
    #return json_object
