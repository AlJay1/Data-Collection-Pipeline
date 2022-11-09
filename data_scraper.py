
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
from player_scraper import PlayerScraper
import pandas as pd




class DataScraper(PlayerScraper):

        def __init__(self, url = 'https://www.icc-cricket.com/homepage'):
                super().__init__()
                self.data = self.driver.find_element(By.XPATH, '//div[@class="rankings-player-stats__format-section js-format-section t-test is-active"]')


        
        
        


        def first_test_stats(self):
                first_test = self.data.find_elements(By.XPATH, './/div[@class="rankings-player-stats__match-info"]')
                first_test_info =  [stats.text for stats in first_test]
                return ''.join(first_test_info)
 


                

        def bat_stats(self):
                
                batting_stats = self.data.find_elements(By.XPATH, './/div[contains(@class, "rankings-player-stats__rankings-wrapper rankings-player-stats__rankings-wrapper")]')[:2]
                batting_stats_info = [bat_stats.text for bat_stats in batting_stats]
                return ''.join(batting_stats_info)


        def bowling_stats(self):
                bowling_stats = self.data.find_elements(By.XPATH, './/div[contains(@class, "rankings-player-stats__rankings-wrapper rankings-player-stats__rankings-wrapper")]')[2:4]
                bowling_stats_info = [bowl_stats.text for bowl_stats in bowling_stats]
                return ''.join(bowling_stats_info)

        def all_rounder_stats(self):
                all_rounder_stats = self.data.find_elements(By.XPATH, './/div[contains(@class, "rankings-player-stats__rankings-wrapper rankings-player-stats__rankings-wrapper")]')[4:]
                all_rounder_stats_info = [all_round_stats.text for all_round_stats in all_rounder_stats]
                return ''.join(all_rounder_stats_info)




        def get_current_batters_info(self):
                current_batter_links = self.current_batters()
                # Create folder for rankings

                for bat_links in current_batter_links:
                        self.driver.get(bat_links)
                        time.sleep(2)
                        self.get_player_info()
                        break


        def get_current_bowlers_info(self):
                current_bowl_links = self.current_bowlers()
                # Create folder for rankings

                for bowl_links in current_bowl_links:
                        self.driver.get(bowl_links)
                        time.sleep(2)
                        self.get_player_info()
                        break

        def get_current_all_rounder_info(self):
                current_all_rounder_links = self.current_all_rounder()
                # Create folder for rankings

                for all_round_links in current_all_rounder_links:
                        self.driver.get(all_round_links)
                        time.sleep(2)
                        self.get_player_info()
                        break
        

        
        def writing_up_data(self):

                first_test_text = self.first_test_stats()
                batting_stats_text = self.bat_stats()
                bowling_stats_text = self.bowling_stats()
                all_rounder_stats_text = self.all_rounder_stats()

                
                
                data_dict = {"First and Most Recent Games": first_test_text,
                             "Batting Stats": batting_stats_text,
                             "Bowling Stats": bowling_stats_text,
                             "All-Rounder Stats": all_rounder_stats_text}

                df_data = pd.DataFrame(data_dict)
                return df_data

                player_name = self.driver.find_element(By.XPATH, '//h2[@class="rankings-player-bio__name"]').text.lower().replace(' ', '-')
                filename = os.path.join("raw data", f"{player_name}.json")
                with open(filename,"w") as file:
                                file.write(f"First and Most Recent Games \n\n {first_test_text}\n")

                                file.write(f"\nBatting Stats\n\n {batting_stats_text}\n")
                                
                                file.write(f"\nBowling Stats\n\n{bowling_stats_text}\n")

                                file.write(f"\nAll-Rounder Stats\n\n{all_rounder_stats_text}\n")

                

                dat

        

        def get_player_info(self):
            self.bat_stats()
            self.bowling_stats()
            self.all_rounder_stats()
            self.writing_up_data()


no1 = DataScraper()
no1.current_batters()
no1.get_current_batters_info()