#!/usr/bin/env python3

# DESCRIPTION: Uses an online tool to extract the source photo of a memorix thumbnail.
# NOTE: This program should be run from the directory the output pages will be stored in.

# DEVELOPMENT:
# 1. Make the book URL a command line argument. 
# 2. Create an optional argument that allows continuation from specified page number.
# 3. Automaticaly shorten names if they're too long.
# 4. Retry from current page number if there is a time-out.

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
print("\n==== MINDREADER ====\n")

# Choose the book path
book_path = "https://babel.hathitrust.org/cgi/pt?id=ucm.5327727356&view=1up&seq=197&skin=2021"

# Set number of pages
pages = 464

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

# Create a progress bar
bar = progressbar.ProgressBar(maxval=pages, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

for i in range(pages):

    # Locate the download panel
    driver.implicitly_wait(10)
    panel_download = driver.find_element_by_id("panel-download")

    # Click the download panel
    driver.implicitly_wait(10)
    panel_download.click()

    # Locate the JPEG option
    driver.implicitly_wait(10)
    jpeg_download = driver.find_element_by_id("format-image-jpeg")

    # Click the JPEG option
    driver.implicitly_wait(10)
    jpeg_download.click()

    # Locate the download button
    driver.implicitly_wait(10)
    btn = driver.find_element_by_xpath('//button[text()="Download"]')

    # Click to download the current page
    driver.implicitly_wait(10)
    btn.click()

    # Wait for download to complete
    # downloads_done()

    # Get the list of buttons and click to the next page
    driver.implicitly_wait(10)
    btn_elements = driver.find_elements_by_class_name("btn")
    btn_elements[8].click()

    # Update the progress bar
    bar.update(i)
    sleep(2) 

# Quit the web driver
driver.quit()

print("\n\n**** FINISHED ****\n")
