import requests
import json

BASE_URL="http://localhost:8000/"
END_POINT1="welcome1"
END_POINT2="welcome2"
response1=requests.get(BASE_URL+END_POINT1)
response2=requests.get(BASE_URL+END_POINT2)
print(response1,type(response1))
print(response2,type(response2))
data1=response1.json()
data2=response2.json()
print(data1,data2,sep="\n")
print(type(data1),type(data2))
print(data1['msg'],data2['msg'])
data3=json.loads(response1.text)
print(data3,type(data3))

