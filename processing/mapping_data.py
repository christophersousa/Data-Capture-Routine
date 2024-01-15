from processing.pesist_data import add_address, add_contact, add_deal, add_organization, add_resume, add_address_organization_rl
from processing.format import format_address, format_organization, format_deals, format_resume, format_object_dataframe
from processing.requests_datas import request_contact_name
from tables.entity import Deals, OrganizationAddressRl

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
    obj_organization_address_rl = {
      "address_id": adr_json['id'],
      "organization_id": organization_json['id'],
      "is_active": True,
      "date_create": organization_json['date_create'],
      "date_update": organization_json['date_update']
    }
    organization_address_rl = format_object_dataframe(obj_organization_address_rl)
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



