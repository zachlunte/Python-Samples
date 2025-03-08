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
book_path = "https://embassyofthefreemind.com/en/library/online-catalogue/detail/d5613472-2fcb-e6de-fcc6-2a5188c49c66/media/5554263a-43ce-bcea-a0bc-64396beb6a17?mode=detail&view=horizontal&rows=1&page=1&fq%5B%5D=search_s_auteur:%22Constant,%20Alphonse%20Louis%22&fq%5B%5D=search_s_digitized_publication:%22Ja%22&sort=random%7B1533866619319%7D%20asc"

# Use Google Chrome and make it headless
# CHROME_PATH = '/usr/local/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

# Navigate to the book page
driver.get(book_path)

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Get the media links
media_links = driver.find_elements_by_class_name("mediabank-detail-panel-button")

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Get all metadata content text
metadata_list = driver.find_elements_by_class_name("metadata-content-text")

# Store the initial important metadata
book_year = metadata_list[3].text
book_author = metadata_list[1].text
book_title = metadata_list[0].text

print("Year: {}".format(book_year))
print("Author: {}".format(book_author))
print("Title: {}".format(book_title))
print("")

# Reformat the stored metadata
book_year = re.sub("[,.]", "", book_year)
book_year = re.sub("[ ]", "-", book_year)
book_author = re.sub("[,.]", "", book_author)
book_author = re.sub("[ ]", "-", book_author)
book_title = re.sub("[,.]", "", book_title)
book_title = re.sub("[ ]", "-", book_title)

# Click on the third media link
media_links[2].click()

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Get the mediabank assets list object
assets_object = driver.find_element_by_class_name("mediabank-assets-list")

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Get the actual assets list
assets_list = assets_object.find_elements_by_tag_name("li")

# Create a srcs list
img_srcs = []

# For each asset
for asset in assets_list:

    # Find the associated thumbnail image object
    img = asset.find_element_by_tag_name("img")

    # Get the src
    src = img.get_attribute("src")

    # Add the src to the list of img srcs
    img_srcs.append(src)

# Create a page counter
page_count = 1

# Create a page list
page_list = []

# Create a progress bar
bar = progressbar.ProgressBar(maxval=len(img_srcs), widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

# For each discovered memorix thumbnail
for src in img_srcs:

    # Set the current input image path
    input_image_path = src

    # Navigate to the online dememorixer tool
    driver.get('http://veradekok.nl/Dememorixer/')

    # Get the image field object
    image_field = driver.find_element_by_id('input')

    # Input the image path name into the image field
    image_field.send_keys(input_image_path)

    # Get the submission button object
    submit_button = driver.find_element_by_xpath("//*[contains(text(), 'Click me')]")

    # Press the button
    submit_button.submit()

    # Get the download link for the output image
    download_link = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download")))

    # Get the href of the download link
    src = download_link.get_attribute("href")

    # Update the output file name
    out_str = "page"+str(page_count)+".jpg"

    # Add output file name to list of pages
    page_list.append(out_str)

    # Save the output file
    urlretrieve(src, out_str)

    # Update the progress bar
    bar.update(page_count)
    sleep(0.1)

    # Update the page counter
    page_count = page_count + 1

# Quit the web driver
driver.quit()

# Create the PDF file name
pdf_title = book_year + "-" + book_author + "-" + book_title + ".pdf"

# Get the path to the current directory
dirname = os.path.dirname(__file__)

# Write the image files to a PDF
with open(pdf_title, "wb") as f:
    f.write(img2pdf.convert(page_list))

# Get the path to the current directory
dirname = os.path.dirname(__file__)

# Reset the page counter
page_count = 1

# For each page in the list of pages
for page in page_list:

    # Get the page name
    page_name = "page" + str(page_count) + ".jpg"
    
    # Get the full path to the current page 
    full_path = os.path.join(dirname, page_name)

    # Remove that stored page file
    os.remove(full_path)

    # Update the page counter
    page_count = page_count + 1

# Get the full path to the gecko driver log file if using Firefox
# full_path = os.path.join(dirname, "geckodriver.log")

# Remove that stored gecko driver log file if using Firefox
# os.remove(full_path)

print("\n\n**** FINISHED ****\n")
