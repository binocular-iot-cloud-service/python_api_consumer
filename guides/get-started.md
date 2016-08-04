[//]: # (title: Get started with python)
[//]: # (description: Quick guide to get started using the Binocular API through the python SDK)
[//]: # (env: python)
# Getting started with Python

### 1. Clone the Python Sdk repository
`$ git clone https://github.com/binocular-iot-cloud-service/python_api_consumer.git`

### 2. Set credentials

Open the `binocularAPI.py` file and set your API key and client secret.

### 3. Make API Request

* Make sure your device have Internet connection
* Call the method `getDevicetypes()` 

At this point you should have some JSON data presented in your terminal (or equivalent) comming from Binocular.

### In bash/terminal
In bash you can test the script (after editing credentials) by preforming the following commands:
```bash
$ python
>>> import binocularAPI
>>> binocularAPI.getDevicetypes()
``````
### Example of some API call
Get all devicetypes

```python
>>> binocularAPI.getDevicetypes()
```
Get a device with the deviceId

```python
>>> binocularAPI.getDevice("55f6b42d54b75359b88b5315")
```

Get data from many device ids
```python
>>> binocularAPI.getDataFromManyDevices(["55f6b42d54b75359b88b5315", "55f6b42d54b75359b88b5316"])
```

Post some data by a deviceId. The data must conform to the,as specified in the Binocular cloud, data model.
```python
>>> binocularAPI.sendData("55f6b42d54b75359b88b5315", {"MyVar":"MyVal"})
```
Post some flags by a deviceId. The flags must conform to the,as specified in the Binocular cloud, flag model.
```python
>>> binocularAPI.setFlags("55f6b42d54b75359b88b5315", {"myFlag":"myFlagValue"})
```
### Data format
* Data must conform to definied datamodel in the Binocular cloud
* Flags must conform to definied flagmodels in the Binocular cloud