from xml.dom import ValidationErr
import datetime
from api.api_validation_token import validation_token
from processing.requests_datas import list_deals, list_organizations,list_activities
from processing.mapping_data import mapping_deal, mapping_activities, mapping_organization
from credentials import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.entity import Base

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
    print(f"\n---------- date start {dateStart} date end {dateEnd}\n")

    # Requests
    print(f"\n---------- Request Deals ----------\n")
    deals = list_deals(dateStart, dateEnd)
    print(f"\n---------- Request Resumes ----------\n")
    resume = list_activities(dateStart, dateEnd)
    print(f"\n---------- Request Organizations ----------\n")
    organizations = list_organizations()
    # Opening connection with the bank
    engine = create_engine(DATABASE_URL)

    # Creating tables
    Base.metadata.create_all(engine)

    print("---------- Connect bank! ----------")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Register datas
    print(f"\n---------- Register Organization ----------\n")
    mapping_organization(organizations,session)
    print(f"\n---------- Register Deals ----------\n")
    mapping_deal(deals,session)
    print(f"\n---------- Register Resume ----------\n")
    mapping_activities(resume,session)
    
  except ValidationErr:
    print("Incorrect validation, check authentication token")
  except Exception as e:
    print(f"An unexpected error occurred, error: :{e}")
