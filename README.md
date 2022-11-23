# Data-collection-project

# Milestone 1

Create GitHub repo


# Milestone 2

In this milestone I chose a website to scrape from. I am very passionate about cricket so I chose https://www.icc-cricket.com/

import player_scraper.py 

# Milestone 3

In this milestone I used selenium to created the PLayerScraper Class in the player_scraper.py file.

In the find_correct_page function I navigated from the homepage to the mens test rankings page which is where I would scrape the data from.
With the click_element function I can just path in the xpath into the function to make it a lot easier

Then with the current_batters, current_bowlers, and current_all_rounder functions, I clicked on the links to reveal the full table of rankings and then return every link for each player in the rankings. This is so each one can be clicked and data can be scraped from each player.



# Milestone 4

This milestone required me to scrape the relevant data from the page.
I created a child scraper of the PlayerScraper called DataScraper in the data_scraper.py file. I did this to keep things separate and it was a lot easier to follow.

I made a data container I would scrape from in the init method so I would not have to define it in each stat type.

I then made functions for each players first test, batting, bowling and all rounder stats. The for loop iterates through the container, and the .text method scrapes any text available from that section of the page into a list.
I then return it with ''.join method to create spaces between stats to make it eassier to read.

In the writing_up_data function, it calls the functions that scrapes the data, and puts them into a dictionary and dumps it a json file with the json.dumps method.

The get_{player_role}_info ties all of it together by iterating through the lists of links return from the methods created in milestone 3.


# Milestone 5 

In this milestone I optimised my code by making the data more user friendly.
Previously all the date was clumped together and it was very difficult to read, and there were multiple stats on a single line.

I made a new file data_scraper_v2.py to improve this.
The scrape stats function return each individual stat within the batting, bowling and all rounder containers into a dictionary. This method just scraped the actual ratings and rankings numbers, and were matched to the key:vale pair in the stat_dict dictionary. 

This made it a lot easier to read; previously all the text in the section was scraped so all the stats were clumped together and was not in a visually appealing presentation.

And having the container as a parameter prevented me from having to write a lot of similar code for each player role. In the get_{player_role}_stats function I could just define the container for either batting, bowling, or all rounder, and then I could call the scrape_stats function.
Also I created folders for each player role if they were not already present for dictionaries to be stored.

In the image_scraper and download_img functions, I downloaded the images with .requests function, then scraped the player name to get the title of the image file
also put them in the correct folder.


# Milestone 6

In this milestone I set up a docker image and container for my code to allow it run on any machine with any operating system. Docker does not work with a GUI so 
I had to add in a headless mode with the __options function to allow this to work.

I then pushed it into the docker hub.

# Milestone 7
Lastly, I created a pipline for the docker container. This would push my docker container to the hub.
I created a workflow main.yaml file and created secrets in github with my docker username and passwords which would allow me to login to docker to push to the hub.
