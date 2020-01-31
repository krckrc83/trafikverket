""" This is the worker program which does everything """
import requests
import tverketheader
import tverketresponse
import dbhelper

url = "https://api.trafikinfo.trafikverket.se/v1/data.json"

# @ToDo i am looking for specific site. Hard code it now. Move it as program arg later. Compose header and body

flow = tverketheader.TrafficFlowCompose(regionid=4, county=1, site=914)
data_to_send = flow.compose_body()
headers = flow.compose_header()

# Send HTTP POST request and get response
response = requests.post(url, data=data_to_send, headers=headers)
json_response = response.json()

# Frame response object
response = tverketresponse.TrafficFlowResponse(json_response)

# push to db
dbobj = dbhelper.DbHelper(response)
dbobj.push_data()
# Sometimes data may not be updated for long time which will cause redundant entries.
dbobj.remove_duplicates()
