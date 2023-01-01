# AiCore  Data Collection Project
The goal was to create a data collection pipeline with a web scraping example

To run the scraper, pull the docker image by running ```docker pull aljay1/data_scraper_final``` and then run with ```docker run aljay1/data_scraper_final```


## Milestone 1 - Choosing the website

The website I chose to scrape from is https://www.icc-cricket.com/.
I am very passionate about cricket and there is lots od data to scrape from the website.


## Milestone 2 - Prototype Finding Target Pages

The PlayerScraper class in the ```player_data_scraper.py``` file was created in this milestone

In the ```find_correct_page``` function I navigated from the homepage to the mens test rankings page which is where I would scrape the data from.

With the ```click_element``` function, the xpath can be passed into the function
and then the scraper clicks on the webpage. This prevented a lot of hard-coding later on in the project.

Then in the ```current_batters```, ```current_bowlers```, and ```current_all_rounder_functions```, the scraper clicks on the links to reveal the full table of rankings and then return every link for each player in the rankings. This is so each one can be clicked and data can be scraped from each player.



## Milestone 3 - Retrieve Data From Target Pages

A child scraper of the PlayerScraper called DataScraper was created to keep things separate and make the code easier to follow.

Functions were created for each stat type and the for loop iterates through the container.

The ```scrape_stats``` function takes in the container as a argument, scrapes the single stat, and then returns to the corresponding key-value pair in a the ```stat_dict``` dictionary.

In the ```writing_up_data``` collects all the data and with ```json.dumps```, puts the data in a dictionary in a separate json file.
And folders were created for each player role.

In the ```image_scraper``` and ```download_img``` functions, images were downloaded with the ```.requests``` method and then put in the correct folder


## Milestone 4 - Documentation and Testing


In this milestone, I used unit tests in ```unit_test.py``` to make sure all parts of the scraper were working.

The ```test_click_element``` method tests the click_element function and also checks that each of the player role method is returning a list of the top 100 player profile links

The remaining functions in the script test, run the 3 ```{get_{player_role}_info}``` functions in the scraper.
The unit test checks if the test player has a dictionary of stats saved in the json, and the image has been downloaded and saved into the correct file path.


## Milestone 5 - Containerising the Scraper

A Docker image was setup to allow the scraper to run on any machine with any operating system.
Docker does not work with a GUI so a headless mode was implemented with the ```__options``` function to allow this to work.

The image was pushed to the Docker hub with the following command:
```docker push aljay1/data_scraper_final```


## Milestone 6 - Setting up a CI/CD pipline 

The CI pipline in the workflow main.yaml file pushes the Docker container onto the hub.

Secret variables were created to configure with Docker.
