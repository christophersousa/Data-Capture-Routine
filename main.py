from xml.dom import ValidationErr
import datetime
from api.api_validation_token import validation_token
from processing.requests_datas import list_deals
def Main():
  try:
    valid_token = validation_token()
    if(valid_token is None):
      raise Exception("Invalid user")
    current_time = datetime.datetime.now()
    dateEnd = current_time.strftime('%Y-%m-%dT%H:%M:%S')
    last_day = current_time - datetime.timedelta(days=2)
    dateStart = last_day.strftime('%Y-%m-%dT%H:%M:%S')
    message = 'Requesting data from the last 2 days!'

    print(f"\n---------- {message} ----------\n")
    print(f"\n---------- date start {dateStart} date end {dateEnd}")
    deals = list_deals(dateStart, dateEnd)
    print(len(deals))
  except ValidationErr:
    print("Incorrect validation, check authentication token")
  except Exception as e:
    print(f"An unexpected error occurred, error: :{e}")
