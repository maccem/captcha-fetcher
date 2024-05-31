from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchWindowException
import requests
from PIL import Image
from io import BytesIO
import uuid

driver = webdriver.Chrome()

try:
    while 1:
        driver.get('https://www.google.com/recaptcha/api2/demo')

        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]'))
        )

        recaptcha_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span#recaptcha-anchor'))
        )
        recaptcha_checkbox.click()

        driver.switch_to.default_content()
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[title="recaptcha challenge expires in two minutes"]'))
        )

        img_url = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[starts-with(@class, "rc-image-tile-") and translate(substring(@class,string-length(@class)-1),"abcdefghijklmnopqrstuvwxyz","") > 0]'))
        ).get_attribute('src')

        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        file_loc = "captchas/"
        if(img.size[0] > 300):
            file_loc += "1x1/"
        else:
            file_loc += "3x3/"
        with open(f"{file_loc}/{uuid.uuid4()}.jpg", 'wb') as file:
            file.write(response.content)

except:
    driver.quit()

finally:
    driver.quit()