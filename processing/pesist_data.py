from sqlite3 import IntegrityError
from tables.entity import Rating, Deals, Organization, Resume, Contact, Address, OrganizationAddressRl, OrganizationContactRl, OrganizationDealsRl
from utils.handles import handle_duplicate_contact, handle_duplicate_organization

def add_rating(session, row):
    try:
        rating = Rating(**row)
        session.add(rating)
        session.commit()
    except IntegrityError as e:
        print("Error adding rating:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()

def add_deal(session, row):
    try:
        deals = Deals(**row)
        session.add(deals)
        session.commit()
        return deals
    except IntegrityError as e:
        print("Error adding deals:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()

def add_organization(session, row):
    try:
        organization = Organization(**row)
        session.add(organization)
        session.commit()
        return organization
    except IntegrityError as e:
        print("Error adding organization:", e)
        session.rollback()
    except Exception as e:
        session.rollback()
        if "unique constraint" in str(e.orig):
           handle_duplicate_organization(session, row)
        else:
            print("Error adding Organization:", e)
            session.rollback()
        print("Other error:", e)
        session.rollback()

def add_resume(session, row):
    try:
        resume = Resume(**row)
        session.add(resume)
        session.commit()
    except IntegrityError as e:
        print("Error adding resume:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()

def add_contact(session, row):
    contact = Contact(**row)
    try:
        session.add(contact)
        session.commit()
        return contact
    except IntegrityError as e:
        print("Error adding contact:", e)
        session.rollback()
    except Exception as e:
        session.rollback()
        if "unique constraint" in str(e.orig):
           handle_duplicate_contact(session, row)
        else:
            print("Error adding contact:", e)
            session.rollback()
        print("Other error:", e)
        session.rollback()

def add_address(session, row):
    try:
        address = Address(**row)
        session.add(address)
        session.commit()
        return address
    except IntegrityError as e:
        print("Error adding address:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()

#  Persist Relations
def add_address_organization_rl(session, row):
    try:
        organizationAddressRl = OrganizationAddressRl(**row)
        session.add(organizationAddressRl)
        session.commit()
    except IntegrityError as e:
        print("Error adding organizationAddressRl:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()

def add_contact_organization_rl(session, row):
    try:
        organizationContactRl = OrganizationContactRl(**row)
        session.add(organizationContactRl)
        session.commit()
    except IntegrityError as e:
        print("Error adding organizationContactRl:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()

def add_deals_organization_rl(session, row):
    try:
        organizationDealstRl = OrganizationDealsRl(**row)
        session.add(organizationDealstRl)
        session.commit()
    except IntegrityError as e:
        print("Error adding organizationDealstRl:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()