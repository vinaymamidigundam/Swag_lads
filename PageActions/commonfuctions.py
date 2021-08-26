from selenium import webdriver


from selenium.webdriver.common.by import By
# import time


class Log_in:
    """
    Firsh we created the class for flowing functions
    """

    def __init__(self):
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

        :param x_path:we find the x_path what we need
        :param value:give the value as requirement by help of yaml file
        :return:it will enter the x_path and value
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_element(self, x_path):
        """

        :param x_path: only for x-path
        :return:root to x_path
        """
        self.browser.find_element_by_xpath(x_path).click()

    def maximize (self):
        """
        this function is used
        :return:
        """
        self.browser.maximize_window()

