from api.api import request_deals, request_organization
def list_deals(dateStart:str, dateEnd:str):
  try:
    deals_list = []
    page = 1
    response = request_deals(page,dateStart,dateEnd)
    deals_list.extend(response['deals'])
    if response['has_more']:
      page += 1
      while True:
        try:
          response = request_deals(page,dateStart,dateEnd)
          deals_list.extend(response['deals'])
          if not response['has_more']:
            break
          page += 1
        except Exception as e:
          print(f'Error in request_deals in page {page}. \nError: {e}')
    return deals_list
  except Exception as e:
    print(f"Error in request_deals. \nError: {e.message}")
    raise e

def list_organizations():
  try:
    organizations_list = []
    page = 1
    response = request_organization(page)
    organizations_list.extend(response['organizations'])
    if response['has_more']:
      page += 1
      while page <= 5:
        try:
          response = request_organization(page)
          organizations_list.extend(response['organizations'])
          if not response['has_more']:
            break
          page += 1
        except Exception as e:
          print(f'Error in request_organization in page {page}. \nError: {e}')
    return organizations_list
  except Exception as e:
    print(f"Error in request_organization. \nError: {e.message}")
    raise e

