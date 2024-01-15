from processing.pesist_data import add_address, add_contact, add_deal, add_organization, add_resume
from processing.format import format_address, format_organization, format_deals, format_resume
from processing.requests_datas import request_contact_name
from tables.entity import Deals

def mapping_deal(deals, session):
  for deal in deals:
    data = format_deals(deal)
    add_deal(session, data)

def mapping_organization(organizations, session):
  for organization in organizations:
    data = format_organization(organization)

    # Data contact
    contacts = data['contacts']
    del data['contacts']
    for contact in contacts:
      print(f"\n---------- Request Contact ----------\n")
      contact_response = request_contact_name(contact['name'])
      add_contact(session, contact_response)
    
    # Data address
    address = data['custom_fields']
    del data['custom_fields']
    print(f"\n---------- Request Address ----------\n")
    format_company_address = format_address(address, data['date_create'], data['date_update'])
    add_address(session, format_company_address)
    
    # Pesist organization
    add_organization(session, data)

def mapping_activities(activities, session):
  for activitie in activities:
    data = format_resume(activitie)

    # Relationship to 'Deal'
    deal_rd_id = data['deal_id']
    deal = session.query(Deals).filter_by(deal_rd_id=deal_rd_id).first()
    data['deal_id'] = None
    if deal:
        print(f'--- Relação com Deal com id: {deal.id} ---')
        data['deal_id'] = deal.id
    add_resume(session, data)



