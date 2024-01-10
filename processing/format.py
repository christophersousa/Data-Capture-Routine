from processing.data_transform import create_dataframe, transform_uuid
import uuid

def format_deals(response) -> list:
    id_transformer = transform_uuid(response['id'])
    obj = {
            'deal_rd_id': response['id'],
            'name': response['name'],
            'pipeline': ' ',
            'stage': ' ',
            'date_create': response['created_at'],
            'date_update': response['updated_at'],
            'rating_id': None,
        }
    data = create_dataframe([obj])
    first_row = data.iloc[0].to_dict()
    return first_row

def format_organization(response) -> list:
    obj=[{
        'organization_rd_id': response['id'],
        'name': response['name'] or " ",
        'date_create': response['created_at'],
        'date_update': response['updated_at'],
        'document': " ",
    }]
    data = create_dataframe(obj)
    first_row = data.iloc[0].to_dict()
    return first_row

def format_rating(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id': response['id'],
                'rank': response[''],
                'name': response['state'],
                'date_create': response['created_at'],
                'date_update': response['updated_at'],
            }
            result_list.append(obj)
    return result_list

def format_organizations(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id': response['id'],
                'organization_rd_id': response['name'],
                'name': response[''],
                'date_create': response['created_at'],
                'date_update': response['updated_at'],
                'document': response[''],
            }
            result_list.append(obj)
    return result_list

def format_address(responses) -> list:
    result_list = []
    if len(responses) > 0:
        for response in responses:
            obj={
                'id': response['id'],
                'cep': response['cep'],
                'state': response['state'],
                'state_code': response['state_code'],
                'lat': response['lat'],
                'lon': response['lon'],
                'date_create': response['created_at'],
                'date_update': response['updated_at'],
            }
            result_list.append(obj)
    return result_list

def format_resume(response) -> list:
    deal_id_transformer = transform_uuid(response['deal_id'])
    obj={
        'text': response['text'],
        'report': response['user_id'] or None,
        'date_create': response['date'],
        'date_update': response['date'],
        'deal_id': uuid.UUID(deal_id_transformer),
    }
    data = create_dataframe([obj])
    first_row = data.iloc[0].to_dict()
    return first_row
