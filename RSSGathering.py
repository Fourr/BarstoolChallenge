import feedparser
from datetime import date

def Gather():
	urls = {
		"The Daily": "https://feeds.simplecast.com/54nAGcIl",
		"NPR News Now": "https://feeds.npr.org/500005/podcast.xml",
		"Up First": "https://feeds.npr.org/510318/podcast.xml",
		"The Ben Shapiro Show": "https://feeds.megaphone.fm/WWO8086402096",
		"Stuff You Should Know": "https://feeds.megaphone.fm/stuffyoushouldknow",
		"Dateline NBC": "https://podcastfeeds.nbcnews.com/dateline-nbc",
		"This American Life": "http://feed.thisamericanlife.org/talpodcast",
		"The Dan Bongino Show": "https://feeds.megaphone.fm/WWO3519750118",
		"NPR Politics": "https://feeds.npr.org/510310/podcast.xml",
		"Call Her Daddy": "https://mcsorleys.barstoolsports.com/feed/call-her-daddy",
		"Pardon My Take": "https://mcsorleys.barstoolsports.com/feed/pardon-my-take"
	}
	message = {}
	message["messages"] = []
	for url in urls:
		print(url)
		
		parse = feedparser.parse(urls[url])

		for entry in parse['entries']:

			year = str(entry.published_parsed[0])
			month = str(entry.published_parsed[1])
			day = str(entry.published_parsed[2])
			if(len(month) < 2):
				month = '0' + month
			
			if(len(day) < 2):
				day = '0' + day


			formated_date = date(int(year),int(month),int(day))
			data = {
				"podcast_name": url,
				"episode_guid": entry.id,
				"episode_title": entry.title,
				"episode_date": formated_date,
				}
			try: 
				data["episode_mp3"] = entry.links[1].href
			except IndexError: 
				data["episode_mp3"] = entry.links[0].href
			entries = {
				"action": 'upsert',
	        	"sequence": 0,
	        	"data": data
	        }

			message["messages"].append(entries)

	return(message)