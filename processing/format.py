from processing.data_transform import create_dataframe, transform_uuid
from utils.list_state import list_state_code
from utils.stages import getPipeline

# List state code
list_state_code_uppercase = {state.upper(): details for state, details in list_state_code.items()}

def format_deals(response) -> list:
    stage = response['deal_stage']['id'] or None
    pipeline = getPipeline(stage)
    organization =  None
    if response.get('organization'):
        organization = response['organization']
    user =  None
    if response.get('user'):
        user = response['user']
    obj = {
            'deal_rd_id': response['id'],
            'name': response['name'],
            'pipeline': pipeline,
            'stage': stage,
            'closed_at': response['closed_at'] or None,
            'organization': organization,
            'user': user,
            'date_create': response['created_at'],
            'date_update': response['updated_at'],
            'visit_id': None
        }
    return format_object_dataframe(obj)

def format_organization(response) -> list:
    user =  None
    if response.get('user'):
        user = response['user']
    obj={
        'organization_rd_id': response['id'],
        'name': response['name'] or None,
        'date_create': response['created_at'],
        'date_update': response['updated_at'],
        'document': None,
        'user': user,
        'contacts': response['contacts'],
        'custom_fields': response['custom_fields'],
    }
    for data in response['custom_fields']:
        if(data['custom_field']['label'] == 'CNPJ/CPF'):
            obj['document'] = data['value']
    return format_object_dataframe(obj)

# def format_rating(responses) -> list:
#     result_list = []
#     if len(responses) > 0:
#         for response in responses:
#             obj={
#                 'id': response['id'],
#                 'rank': response[''],
#                 'name': response['state'],
#                 'date_create': response['created_at'],
#                 'date_update': response['updated_at'],
#             }
#             result_list.append(obj)
#     return result_list

def format_contact(response) -> list:
    # Handle edge cases where phones or emails might be empty
    phones = response.get('phones', [])
    emails = response.get('emails', [])

    # Get the first phone and email (if available)
    phone = phones[0]['phone'] if phones else None
    email = emails[0]['email'] if emails else None
    obj={
        'contact_rd_id': response['id'],
        'name': response['name'] or None,
        'phone': phone,
        'email': email,
        'date_create': response['created_at'],
        'date_update': response['updated_at']
    }
    return format_object_dataframe(obj)

def format_address(responses, date_created, date_updated) -> list:
    obj={
        'cep': None,
        'state': None,
        'state_code': None,
        'lat': None,
        'lon': None,
        'date_create': date_created,
        'date_update': date_updated
    }
    if len(responses) > 0:
        for response in responses:
            if(response['custom_field']['label'] == 'Estado'):
                obj['state'] = response['value']
                state_code = list_state_code_uppercase.get(str(response['value']).upper())
                code =  state_code['sigla'] if state_code else None
                obj['state_code'] = code
            elif(response['custom_field']['label'] == 'CEP'):
                obj['cep'] = response['value']
    return format_object_dataframe(obj)

def format_resume(response) -> list:
    obj={
        'text': response['text'],
        'reporter': response['user_id'] or None,
        'date_create': response['date'],
        'date_update': response['date'],
        'deal_id': response['deal_id'],
    }
    return format_object_dataframe(obj)

def format_users(response) -> list:
    obj={
        'user_rd_id': response['id'] or None,
        'name': response['name'] or None,
        'email': response['email'] or None,
        'token': None,
        'date_create': response['created_at'],
        'date_update': response['updated_at'],
        'is_active': response['active'],
        'permission': 'user',
    }
    return format_object_dataframe(obj)

def format_organization_contact_rl(organization, contact):
    obj_organization_contact_rl = {
      "contact_id": contact['id'],
      "organization_id": organization['id'],
      "is_active": True,
      "date_create": organization['date_create'],
      "date_update": organization['date_update']
    }
    return format_object_dataframe(obj_organization_contact_rl)

def format_organization_address_rl(organization, address):
    obj_organization_address_rl = {
      "address_id": address['id'],
      "organization_id": organization['id'],
      "is_active": True,
      "date_create": organization['date_create'],
      "date_update": organization['date_update']
    }
    return format_object_dataframe(obj_organization_address_rl)

def format_organization_deals_rl(organization_id, deals):
    obj_organization_address_rl = {
      "deal_id": deals['id'],
      "organization_id": organization_id,
      "is_active": True,
      "date_create": deals['date_create'],
      "date_update": deals['date_update']
    }
    return format_object_dataframe(obj_organization_address_rl)

def format_user_deals_rl(user_id, deals):
    obj= {
      "deal_id": deals['id'],
      "user_id": user_id,
      "is_active": True,
      "date_create": deals['date_create'],
      "date_update": deals['date_update']
    }
    return format_object_dataframe(obj)

def format_user_address_rl(user_id, address):
    obj= {
      "address_id": address['id'],
      "user_id": user_id,
      "is_active": True,
      "date_create": address['date_create'],
      "date_update": address['date_update']
    }
    return format_object_dataframe(obj)

def format_object_dataframe(obj):
    data = create_dataframe([obj])
    first_row = data.iloc[0].to_dict()
    return first_row