import twitter_api

bot = twitter_api.TwitterAPIBot()

print("Authenticating...")
bot.authenticate()
print("Authentication complete.")

print("Performing search for tweets from @nytgraphics...")
stories = bot.getSearch(['from:MarshallProj'])
print("Search complete.")

print("Printing results...")
for t in stories:
  print(t)
