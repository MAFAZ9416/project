import sqlite3
conn = sqlite3.connect('JAMAL.db')

cursor = conn.cursor()

# FOR LOCAL PATH TABLE
query = "CREATE TABLE IF NOT EXISTS LOCAL_PATH(ID INTEGER PRIMARY KEY, NAME VARCHAR(100),PATH VARCHAR(1000))"
cursor.execute(query)


# for insert perpose

# query = "INSERT INTO LOCAL_PATH VALUES (null,'Notepad++','C:\\Program Files\\Notepad++\\notepad++.exe')"
# cursor.execute(query)
# conn.commit()
# conn.close()

# for delete perpose

# query = " DELETE FROM PROJECT WHERE NAME = 'Notepad++'"
# cursor.execute(query)
# conn.commit()
# conn.close()

# query = "CREATE TABLE IF NOT EXISTS PROJECT(ID INTEGER PRIMARY KEY, NAME VARCHAR(100),PATH VARCHAR(1000))"
# cursor.execute(query)

# FOR WEB PATH TABLE

query = "CREATE TABLE IF NOT EXISTS WEB_PATH(ID INTEGER PRIMARY KEY, NAME VARCHAR(100),URL VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO WEB_PATH VALUES (null,'ChatGPT','https://chatgpt.com/?utm_source=google&utm_medium=paidsearch_brand&utm_campaign=GOOG_C_SEM_GBR_BackToSchool_CHT_SEA_ACQ_PER_MIX_ALL_APAC_IN_EN_082225&utm_term=chatgpt&utm_content=191102245624&utm_ad=771607822706&utm_match=e&gad_source=1&gad_campaignid=22930008418&gbraid=0AAAAA-IW-UWsFd0HOskxJlneClApsfRsc&gclid=CjwKCAiA24XJBhBXEiwAXElO39r_N_LCFQxIrUdOyXbET0M-rp0wpEPBZSPxKmHXhhXp8vG-5iRmPRoCmBMQAvD_BwE')"
cursor.execute(query)
conn.commit()
conn.close()