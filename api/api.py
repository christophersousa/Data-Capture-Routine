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
    return{
      "total": 0,
      "has_more": False,
      "deals": []
    }
  return response.json()

def request_organization(page:int):
  print(f"Request organization page: {page}")
  url = f"{credentials.url}/organizations"
  params = {
    'token': credentials.token,
    'limit': 20,
    'page': page
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
    return{
      "total": 0,
      "has_more": False,
      "organizations": []
    }
  return response.json()

def request_activities(page:int, dateStart:str, dateEnd:str):
  print(f"Request activities page: {page}")
  url = f"{credentials.url}/activities"
  params = {
    'token': credentials.token,
    'limit': 200,
    'page': page,
    'start_date': dateStart,
    'end_date': dateEnd
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
    return{
      'activities': []
    }
  return response.json()


def request_contacts(q:str):
  print(f"Request contacts")
  url = f"{credentials.url}/contacts"
  params = {
    'token': credentials.token,
    'limit': 200,
    'q': q
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
     return{
      "total": 0,
      "has_more": False,
      "contacts": []
    }
  return response.json()

def request_contacts(q:str):
  print(f"Request contacts")
  url = f"{credentials.url}/contacts"
  params = {
    'token': credentials.token,
    'limit': 200,
    'q': q
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
     return{
      "total": 0,
      "has_more": False,
      "contacts": []
    }
  return response.json()

def request_users():
  print(f"Request contacts")
  url = f"{credentials.url}/users"
  params = {
    'token': credentials.token,
    # 'active': active
  }
  response = requests.get(url=url,headers=headers,params=params)
  if(response.status_code != 200):
     return{
      "users": []
    }
  return response.json()