#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class YAFAD(object):

    def __init__(self):
        self.folder = 'album'
        self.driver_path = './geckodriver'

        self.first_img_el = None
        self.already_downloaded = []
        self.driver = webdriver.Firefox(executable_path=self.driver_path)

    def get_bigger_img(self):
        tries = 0
        while tries <= 50:
            try:
                imgs = self.driver.find_elements_by_tag_name('img')
                if self.first_img_el:
                    imgs = [i for i in imgs if i != self.first_img_el]
                return max(
                    imgs,
                    key=lambda i: i.rect['width'] * i.rect['height'])
            except:
                tries += 1
                time.sleep(0.1 * tries + 0.1)

    def wait_new_img(self, current_url):
        while True:
            time.sleep(0.1)
            new = self.get_bigger_img()
            if (new.get_attribute('src') != current_url and
               new.rect['width'] > 50):
                break
        return new

    def save(self, url):
        filepath = os.path.join(self.folder,
                                str(len(self.already_downloaded)) + '.jpg')
        print(filepath)
        urllib.request.urlretrieve(url, filepath)

    def download_album(self, url):
        os.makedirs(self.folder, exist_ok=True)
        self.driver.get(init_url)

        # close login request
        try:
            self.driver.find_element_by_link_text('Not Now').click()
        except:
            pass

        i = self.get_bigger_img()
        self.first_img_el = i
        url = i.get_attribute('src')
        i.click()
        while True:
            i = self.wait_new_img(url)
            url = i.get_attribute('src')
            if url in self.already_downloaded:
                break
            else:
                self.already_downloaded.append(url)
                self.save(url)
                i.send_keys(Keys.ARROW_RIGHT)


if __name__ == "__main__":
    init_url = sys.argv[1]
    YAFAD().download_album(init_url)
