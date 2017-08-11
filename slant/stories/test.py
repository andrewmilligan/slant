import npr_api

bot = npr_api.NPRAPIBot()

stories = bot.getNewsStories()

print(stories)
