from selenium import webdriver


from selenium.webdriver.common.by import By
# import time


class Log_in:
    """

    """

    def __init__(self):
        self.browser = webdriver.Chrome("/home/vinay/selenium/chromedriver")

    def open_url(self, url):
        """


        :param url:
        :return:
        """
        self.browser.get(url)

    def click_on_inputs_send_keys(self, x_path, value):
        """

        :param x_path:
        :param value:
        :return:
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_element(self, x_path):
        """

        :param x_path:
        :return:
        """
        self.browser.find_element_by_xpath(x_path).click()

    def maximize (self):
        """

        :return:
        """
        self.browser.maximize_window()

