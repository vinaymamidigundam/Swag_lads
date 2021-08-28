"""
    this file is used for the to test the ui_test cases
"""
from PageActions.commonfuctions import Log_in
from PageObject.swag_obj import Swage_log_in
import yaml
import time

with open('../TestData/data.yaml', 'r') as file:
    data = yaml.full_load(file)

cfuntion = Log_in()
g_objects = Swage_log_in()

cfuntion.open_url('https://www.saucedemo.com/')
cfuntion.browser.maximize_window()
time.sleep(2)
cfuntion.click_on_inputs_send_keys(g_objects.lon_in_xpath, data['user_name'])
time.sleep(1)
cfuntion.click_on_inputs_send_keys(g_objects.password_xpath, data['password'])
time.sleep(1)
cfuntion.click_on_element(g_objects.login)
time.sleep(1)
cfuntion.click_on_element(g_objects.bag)
time.sleep(1)
cfuntion.click_on_element(g_objects.tshirt)
time.sleep(0)
cfuntion.click_on_element(g_objects.labcort)
time.sleep(1)
cfuntion.click_on_element(g_objects.light)
time.sleep(1)
cfuntion.click_on_element(g_objects.jacket)
time.sleep(1)
cfuntion.click_on_element(g_objects.red_tshirt)
time.sleep(0)
cfuntion.click_on_element(g_objects.cart)
time.sleep(1)
cfuntion.click_on_element(g_objects.check_out)
time.sleep(1)
cfuntion.click_on_inputs_send_keys(g_objects.first_name,data['firstname'])
time.sleep(1)
cfuntion.click_on_inputs_send_keys(g_objects.last_name,data['lastname'])
time.sleep(1)
cfuntion.click_on_inputs_send_keys(g_objects.zip,data['zip'])
time.sleep(1)
cfuntion.click_on_element(g_objects.cont)
time.sleep(1)
cfuntion.click_on_element(g_objects.finish)
time.sleep(1)
cfuntion.click_on_element(g_objects.back_to_home)
