from processing.pesist_data import add_address, add_contact, add_deal, add_organization, add_resume, add_address_organization_rl, add_contact_organization_rl
from processing.format import format_address, format_organization, format_deals, format_resume, format_organization_address_rl, format_organization_contact_rl
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
    list_contact_pesist = []
    for contact in contacts:
      print(f"\n---------- Request Contact ----------\n")
      contact_response = request_contact_name(contact['name'])
      contact_persist = add_contact(session, contact_response)
      contact_json = contact_persist.as_dict()
      list_contact_pesist.append(contact_json)
    
    # Data address
    address = data['custom_fields']
    del data['custom_fields']
    print(f"\n---------- Request Address ----------\n")
    format_company_address = format_address(address, data['date_create'], data['date_update'])
    adr = add_address(session, format_company_address)
    adr_json = adr.as_dict()
    # Persist organization
    organization_pesist = add_organization(session, data)
    organization_json = organization_pesist.as_dict()
    # Persist relationship
    # Contact
    for contact_json in list_contact_pesist:
      organization_contact_rl = format_organization_contact_rl(organization_json, contact_json)
      add_contact_organization_rl(session, organization_contact_rl)
    # address
    organization_address_rl = format_organization_address_rl(organization_json, adr_json)
    add_address_organization_rl(session, organization_address_rl)


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



