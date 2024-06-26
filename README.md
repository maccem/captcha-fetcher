# maccem's Captcha Fetcher

Tool to download partial Street View images from Google's reCAPTCHA service, some of which aren't published on Google Maps.

## Setup
1. `git clone https://github.com/maccem/captcha-fetcher.git`
2. `pip install -r requirements.txt`

Uses Google Chrome by default; if you wish to use a different browser, change line 11 in `captcha-downloader.py` to any [supported browser](https://www.selenium.dev/documentation/webdriver/browsers/).

## Run
`python captcha-downloader.py`

Stop running by closing the browser window.

Your Captchas will be saved to the respective subfolders "1x1" and "3x3" in the "captchas" folder.

## Note
After too many requests, Google will usually catch on and stop serving Captchas. When this happens, the application will close automatically.