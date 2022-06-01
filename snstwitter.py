import snscrape.modules.twitter as snstwitter
import pandas as pd
import time

query = 'UCL lang:en until:2022-05-31 since:2022-05-28'
tweets = []
limit = 10000

start = time.time()
counter = 0
for tweet in snstwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        counter += 1
        tweets.append([counter, tweet.date, tweet.user.username, tweet.content])
        
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
df = pd.DataFrame(tweets, columns=['No', 'Date', 'Username', 'Tweet'])
print(df)
print("End ind {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
df.to_csv('tweet.csv', index=False)