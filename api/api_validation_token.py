from xml.dom import ValidationErr
import requests
import credentials

def validation_token():
  url = f"{credentials.url}/token/check"
  params = {
    'token': credentials.token
  }
  response = requests.get(url=url,params=params)
  if(response.status_code == 208):
    raise ValidationErr(response.status_code)
  if(response.status_code != 200):
    raise Exception('Invalid response')
  return response.json()