"""
this file is for define class and functions
"""
from selenium import webdriver


from selenium.webdriver.common.by import By
# import time


class Log_in:
    """
        this class is used for the flowing functions
    """

    def __init__(self):
        """
            this function will do   -
                - inti the browser
        """
        self.browser = webdriver.Chrome("/home/vinay/selenium/chromedriver")

    def open_url(self, url):
        """
        this functions is used for to root the browser
        :param url:open the browser
        :return:browser opened
        """
        self.browser.get(url)

    def click_on_inputs_send_keys(self, x_path, value):
        """
                this function will do   -
                    - select the element by use of x_path and enter the input value

        :param x_path:we find the x_path what we need
        :param value:give the value as requirement by help of yaml file
        :return:it will enter the x_path and value
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_element(self, x_path):
        """
                this function well do   -
                    - select the element by use of x_path
        :param x_path: only for x-path
        :return:root to x_path
        """
        self.browser.find_element_by_xpath(x_path).click()

    def maximize (self):
        """
                this function well do   -
                    maximize the window
        :return:
        """
        self.browser.maximize_window()

