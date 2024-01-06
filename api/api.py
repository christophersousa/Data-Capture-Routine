import requests
import credentials
# Url and Headers
headers = {"accept": "application/json"}

# Requests
def request_deals(page:int, dateStart:str, dateEnd:str):
  print(f"Request deals page: {page}")
  url = f"{credentials.url}/deals"
  params = {
    'token': credentials.token,
    'limit': 200,
    'page': page,
    'start_date': dateStart,
    'end_date': dateEnd
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
    raise Exception('Invalid response in list_deals')
  return response.json()

def request_organization(page:int):
  print(f"Request deals page: {page}")
  url = f"{credentials.url}/organizations"
  params = {
    'token': credentials.token,
    'limit': 200,
    'page': page
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
    raise Exception('Invalid response in list_deals')
  return response.json()