from pytrends.request import TrendReq
import pandas
import random



pytrends = TrendReq(hl='en-US', tz = 360)

# trendingsearches = (pytrends.trending_searches(pn='united_states'))

realtimesearchtrends = (pytrends.realtime_trending_searches(pn='US'))

value1 = realtimesearchtrends.at[random.randint(0,78),'entityNames']
x = 0
list1 = []

for i in range(1,20):
    print(i)
    while x <= 2:
        print(random.choice(value1))
        value1 = realtimesearchtrends.at[random.randint(0,78),'entityNames']
        x += 1
    x = 0


   
