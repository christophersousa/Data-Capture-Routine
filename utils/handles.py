from tables.entity import Contact, Organization
from sqlalchemy.orm.exc import NoResultFound

def handle_duplicate_contact(session, row):
    try:
        existing_contact = session.query(Contact).filter_by(contact_rd_id=row['contact_rd_id']).one()
        update_existing(session, existing_contact, row)
    except NoResultFound:
        print("No existing Contact found for unique field:", row['contact_rd_id'])

def handle_duplicate_organization(session, row):
    try:
        existing_contact = session.query(Organization).filter_by(organization_rd_id=row['organization_rd_id']).one()
        update_existing(session, existing_contact, row)
    except NoResultFound:
        print("No existing Organization found for unique field:", row['organization_rd_id'])


def update_existing(session, existing_contact, new_data):
    try:
        for key, value in new_data.items():
            setattr(existing_contact, key, value)
        session.commit()
    except Exception as e:
        print("Error updating:", e)
        session.rollback()