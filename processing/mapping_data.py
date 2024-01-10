from processing.pesist_data import add_deal, add_organization, add_resume
from processing.format import format_organization, format_deals, format_resume

def mapping_deal(deals, session):
  for deal in deals:
    data = format_deals(deal)
    add_deal(session, data)

def mapping_organization(organizations, session):
  for organization in organizations:
    data = format_organization(organization)
    add_organization(session, data)

def mapping_activities(activities, session):
  for activitie in activities:
    data = format_resume(activitie)
    add_resume(session, data)



