from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as CH_SERVICE
from selenium.webdriver.chrome.options import Options as CH_OPTIONS
from selenium.webdriver.firefox.service import Service as FF_SERVICE
from selenium.webdriver.firefox.options import Options as FF_OPTIONS

import time
import os
from pathlib import Path
# import json
import configparser

# Import functions
from functions._clear_div import *
from functions._print_debug import *


def parse_group(url: str, debug: bool = False) -> dict:
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

    url = url + '?locale=en_US'  # force english lang on the page

    config = configparser.ConfigParser()

    sep = os.sep
    cfg_path = str(
        os.path.join(
            os.path.dirname(__file__),
            '..' +
            sep +
            'config.cfg'))

    config.read(cfg_path)
    driver_path = config.get('browser', 'driver_path')
    browser_name = config.get('browser', 'browser_name')
    session_time = int(config.get('browser', 'session_time'))
    cache_path = config.get('browser', 'cache_path')

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
        options.add_argument(f'user-data-dir={cache_path}')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(
            service=service,
            options=options)  # init browser
    elif browser_name == 'Firefox':
        service = FF_SERVICE(executable_path=r'' + driver_path)
        options = FF_OPTIONS()
        options.add_argument('--headless')
        driver = webdriver.Firefox(
            service=service,
            options=options)  # init browser
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    try:
        driver.set_window_size(1280, 820)
        driver.get(url)  # open page
        time.sleep(session_time)

        try:
            decline_cookies = driver.find_element(
                By.XPATH, "//div[@aria-label='Decline optional cookies']")

            try:
                decline_cookies.click()  # decline optional cookies
            except Exception as e:
                print_debug(f"Cannot decline cookies: {e}")

        except NoSuchElementException:
            if debug:
                print_debug("No cookies modal...")
                driver.save_screenshot('./1.png')

        try:
            close_login_modal = driver.find_element(
                By.CSS_SELECTOR, "[aria-label=Close]")

            try:
                close_login_modal.click()  # close modal
            except Exception as e:
                print_debug(f"Cannot close modal: {e}")

        except NoSuchElementException:
            if debug:
                print_debug("No login modal...")
                driver.save_screenshot('./2.png')

        try:
            post = driver.find_element(
                By.XPATH, "//div[contains(@class, 'html-div xdj266r x14z9mp x1lziwak x18d9i69 x1cy8zhl x78zum5 x1q0g3np xod5an3 xz9dl7a x1g0dm76 xpdmqnj')]")
            desired_y = (post.size['height'] / 2) + post.location['y']
            window_h = driver.execute_script('return window.innerHeight')
            window_y = driver.execute_script('return window.pageYOffset')
            current_y = (window_h / 2) + window_y
            scroll_y_by = desired_y - current_y
            driver.execute_script(
                "window.scrollBy(0, arguments[0]);", scroll_y_by)
        except Exception as e:
            if debug:
                print_debug(f"Cannot scroll to the post: {e}")
                driver.save_screenshot('./3.png')

        try:
            see_more_button = driver.find_element(
                By.XPATH, "//div[text()='See more']")

            try:
                see_more_button.click()  # click see more
            except Exception as e:
                print_debug(f"Cannot click on see more: {e}")

            if debug:
                driver.save_screenshot('./4.png')

        except NoSuchElementException:
            if debug:
                print_debug("No see more button...")

        response = driver.page_source  # get page

    except Exception as e:
        raise Exception(f"An error occurred while fetching the page: {e}")

    driver.close()  # close browser

    soup = BeautifulSoup(response, 'html.parser')

    text = soup.find_all(
        # "span", {
        #     "class": "x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"})
        "div", {
            "class": "xu06os2 x1ok221b"})

    # try to get multiple images firstly
    images = soup.find_all(
        "div", {
            "class": "html-div xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1n2onr6"})
    if images == []:
        if debug:
            print_debug("No multiple images.. Trying single image...")
        # this will always get 1st image in the post, so it should be after
        images = soup.find_all(
            "div", {
                "class": "x6s0dn4 x1jx94hy x78zum5 xdt5ytf x6ikm8r x10wlt62 x1n2onr6 xh8yej3"})

    group_name = soup.find_all(
        "h1", {"class": "html-h1 xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x1vvkbs x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"})

    if debug:
        # print_debug("page = " + str(response))
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

    # json_object = json.dumps(d, indent=4)
    # return json_object
