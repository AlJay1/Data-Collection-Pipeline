from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os
import requests


class PlayerScraper():
        '''
        This class is used to scrape cricket players from a website.
        '''

        def __init__(self, url = 'https://www.icc-cricket.com/homepage'):
                self.driver=webdriver.Chrome(ChromeDriverManager().install(), options= self.__options())
                self.driver.get(url)
                time.sleep(2)
                self.find_correct_page()


        def __options(self):
                '''
                This function allows the code to run in headless mode.
                '''
                chrome_options = Options()
                chrome_options.set_headless(headless=True)
                chrome_options.add_argument("--window-size=1920,1080")
                chrome_options.add_argument("--disable-notifications")
                chrome_options.add_argument('no-sandbox') 
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("disable-dev-shm-usage")
                chrome_options.add_argument("--disable-setuid-sandbox") 
                chrome_options.add_argument('--disable-gpu')
                return chrome_options

        def click_element(self, xpath, index=None):
                '''
                This function finds an element and then clicks on it.
                If the index is given, the .find_elements method is used to click
                '''
                if index == None:
                        element = self.driver.find_element(By.XPATH, xpath)
                        element.click()
                else:
                        elements = self.driver.find_elements(By.XPATH, xpath)[index]
                        elements.click()
                        

        def find_correct_page(self):
                '''
                This function navigates to the correct page. 
                '''
                self.click_element('//button[@class="linked-list__dropdown-label js-dropdown-btn"]', 3)
                 #finds the button to reveal the link for the rankings. Its the 4th button along the tab so the index is 3.

                time.sleep(2)                
                self.click_element('//a[contains(@href, "/rankings/mens/player-rankings")]')
                #finds the mens player rankings after opening the tab

                self.click_element('//a[@href="test"]')
                #clicks on the rankings for the test match format
                

        def current_batters(self):
                '''
                The following 3 function clicks on the full table for current batters, bowlers and all rounder.
                Then it returns the links for the profile of each player.
                '''

                self.click_element('//a[contains(@href, "/rankings/mens/player-rankings/test/batting")]')             
                #clicks to reveal the full batting rankings, only the first can be seen on the previous page.

                current_bat = self.driver.find_element(By.XPATH, '//table[@class="table rankings-table"]')
                #container for batting rankings
                link_bat = current_bat.find_elements(By.XPATH, './/a')[1:]
                #finds all the href links on the page. First value is sliced as the top player has two links
                return [bat.get_attribute('href') for bat in link_bat]
                #returns a list of all the links

                
        def current_bowlers(self):

                self.click_element('//a[contains(@href, "/rankings/mens/player-rankings/test/bowling")]')
                #clicks to reveal full bowler rankings

                current_bowl = self.driver.find_element(By.XPATH, '//table[@class="table rankings-table"]')          
                #finds the container for the bowlers
                link_bowl = current_bowl.find_elements(By.XPATH, './/a')[1:]
                return [bat.get_attribute('href') for bat in link_bowl]
                #return a list of all the links

        def current_all_rounder(self):

                self.click_element('//a[contains(@href, "/rankings/mens/player-rankings/test/all-rounder")]')
                #clicks to reveal full all rounder rankings

                current_all_round = self.driver.find_element(By.XPATH, '//table[@class="table rankings-table"]')                   
                #finds all rounder container
                link_all_round = current_all_round.find_elements(By.XPATH, './/a')[1:]
                return [bat.get_attribute('href') for bat in link_all_round]
                #returns a list of all the linkes

        def back_to_original_page(self):

                '''
                This function takes it back to he homepage, so the full table of other rankings can be clicked.
                This is only possible on the player profile page.
                '''
                self.click_element('//li[@class="rankings-menu__item"]', 2)
                #clicks the 3rd element in the table to get to back to the page of mens player rankings

                self.click_element('//a[@href="test"]')
                #clicks on the test format


class DataScraper(PlayerScraper):
        
        '''
        This class inherits from the PlayerScraper and  scrapes data from the player profiles page
        '''

        def __init__(self, url = 'https://www.icc-cricket.com/homepage'):
                super().__init__()


        def scrape_stats(self, role , container):

                '''
                This function scrapes test match stats from the player profile and returns in as a dictionary.
                The container is a variable because it allows this function to be used for batter, bowling, and all-rounder stats.
                '''

                stat_dict = {
                f"Latest {role} Ranking": " ",
                f"Latest {role} Rating": " ",
                
                f"Highest {role} Ranking": " ",
                f"Date achieved of highest {role} ranking": " ",

                f"Highest {role} Rating": " ",
                f"Data achieved of highest {role} rating" : " "
                }
                #empty dictionary which can be used for all 3 player roles

                latest_bat_rank = container.find_elements(By.XPATH, './/div[@class="rankings-player-stats__rankings-number rankings-player-stats__rankings-number--large"]')[0].text    
                latest_bat_rating = container.find_elements(By.XPATH, './/div[@class="rankings-player-stats__rankings-number"]')[0].text
                #finds the latest bat ranking and bat rating, the .text method is used to scrape the ratings into the dictionary
                
                highest_bat_rank = container.find_elements(By.XPATH, './/div[@class="rankings-player-stats__rankings-number rankings-player-stats__rankings-number--large"]')[1].text
                ranking_date_achieved = container.find_elements(By.XPATH, './/div[@class="rankings-player-stats__rankings-label rankings-player-stats__rankings-label--date"]')[0].text
                #finds the latest bowling ranking and bowling rating, the .text method is used to scrape the ratings into the dictionary

                highest_bat_rating = container.find_elements(By.XPATH, './/div[@class="rankings-player-stats__rankings-number"]')[1].text
                rating_date_achieved = container.find_elements(By.XPATH, './/div[@class="rankings-player-stats__rankings-label rankings-player-stats__rankings-label--date"]')[1].text
                #finds the latest bat ranking and bat rating, the .text method is used to scrape the ratings into the dictionary

                stat_dict.update(
                        {f"Latest {role} Ranking": latest_bat_rank,
                        f"Latest {role} Rating": latest_bat_rating, 

                        f"Highest {role} Ranking": highest_bat_rank,
                        f"Date Achieved of Highest {role} Ranking": ranking_date_achieved,
                        
                        f"Highest {role} Rating" : highest_bat_rating,
                        f"Data Achieved of Highest {role} Rating" : rating_date_achieved}
                        )
                
                return stat_dict
                #updates the dictionary with the scraped stats and returns them


        def get_bat_stats(self):
                
                '''
                The next three functions defines the container for batting, bowling and all-rounder stats.
                It then calls the scrape_stats function with the respective container as a variable, the position which is used in the dictionary that is return.
                '''
                bat_container = self.driver.find_elements(By.XPATH, '//div[@class="rankings-player-stats__type-wrapper js-ranking-container"]')[0]
                #the batting container appears first on the page so its index is one.
                return self.scrape_stats("Batting", bat_container)
                #calls self scrape function passing in the player role and container. It returns the dictionary of all the stats


        def get_bowl_stats(self):
                bowl_container = self.driver.find_elements(By.XPATH, '//div[@class="rankings-player-stats__type-wrapper js-ranking-container"]')[1]
                #test bowling stats appear second on the page so its index 1
                return self.scrape_stats("Bowling", bowl_container)

        def get_all_round_stats(self):
                all_round_container = self.driver.find_elements(By.XPATH, '//div[@class="rankings-player-stats__type-wrapper js-ranking-container"]')[2]
                #test all rounder stats appear second on the page so its index 2
                return self.scrape_stats("All-Rounder", all_round_container)


        def get_current_batters_info(self):
                '''
                The next 3 functions call the other functions that scrape the states, convert them to a dictionary and dumps into another folder.
                '''
                current_batter_links = self.current_batters()
                #calls the function which returns all the batter links

                current_batting_folder = "current-batting-rankings"
                Path(f"data/rankings/{current_batting_folder}").mkdir(parents=True, exist_ok=True)

                current_batting_image_folder = "current-batting-images"
                Path(f"data/images/{current_batting_image_folder}").mkdir(parents=True, exist_ok=True)
                #checks if folders for the stats and images are created. If not it creates them.                        

                for bat_links in current_batter_links:
                        self.driver.get(bat_links)
                        #clicks on every link
                        time.sleep(2)
                        batters_batting_stats = self.get_bat_stats()
                        batters_bowling_stats = self.get_bowl_stats()
                        batters_all_round_stats = self.get_all_round_stats()
                        #calls the function to scrape all the stats and returns 3 dictionaries.
                        self.writing_up_data(current_batting_folder, batters_batting_stats, batters_bowling_stats, batters_all_round_stats)
                        #calls the function to dump the data in a json file and save it in the correct folder which was defined above in this function
                        self.image_scraper(current_batting_image_folder)
                        #calls the function to download the player image and save it in the correct folder which was defined above in this function
                                
                self.back_to_original_page()
                #back to original page so the next player role rankings can be scraped


        def get_current_bowlers_info(self):

                current_bowl_links = self.current_bowlers()
                #calls the function which returns all the bowlers links

                current_bowling_folder = "current-bowling-rankings"
                Path(f"data/rankings/{current_bowling_folder}").mkdir(parents=True, exist_ok=True)
                current_bowling_image_folder = "current-bowling-images"
                Path(f"data/images/{current_bowling_image_folder}").mkdir(parents=True, exist_ok=True)
                #creates folders for images and rankings for bowlers

                for bowl_links in current_bowl_links:
                        self.driver.get(bowl_links)
                        #clicks on every link
                        time.sleep(2)
                        bowlers_batting_stats = self.get_bat_stats()
                        bowlers_bowling_stats = self.get_bowl_stats()
                        bowlers_all_round_stats = self.get_all_round_stats()
                        #returns 3 dictionaries with batting, bowling, and all rounder stats
                        self.writing_up_data(current_bowling_folder, bowlers_batting_stats, bowlers_bowling_stats, bowlers_all_round_stats)
                        self.image_scraper(current_bowling_image_folder)
                        #calls the functions to download images and dump data into json into the correct folders defined earlier in the function.
                        
                self.back_to_original_page()
                #back to original page so the next player role rankings can be scraped


        def get_current_all_rounder_info(self):
                
                current_all_rounder_links = self.current_all_rounder()
                #calls the function which returns all the all rounder links

                current_all_rounder_folder = "current-all-rounder-rankings"
                Path(f"data/rankings/{current_all_rounder_folder}").mkdir(parents=True, exist_ok=True)

                current_all_rounder_image_folder = "current-all-rounder-images"
                Path(f"data/images/{current_all_rounder_image_folder}").mkdir(parents=True, exist_ok=True)
                #creates folders for images and rankings for all-rounders

                for all_round_links in current_all_rounder_links:
                        self.driver.get(all_round_links)
                        #clicks on all the links
                        time.sleep(2)
                        all_rounder_batting_stats = self.get_bat_stats()
                        all_rounder_bowling_stats = self.get_bowl_stats()
                        all_rounder_all_round_stats = self.get_all_round_stats()
                        #returns 3 dictionaries with batting, bowling and all rounder stats
                        self.writing_up_data(current_all_rounder_folder, all_rounder_batting_stats, all_rounder_bowling_stats, all_rounder_all_round_stats)
                        self.image_scraper(current_all_rounder_image_folder)
                        #calls the functions to download images and dump data into json into the correct folders defined earlier in the function.
        
                self.back_to_original_page()
                #back to original page so the next player role rankings can be scraped


        def writing_up_data(self, folder, bat, bowl, all_round):

                '''
                This method dumps the stats in a dictionary in a json file.
                It takes the folder as variable so it can be put in the batting, bowling, or all-rounder folder.
                '''      

                #player name is scraped for the title of the json file.
                player_name = self.driver.find_element(By.XPATH, '//h2[@class="rankings-player-bio__name"]').text.lower().replace(' ', '-')
                filename = os.path.join(f"data/rankings/{folder}/" f"{player_name}.json")
                #folder is called in the get_{player_role}_info functions

                with open( filename, 'w') as file:

                        file.write("Test Batting Stats \n\n")
                        #title for battings stats
                        json.dump( bat, file, indent=4)
                        #dumps dictionary for batting stats
                        file.write("\n\nTest Bowling Stats \n\n")
                        #bowling stats title
                        json.dump (bowl, file, indent=4)
                        #dumps dictionary for bowling stats
                        file.write("\n\nTest All Rounder Stats\n\n")
                        #all rounder stats title
                        json.dump(all_round, file, indent=4)
                        #dumps dictionary for all rounder stats
                        #indent =4 separates each key value pair on different lines
                        

        def image_scraper(self, image_folder):
                
                '''
                The last two methods scrape the image from the player profile.
                And then put it into the respecitive file.
                '''
                image = self.driver.find_element(By.XPATH, '//img[@class="rankings-player-bio__player-image"]')
                img_src = image.get_attribute('src')
                #finds the image within the src attribute
                player_name = self.driver.find_element(By.XPATH, '//h2[@class="rankings-player-bio__name"]').text.lower().replace(' ', '-')
                #scrapes player name for image file title
                self.download_img(img_src, f"data/images/{image_folder}/{player_name}.jpg") 
                #calls the function to download the image, into the specific folder)


        def download_img(self, img_url, fp):

                img_data = requests.get(img_url).content
                #downloads the image with the .requests method 
                with open(fp, 'wb') as handler:
                        handler.write(img_data)
                        #puts the downloaded image into the folder.


    
if __name__ == "__main__":
    testing = DataScraper()
    testing.get_current_batters_info()
    testing.get_current_bowlers_info()
    testing.get_current_all_rounder_info()
