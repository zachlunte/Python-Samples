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
from selenium.webdriver.common.action_chains import ActionChains
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
book_path = "https://www.google.com/books/edition/Quadriga_aurifera/f0DvWZtGticC?hl=en&gbpv=1"

# Set number of pages
pages = 104

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

# Locate the banner dismiss link
# driver.implicitly_wait(10)
# banner_dismiss = driver.find_element_by_id("gb-ogen-opt-in-banner-dismiss")

# Click to dismiss the banner
# driver.implicitly_wait(10)
# banner_dismiss.click()

# Set the zoom of the page
# driver.implicitly_wait(10)
# driver.execute_script("document.body.style.zoom='67%'")

# Switch to the right frame
driver.switch_to.frame(driver.find_element_by_id("s7Z8Jb"))

# Locate the zoom out button
driver.implicitly_wait(10)
zoom_out_button = driver.find_element_by_id(":4")

# Click the zoom out button three times
driver.implicitly_wait(10)
zoom_out_button.click()
driver.implicitly_wait(10)
zoom_out_button.click()
driver.implicitly_wait(10)
zoom_out_button.click()

# Locate the move back button
driver.implicitly_wait(10)
move_back_button = driver.find_element_by_id(":1")

# Click the move back button four times
driver.implicitly_wait(10)
move_back_button.click()
driver.implicitly_wait(10)
move_back_button.click()
driver.implicitly_wait(10)
move_back_button.click()
driver.implicitly_wait(10)
move_back_button.click()

# Locate the move forward button
driver.implicitly_wait(10)
move_forward_button = driver.find_element_by_id(":2")

# Wait to load
driver.implicitly_wait(20)

for i in range(pages):

    # Take a screenshot
    driver.implicitly_wait(10)
    driver.save_screenshot("page{}.png".format(i))
    
    # Scroll to the next page
    driver.implicitly_wait(10)
    move_forward_button.click()

    # Update the progress bar
    bar.update(i)
    sleep(2) 

# Quit the web driver
driver.quit()

print("\n\n**** FINISHED ****\n")
