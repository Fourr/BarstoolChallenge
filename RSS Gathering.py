import feedparser
from datetime import datetime

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
for url in urls:
	print(url)
	message[url] = []
	parse = feedparser.parse(urls[url])

	for entry in parse['entries']:
		# Entries = []
		# Entries.append(url)
		year = str(entry.published_parsed[0])
		month = str(entry.published_parsed[1])
		day = str(entry.published_parsed[2])
		if(len(month) < 2):
			month = '0' + month
		
		if(len(day) < 2):
			day = '0' + day

		date = year + '-' + month + '-' + day

		Entries = {
				"podcast_name": url,
				"episode_guid": entry.id,
				"episode_title": entry.title,
				"episode_date": date,
				}
		try: 
			Entries["episode_mp3"] = entry.links[1].href
			# Entries.extend([entry.id,entry.title,date,entry.links[1].href])
		except IndexError: 
			# Entries.extend([entry.id,entry.title,date,entry.links[0].href])
			Entries["episode_mp3"] = entry.links[0].href

		message[url].append(Entries)

from pprint import pprint
pprint(message)



