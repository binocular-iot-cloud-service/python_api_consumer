import requests
import json
import base64

## Credentialas goes here
api_key = "[API_KEY goes here]"
client_secret = "[CLIENT SECRET GOES HERE]"

def __createHeaderAuth():
	return 'Basic ' + base64.b64encode(api_key + ':' + client_secret)

s = requests.Session()
headers = {'Content-type': 'application/json','Authorization': __createHeaderAuth()}
BASE_URL = "http://api.binocular.se/v1/"


def getDevicetypes():
	r = s.get(BASE_URL + 'devicetypes', headers=headers)
	return r.text

def getDevices(devicetypeId):
	r = s.get(BASE_URL + 'devicetypes/' + devicetypeId + "/devices", headers=headers)
	return r.text

def getDevice(deviceId):
	r = s.get(BASE_URL + 'devices/' + deviceId, headers=headers)
	return r.text

def getDataEntry(entryId):
	r = s.get(BASE_URL + 'data/' + entryId, headers=headers)
	return r.text

def getData(deviceId):
	r = s.get(BASE_URL + 'devices/' + deviceId, headers=headers)
	return r.text

def getDataFromManyDevices(idArray):
	r = s.post(BASE_URL + 'devices/data', data=json.dumps(idArray), headers=headers)
	return r.text

def getDevices():
	r = s.get(BASE_URL + 'devices/', headers=headers)
	return r.text

def sendData(deviceId, data):
	r = s.post(BASE_URL + 'devices/'+deviceId + '/data', data=json.dumps(data), headers=headers)
	return r.text

def getFlags(deviceId): 
	r = s.get(BASE_URL + 'devices/' + deviceId + '/flags', headers=headers)
	return r.text	

def setFlags(deviceId, flagData):
	r = s.post(BASE_URL + 'devices/'+deviceId + '/flags', data=json.dumps(flagData), headers=headers)
	return r.text

def heartbeat(deviceId): 
	r = s.get(BASE_URL + 'devices/' + deviceId + '/heartbeat', headers=headers)
	return r.text	

def activateDevice(devicetypeId):
	r = s.post(BASE_URL + 'devicetypes/'+devicetypeId + '/activate_device', data=json.dumps({}), headers=headers)
	return r.text