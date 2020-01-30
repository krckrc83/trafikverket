import requests
import tverketheader
import tverketresponse
import dbhelper

url = "https://api.trafikinfo.trafikverket.se/v1/data.json"

# i am looking for specific site. Hard code it now. Move it as program
# arg later. Compose header and body
flow = tverketheader.TrafficFlowCompose(regionid=4, county=1, site=914)
data_to_send = flow.compose_body()
headers = flow.compose_header()
print(data_to_send)
print(headers)
# Send HTTP POST request and get response
response = requests.post(url, data=data_to_send, headers=headers)
json_response = response.json()
print(json_response)
print(json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['MeasurementTime'])
print(json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['VehicleFlowRate'])
print(json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['AverageVehicleSpeed'])

# Frame response object
response = tverketresponse.TrafficFlowResponse(json_response)

# push to db
dbobj = dbhelper.DbHelper(response)
dbobj.push_data()
dbobj.remove_duplicates()
