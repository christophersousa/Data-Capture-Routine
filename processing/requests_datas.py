from api.api import request_contacts, request_deals, request_organization, request_activities,request_users
from processing.format import format_contact

def list_deals(dateStart:str, dateEnd:str):
    deals_list = []
    page = 1
    response = request_deals(page,dateStart,dateEnd)
    deals_list.extend(response['deals'])
    if response['has_more']:
      page += 1
      while page <=2:
        try:
          response = request_deals(page,dateStart,dateEnd)
          deals_list.extend(response['deals'])
          if not response['has_more']:
            break
          page += 1
        except Exception as e:
          print(f'Error in request_deals in page {page}. \nError: {e}')
    return deals_list

def list_organizations():
    organizations_list = []
    page = 1
    response = request_organization(page)
    organizations_list.extend(response['organizations'])
    if response['has_more']:
      page += 1
      while page <= 2:
        try:
          response = request_organization(page)
          organizations_list.extend(response['organizations'])
          if not response['has_more']:
            break
          page += 1
        except Exception as e:
          print(f'Error in request_organization in page {page}. \nError: {e}')
    return organizations_list

def list_activities(dateStart:str, dateEnd:str):
    activities_list = []
    page = 1
    response = request_activities(page, dateStart, dateEnd)
    activities_list.extend(response['activities'])
    if response['has_more']:
      page += 1
      while page <= 2:
        try:
          response = request_activities(page, dateStart, dateEnd)
          activities_list.extend(response['activities'])
          if not response['has_more']:
            break
          page += 1
        except Exception as e:
          print(f'Error in request_organization in page {page}. \nError: {e}')
    return activities_list

def request_contact_name(name:str):
  response = request_contacts(name)
  response_format = format_contact(response['contacts'][0])
  return response_format

def request_users_app():
  response = request_users()
  return response['users']
