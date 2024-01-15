from processing.pesist_data import add_address, add_contact, add_deal, add_organization, add_resume, add_address_organization_rl, add_contact_organization_rl, add_deals_organization_rl
from processing.format import format_address, format_organization, format_deals, format_resume, format_organization_address_rl, format_organization_contact_rl, format_organization_deals_rl
from processing.requests_datas import request_contact_name
from tables.entity import Deals, Organization

def mapping_organization(organizations, session):
  for organization in organizations:
    data = format_organization(organization)

    # Data contact
    contacts = data['contacts']
    del data['contacts']
    list_contact_pesist = []
    for contact in contacts:
      print(f"\n---------- Request Contact ----------\n")
      contact_response = request_contact_name(contact['name'])
      contact_persist = add_contact(session, contact_response)
      if contact_persist:
        contact_json = contact_persist.as_dict()
        list_contact_pesist.append(contact_json)
    
    # Data address
    address = data['custom_fields']
    del data['custom_fields']
    print(f"\n---------- Request Address ----------\n")
    format_company_address = format_address(address, data['date_create'], data['date_update'])
    adr = add_address(session, format_company_address)
    adr_json = None
    if(adr):
      adr_json = adr.as_dict()
    # Persist organization
    organization_pesist = add_organization(session, data)
    organization_json = None
    if organization_pesist:
      organization_json = organization_pesist.as_dict()
    # Persist relationship
    # Contact
    if(len(list_contact_pesist) > 0):
      for contact_json in list_contact_pesist:
        organization_contact_rl = format_organization_contact_rl(organization_json, contact_json)
        add_contact_organization_rl(session, organization_contact_rl)
    # address
    if(adr_json and organization_json):
      organization_address_rl = format_organization_address_rl(organization_json, adr_json)
      add_address_organization_rl(session, organization_address_rl)

def mapping_deal(deals, session):
  for deal in deals:
    data = format_deals(deal)
    organization = data['organization']
    del data['organization']
    deal_persist = add_deal(session, data)
    if deal_persist:
      deal_json = deal_persist.as_dict()
      if organization:
        organization_id = organization['id']
        print(f'\n--------- Relationship between deal with id: and organization with id:{organization_id} ---------')
        response = session.query(Organization).filter_by(organization_rd_id=organization['id']).first()
        if(response):
          deal_organization = format_organization_deals_rl(response.id, deal_json)
          add_deals_organization_rl(deal_organization)
        else:
          print(f'\n--------- Organization not found: {organization_id} ---------')

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



