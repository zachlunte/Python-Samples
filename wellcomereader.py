#!/usr/bin/env python3

import sys, re, os
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fpdf import FPDF
from PIL import Image
import img2pdf
import progressbar
from time import sleep

# Print the header
print("\n==== WELLCOME READER ====\n")

# Choose the book path
book_path = "https://wellcomelibrary.org/item/b24884340#?c=0&m=0&s=0&cv=0&z=-0.9535%2C-0.0889%2C2.907%2C1.7778"

# Use Google Chrome and make it headless
# CHROME_PATH = '/usr/local/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()  
# chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

# Navigate to the book page
driver.get(book_path)

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Get the media links
media_links = driver.find_elements_by_css_selector(".thumb.twoCol")

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Store the initial important metadata
book_year = "YEAR"
book_author = "AUTHOR"
book_title = "TITLE"

# Get number of images
num_media = len(media_links)

print(num_media)

# For each image
for i in range(num_media):

    print(i)

    # Click on the media link
    media_links[i].click()

    # Let drive wait about 10 seconds before doing a find_element
    driver.implicitly_wait(10)

    # Get the download link
    download_link = driver.find_element_by_class_name("download")

    # Click on the download link
    download_link.click()

    # Let drive wait about 10 seconds
    driver.implicitly_wait(10)

    # Get the hi-res option
    hires_option = driver.find_element_by_id("wholeImageHighRes")

    # Click the hi-res option
    hires_option.click()

    # Let drive wait about 10 seconds 
    driver.implicitly_wait(10)

    # Get the image link
    image_link = driver.find_element_by_link_text("Download")

    # Get the href of the image link
    src = image_link.get_attribute("href")

    # Create an out string
    out_str = "page" + str(i) + ".jpg"

    # Save the output file
    urlretrieve(src, out_str)

print("\n\n**** FINISHED ****\n")
