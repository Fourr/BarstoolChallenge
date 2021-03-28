#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='USER',
    password='PASSWORD',
    account='ACCOUNT'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
    cs.execute("CREATE DATABASE IF NOT EXISTS CHALLENGE_DB")
    cs.execute("USE DATABASE CHALLENGE_DB")
    cs.execute("CREATE SCHEMA IF NOT EXISTS CHALLENGE_SCHEMA")

    cs.execute("USE SCHEMA CHALLENGE_DB.CHALLENGE_SCHEMA")
    cs.execute(
        "CREATE OR REPLACE TABLE "
        "podcast_episodes(podcast_name string, episode_guid string, episode_title string, episode_date date, episode_mp3 string)")

    # cs.execute(
    #     "INSERT INTO podcast_episodes(col1, col2) VALUES " + 
    #     "    (123, 'test string1'), " + 
    #     "    (456, 'test string2')")
finally:
    cs.close()
ctx.close()