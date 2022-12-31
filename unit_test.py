import unittest
from  unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from player_data_scraper import DataScraper
import os

class TestPlayerScraper(unittest.TestCase):

    def setUp(self):
        #Create an instance of the DataScraper class
        self.scraper = DataScraper()           

    def test_click_element(self):
        # Test the click_element method
    
        bat_links = self.scraper.current_batters()
        self.assertTrue(len(bat_links) == 100)
        #checks the current_batter function returns a list of 100 links
        self.scraper.back_to_original_page()
        #returns to original page each text so next unit test can run

        bowl_links = self.scraper.current_bowlers()
        self.assertTrue(len(bowl_links) == 100)
        #checks the current_bowler function returns a list of 100 links       
        self.scraper.back_to_original_page()

        all_rounder_links = self.scraper.current_bowlers()
        self.assertTrue(len(all_rounder_links) == 100)
        self.scraper.back_to_original_page()
    
    
    def test_batting_folders(self):
        #Test the get_current_batters_info method

        test_batter = "marnus-labuschagne"
        self.scraper.get_current_batters_info()

        # Check if the data was saved to a JSON file in the correct path
        self.assertTrue(os.path.exists(f"data/rankings/current-batting-rankings/{test_batter}.json"))
        # Check if the image was downloaded and saved in the correct path
        self.assertTrue(os.path.exists(f"data/images/current-batting-images/{test_batter}.jpg"))

        self.scraper.back_to_original_page()


    def test_bowling_folders(self):
        #Test the get_current_bowlers_info method
        test_bowler = "pat-cummins"
        self.scraper.get_current_bowlers_info()

        # Check if the data was correctly saved to a JSON file
        self.assertTrue(os.path.exists(f"data/rankings/current-bowling-rankings/{test_bowler}.json"))
        # Check if the image was correctly saved to a file
        self.assertTrue(os.path.exists(f"data/images/current-bowling-images/{test_bowler}.jpg"))
        self.scraper.back_to_original_page()

    def test_all_rounder_folders(self):
        #Test the get_current_all_rounder_info method
        test_all_rounder = "ravindra-jadeja"
        self.scraper.get_current_all_rounder_info()

        # Check if the data was correctly saved to a JSON file
        self.assertTrue(os.path.exists(f"data/rankings/current-all-rounder-rankings/{test_all_rounder}.json"))
        # Check if the image was correctly saved to a file
        self.assertTrue(os.path.exists(f"data/images/current-all-rounder-images/{test_all_rounder}.jpg"))
        self.scraper.back_to_original_page()

       
unittest.main(argv=[''], verbosity=2, exit=False)