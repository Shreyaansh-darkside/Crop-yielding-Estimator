import requests

url = "https://api.awhere.com/oauth/token"

payload = "grant_type=client_credentials"
headers = {
    'Authorization': "Basic ZjRLUEl6dk1uRk9DcnZRUVNRQWltbDNkZ0xkeElHTG86eHBVZWs1SW5XTDN5T2hWSQ==",
    'Host': "api.awhere.com",
    'Content-Type': "application/x-www-form-urlencoded",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

res = requests.request("POST", url, data=payload, headers=headers)

print(res.json())
token = res.json()
access_token = token.get("access_token")



url = "https://api.awhere.com/v2/agronomics/fields/field1/agronomicnorms/07-01,07-01/years/2017,2019"

headers = {
    'Authorization': "Bearer "+ access_token,
    'Host': "api.awhere.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()
print(data)
#input_data = data.get("averageAccumulations")
#pet = input_data.get("pet")
#ppet = input_data.get("ppet")
#print(pet)
#print(ppet)





#def date_input():
#    url = "https://api.awhere.com/v2/agronomics/fields/field1/agronomicnorms/07-01,07-01/years/2017,2019"
#    date = input('Enter date in this way: mm-dd,mm-dd = ')
#    ur = url.split("/")
#    ur[-3] = ur[-3].replace(ur[-3],date)
#    url = "/".join(ur)
#    return url
