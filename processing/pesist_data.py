from sqlite3 import IntegrityError
from tables.entity import Rating, Deals, Organization, Resume, Contact, Address
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
    try:
        contact = Contact(**row)
        session.add(contact)
        session.commit()
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
    except IntegrityError as e:
        print("Error adding address:", e)
        session.rollback()
    except Exception as e:
        print("Other error:", e)
        session.rollback()