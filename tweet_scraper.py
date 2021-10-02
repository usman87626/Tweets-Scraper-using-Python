## IMPORTS
import snscrape.modules.twitter as sntwitter #Module to scrap twitter
import pandas as pd
from tqdm import tqdm   #Module to show progress bar


## CLASS DEFINITION
class TwitterScraper(object):
    # Container for our scrapped data
    tweet_details = []
    #Constructor to initialize the Scraper
    def __init__(self,keywords,maxTweets,followerLimit):
        self.keywords = keywords
        self.maxTweets = maxTweets
        self.followerLimit = followerLimit
    
    # Function which takes output-filename.csv as argument (You can give the path as well like : data/filename.csv)
    def start_scraping(self,filename):
        for i,tweet in enumerate(tqdm(
                                    sntwitter.TwitterSearchScraper(self.keywords).get_items(),
                                    desc='Scraping',
                                    total=self.maxTweets+1
                                )):
            # Break when limits reaches
            if i > self.maxTweets:
                break
            # If followers are more than followerLimit sent via constructor
            if tweet.user.followersCount >= self.followerLimit:
                self.tweet_details.append([
                            tweet.id, 
                            tweet.user.username, 
                            tweet.content, 
                            tweet.date,
                            tweet.source,
                            tweet.user.location,
                            tweet.user.friendsCount,
                            tweet.user.followersCount,
                            tweet.mentionedUsers,
                            tweet.user.statusesCount,
                            tweet.user.created,
                            tweet.retweetCount,    
                        ])
        
                
        # Creating a dataframe from the tweets list above
        tweets_df = pd.DataFrame(self.tweet_details,
                         columns=[
                            'tweet_id',
                            'tweeter_name',
                            'tweet_text',
                            'tweet_date',
                            'source',
                            'location',
                            'following',
                            'followers',
                            'mentions',
                            'total_tweets',
                            'account_created_on',
                            'retweet_count',     
                        ])
        
        tweets_df.to_csv(filename,index=False)
        print(f"Success!! Data of {self.maxTweets} Tweets are scraped...")


## PARAMETERS TO PASS

# Keyword(s) to scrape
keywords = "#"
# How many tweets to scrap data from
tweets_to_scrape = 
# Scrape users having more than "N" followers
# Here N=10000
follower_condition = 
# CSV Output Filename Name For example output.csv
output_file = ""

# Creating Class and passing the parameters to constructor
twitter_scraper = TwitterScraper(keywords, tweets_to_scrape,follower_condition)
# Let's start the scraping
twitter_scraper.start_scraping(filename=output_file)
