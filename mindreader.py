#!/usr/bin/env python3

# DESCRIPTION: Uses an online tool to extract the source photo of a memorix thumbnail.
# NOTE: This program should be run from the directory the output pages will be stored in.

import sys
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Choose the book path
book_path = "https://embassyofthefreemind.com/en/library/online-catalogue/detail/54fe32c6-77d2-907c-c5b6-f1db9f85d0f8/media/cb99a771-a678-cd26-1b53-967bd38aaef0?mode=detail&view=horizontal&rows=1&page=28&sort=random%7B1533866619319%7D%20asc"

# Set the driver to be Firefox
driver = webdriver.Firefox()

# Let drive wait about 10 seconds before doing a find_element
driver.implicitly_wait(10)

# Navigate to the book page
driver.get(book_path)

# Get the media links
media_links = driver.find_elements_by_class_name("mediabank-detail-panel-button")

# Get all metadata content text
metadata_list = driver.find_elements_by_class_name("metadata-content-text")

for m in metadata_list:
    print(m.text())

'''

# Click on the third media link
media_links[2].click()

# Get the mediabank assets list object
assets_object = driver.find_element_by_class_name("mediabank-assets-list")

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

    # Print the src
    img_srcs.append(src)

# Create a page counter
page_count = 1

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
    download_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Download")))

    # Get the href of the download link
    src = download_link.get_attribute("href")

    # Update the output file name
    out_str = "page"+str(page_count)+".png"

    # Save the output file
    urlretrieve(src, out_str)

    # Update the page counter
    page_count = page_count + 1

# Quit the web driver
driver.quit()

'''
