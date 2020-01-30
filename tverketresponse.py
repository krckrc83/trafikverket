class TrafficFlowResponse(object):

    sql = "INSERT INTO trafficflow (flow, speed, time) VALUES (%s, %s, %s)"

    def __init__(self, json_response):
        self.flow = json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['VehicleFlowRate']
        self.speed = json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['AverageVehicleSpeed']
        self.time = json_response['RESPONSE']['RESULT'][0]['TrafficFlow'][0]['MeasurementTime']
        self.values = (self.flow, self.speed, self.time)

