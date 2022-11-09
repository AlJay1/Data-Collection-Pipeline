from asyncore import write
from distutils.log import info
from operator import contains
from time import sleep
from os import link
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json
import urllib
import requests

class PlayerScraper():

        def __init__(self, url = 'https://www.icc-cricket.com/homepage'):
                self.driver = webdriver.Chrome()
                self.driver.get(url)
                self.find_correct_page()


        def find_correct_page(self):
                rankings = self.driver.find_element(By.XPATH, '//li[@class="site-tabs__item theme theme-icc is-active"]')
                rankings.click()
                tests = self.driver.find_element(By.XPATH, '//a[@href="test"]')
                tests.click()



        def current_batters(self):
                current_bat = self.driver.find_elements(By.XPATH, '//div[@class="col-4 col-12-desk touch-scroll-list__element"]')[0]
                #poss = [current_batters, current_bowlers, current_allrounders, alltime_batters, alltime_bowlers, alltime_allrounders]
                #current_bowlers = container[1]
                
                link_bat = current_bat.find_elements(By.XPATH, './/a')
                return [bat.get_attribute('href') for bat in link_bat]
                
        def current_bowlers(self):
                current_bowl = self.driver.find_elements(By.XPATH, '//div[@class="col-4 col-12-desk touch-scroll-list__element"]')[1]              
                link_bowl = current_bowl.find_elements(By.XPATH, './/a')
                return [bat.get_attribute('href') for bat in link_bowl]

        def current_all_rounder(self):
                current_all_round = self.driver.find_elements(By.XPATH, '//div[@class="col-4 col-12-desk touch-scroll-list__element"]')[2]                
                link_all_round = current_all_round.find_elements(By.XPATH, './/a')
                return [bat.get_attribute('href') for bat in link_all_round]


        

number_1= PlayerScraper()
