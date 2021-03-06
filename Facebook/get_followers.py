import requests
import json
import datetime
import pandas as pd

#---facebook---#
token='<<Your Token >>'
action="/v3.2/me?fields=id,name,fan_count,instagram_accounts{followed_by_count}"

#---dataframe---#
df= pd.DataFrame(columns=['InsertTimeRecordUTC','social_platform','followers_count'])

today = datetime.date.today()
#---facebook---#
r = requests.get("https://graph.facebook.com/"+action+"&access_token="+token).text
json_data = json.loads(r.strip())
df = df.append({'InsertTimeRecordUTC'   : today,
                'social_platform' : 'facebook' ,
                'followers_count': json_data['fan_count']},ignore_index=True)

coolaResult = df
