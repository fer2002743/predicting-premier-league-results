#importing the libraries we are going to use
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


""" #step one:getting the standings table
#standings_url = "https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0"}

#standings_page = requests.get(standings_url, headers = headers)
#print(standings_page)

#soup = BeautifulSoup(standings_page.text, "html.parser")
#standings_table = soup.select("table.stats_table")[0] #this is a css selector. table is the tag and stats_table is the class



#step two: getting all the links of each team. For such purpose I will create one function.
def getting_team_links(standings_table):
    all_links = []#here we will store all the links we find in the table
    for link in standings_table.find_all("a"):#searching for the "a" tags all over the table
        all_links.append(link.get("href"))#adding the "href" (that includes link) to the list "all_links"


    team_links_dirty = [] #here we will store only the parcial links of each team
    for link in all_links: #with the condition I only select the url of each team
        if "/en/squads/" in str(link):#use the str() otherwise I will get an error because the "link" in theory does not have data type
            team_links_dirty.append(link)

    team_links = [] #here is where I will actually store the absolute links
    for links in team_links_dirty:
        team_links.append(f"https://fbref.com{links}")#adding the parcial link we go above with the initial url of the website
    return team_links #final list with all the links of each team

#team_links = getting_team_links(standings_table)


#step three: getting the table scores and features of each team
#team_page = requests.get("https://fbref.com/en/squads/d3fd31cc/Everton-Stats")
#soup = BeautifulSoup(team_page.text, "html.parser")
#scores_and_features_table = soup.find_all("table", id = "matchlogs_for")[0]
#matches = pd.read_html(str(scores_and_features_table))
#another way of getting the scores and features table is:
#matches_table = pd.read_html(team_page.text, match = "Scores & Fixtures")

#the above block of code worked for just one team. Now I will make it work for all the teams and also for the last season
years = list(range(2022, 2020, -1))
matches_stats = pd.DataFrame() #df where we are going to store all the matches stats
standings_url = "https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats" #same url as in the beginning

for year in years:
    #first we get the standings table
    data = requests.get(standings_url)
    soup = BeautifulSoup(data.text, "html.parser")
    standings_table = soup.select("table.stats_table")[0]

    #second we get the links for each team
    teams_urls = getting_team_links(standings_table)
    

    #in this part I will add the code to access different seasons
    previous_season = soup.select("a.prev")[0].get("href")
    standings_url = f"https://fbref.com{previous_season}"

    #third we enter into each link and get the matches stats
    for team_url in teams_urls:
        data = requests.get(team_url) """
"""         team_table = pd.read_html(data.text, match="Scores & Fixtures")
        matches_stats.append(team_table)
        time.sleep(5)#never forget to make request slowly. Otherwise I will get blocked




#print(matches_stats[0])
 """


#step 4: We are going to get the shooting statistics of each team
#To do this: first I will get into the link of each team.
#second: get the url of the shooting statistics
#third: enter into such link and then get the table
#fourth: do this for all the teams



#function to get the shooting links of each team
def getting_shooting_links(team_page):
    all_links = []#here we will store all the links we find in the table
    for link in team_page.find_all("a"):#searching for the "a" tags all over the table
        all_links.append(link.get("href"))#adding the "href" (that includes link) to the list "all_links"


    shooting_links_dirty = [] #here we will store only the parcial links of each team
    for link in all_links: #with the condition I only select the url of each team
        if "/all_comps/shooting/" in str(link):#use the str() otherwise I will get an error because the "link" in theory does not have data type
            shooting_links_dirty.append(link)

    shooting_links = [] #here is where I will actually store the absolute links
    for links in shooting_links_dirty:
        shooting_links.append(f"https://fbref.com{links}")#adding the parcial link we go above with the initial url of the website
    return shooting_links[0] #To get only one link



#getting shooting statistics of all teams
#shooting_df = pd.DataFrame()
#for year in years:
    #data = requests.get(standings_url)
    #soup = BeautifulSoup(data.text, "html.parser")
    #standings_table = soup.select("table.stats_table")[0]

    #second we get the links for each team
    #teams_urls = getting_team_links(standings_table)
    
    #code to get data from previous season
    #previous_season = soup.select("a.prev")[0].get("href")
    #standings_url = f"https://fbref.com{previous_season}"

    #for team_url in teams_urls:
        #team_page = requests.get(team_url)
        #parsed_team_page = BeautifulSoup(team_page.text, "html.parser")
       # shooting_url = getting_shooting_links(parsed_team_page)
      #  shooting_page = requests.get(shooting_url)
     #   parsed_shooitng_page = BeautifulSoup(shooting_page.text, "html.parser")
    #    shooting_table = parsed_shooitng_page.find_all("table", id = "matchlogs_for")[0]
   #     pretty_table = pd.read_html(str(shooting_table))[0]
  #      shotting_table = pretty_table.columns.droplevel()
 #       shooting_df.append(shooting_table)
#        time.sleep(3)




#finally we just need to concat all of this data

standings_url = "https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"



def getting_team_links(standings_table):
    all_links = []#here we will store all the links we find in the table
    for link in standings_table.find_all("a"):#searching for the "a" tags all over the table
        all_links.append(link.get("href"))#adding the "href" (that includes link) to the list "all_links"


    team_links_dirty = [] #here we will store only the parcial links of each team
    for link in all_links: #with the condition I only select the url of each team
        if "/en/squads/" in str(link):#use the str() otherwise I will get an error because the "link" in theory does not have data type
            team_links_dirty.append(link)

    team_links = [] #here is where I will actually store the absolute links
    for links in team_links_dirty:
        team_links.append(f"https://fbref.com{links}")#adding the parcial link we go above with the initial url of the website
    return team_links #final list with all the links of each team

years = list(range(2022, 2020, -1))



all_matches = []
for year in years:
    data = requests.get(standings_url)#getting inital page
    soup = BeautifulSoup(data.text, "html.parser")#parsing it
    standings_table = soup.select("table.stats_table")[0]#getting the standings table

    #second we get the links for each team
    teams_urls = getting_team_links(standings_table)#obataining the links to the statistics of each team 
    #code to get data from previous season
    previous_season = soup.select("a.prev")[0].get("href")#getting the link to the previous season page
    standings_url = f"https://fbref.com{previous_season}"#creating the link to the previous season page

    for team_url in teams_urls:
        data = requests.get(team_url)#getting the page of each team
        team_table = pd.read_html(data.text, match="Scores & Fixtures")[0]
        #with the above 2 lines of code I am getting the scores and fixtures table
        parsed_team_page = BeautifulSoup(data.text, "html.parser")#parsing team page
        shooting_url = getting_shooting_links(parsed_team_page)#getting the shooting URL
        shooting_page = requests.get(shooting_url)#Getting the shooting page 
        parsed_shooitng_page = BeautifulSoup(shooting_page.text, "html.parser")#parsing the shooting page
        shooting_table = parsed_shooitng_page.find_all("table", id = "matchlogs_for")[0]#getting the shooting table
        pretty_shooting_table = pd.read_html(str(shooting_table))[0]#reading the shooting table using pandas to get it "pretty"
        pretty_shooting_table.columns = pretty_shooting_table.columns.droplevel()#getting rid of the upper title cell
        #the block of code written above is used to get the shooting table
        #merging the match stats table with the shoooting stats.
        try:#I use the try because for some teams match stats and shooting stats table has different sizes
            team_data = team_table.merge(pretty_shooting_table[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
        except ValueError:
            continue
        #selecting only premier league matches
        team_data = team_data[team_data["Comp"] == "Premier League"]
        team_data["Season"] = year
        #getting the team name 
        team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
        team_data["Team"] = team_name#create a column with the team name
        all_matches.append(team_data)
        time.sleep(3)#sleep for 3 seconds to make sure the website does not block me


#cocatenating all the matches
matches_statistics = pd.concat(all_matches)
#converting all the column names into lowercase(this is just a good practice, you do not need to do it)
matches_statistics.columns = [c.lower() for c in matches_statistics.columns]
#creating the CSV file
matches_statistics.to_csv("matches_statistics.csv")

print(matches_statistics)