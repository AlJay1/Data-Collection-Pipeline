# Data-collection-project

# Milestone 1

Create GitHub repo


# Milestone 2

In this milestone I chose a website to scrape from. I am very passionate about cricket so I chose https://www.icc-cricket.com/


# Milestone 3

In this milestone and I created the Scraper Class and made a function to navigate to the correct page. I chose to scrape the data of the current top 100 batters, bowlers, and all-rounders in the test format. Then I made a method to find all of the links to their individual player profiles and click on each one.

# Milestone 4

This milestone required me to scrape the relevant data from the page. I scraped each players latest stats, and their highest ever stats with the .text method and used the json.dump method to dump the data into a json file in a specific folder. I also downloaded the image for each player and dumped it into a separate folder.

# Milestone 5 

In this milestone I optimised my code by making it more readable in the json file. I made a dictionary in the scrape_stats function which would make the stats very clear to read and allowed me to get rid of a lot of unnecessary code because I could define the player role and container. I no longer needed 3 different functions for each different player role.

# Milestone 6
In this milestone I set up a docker image and container for my code to allow it run on any machine with any operating system. I had to add in a headless mode to allow this to work.

I then pushed it into the docker hub.


# Milestone 7
I created a pipline for the docker container. I created a workflow yaml file and created secrets to allow me to login to docker.
