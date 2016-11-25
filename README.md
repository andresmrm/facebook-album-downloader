# Yet Another Facebook Album Downloader (Alpha)

Uses Selenium.

## Install

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

Download the [webdriver](https://github.com/mozilla/geckodriver/releases) and place in the same folder.

## Run

Pass the link to a photo and it should download all photos of that album.

    python yafad.py https://www.facebook.com/therules.org/photos/a.378934665489642.79679.319457374770705/1139206752795759
