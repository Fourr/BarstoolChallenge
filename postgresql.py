import psycopg2
from datetime import date
from RSSGathering import Gather
result = Gather()

conn = psycopg2.connect('dbname=barstool user=johnnysheffer')

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

x = result['messages']

for info in x:

	SQL = 'INSERT INTO podcast_episodes (podcast_name, episode_guid, episode_title, episode_date, episode_mp3) VALUES (%(podcast_name)s, %(episode_guid)s, %(episode_title)s, %(episode_date)s, %(episode_mp3)s);'

	data = info['data']
	cursor.execute(SQL, data)

	conn.commit()

conn.close()
cursor.close()

#print(result['messages'][0]['data'])