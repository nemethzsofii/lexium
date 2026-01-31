from db import db
from models import Case, CaseWork, Client, ClientPerson, ClientCompany, User
from sqlalchemy.exc import SQLAlchemyError
from models import CaseWork
from sqlalchemy.orm import joinedload
from datetime import date as DateType

# --------------------
# Generic helpers
# --------------------

def commit_session():
    try:
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e


def add_instance(instance):
    try:
        db.session.add(instance)
        commit_session()
        return instance
    except SQLAlchemyError as e:
        raise e


def delete_instance(instance):
    try:
        db.session.delete(instance)
        commit_session()
        return True
    except SQLAlchemyError as e:
        raise e


def get_all_users():
    return User.query.all()
# --------------------
# Case utilities
# --------------------

def create_case(name, client_id, description=None):
    case = Case.create( 
        name=name,
        client_id=client_id,
        description=description
    )
    return case


def get_case_by_id(case_id):
    return Case.query.get(case_id)


def get_all_cases():
    return Case.query.all()


def get_cases_by_client(client_id):
    return Case.query.filter_by(client_id=client_id).all()


def update_case(case_id, **kwargs):
    case = get_case_by_id(case_id)
    if not case:
        return None

    for key, value in kwargs.items():
        if hasattr(case, key):
            setattr(case, key, value)

    commit_session()
    return case

from models import OutsourceCompany

def get_all_outsource_companies():
    """
    Returns a list of all outsource companies.
    """
    try:
        return OutsourceCompany.query.order_by(OutsourceCompany.name).all()
    except Exception as e:
        print(f"Error fetching outsource companies: {e}")
        return []
    
def delete_case(case_id):
    case = get_case_by_id(case_id)
    if not case:
        return False
    return delete_instance(case)


# --------------------
# CaseWork utilities
# --------------------

def create_case_work(user_id, case_id, date, start_time, end_time):
    case_work = CaseWork(
        user_id=user_id,
        case_id=case_id,
        date=date,
        start_time=start_time,
        end_time=end_time
    )
    return add_instance(case_work)

def get_case_works_by_date(day: DateType):
    """
    Returns all CaseWork entries for a specific date.
    Includes user and case relationships for display.
    """
    return (
        CaseWork.query
        .options(
            joinedload(CaseWork.user),  # load user to avoid lazy loading
            joinedload(CaseWork.case)   # load case
        )
        .filter(CaseWork.date == day)
        .order_by(CaseWork.start_time)
        .all()
    )

def get_all_case_works():
    return CaseWork.query.all()

def get_case_work_by_id(case_work_id):
    return CaseWork.query.get(case_work_id)


def get_case_work_for_case(case_id):
    return CaseWork.query.filter_by(case_id=case_id).all()


def get_case_work_for_user(user_id):
    return CaseWork.query.filter_by(user_id=user_id).all()


def delete_case_work(case_work_id):
    case_work = get_case_work_by_id(case_work_id)
    if not case_work:
        return False
    return delete_instance(case_work)


# --------------------
# Client utilities
# --------------------

def create_client_person(client_code, name, tax_number=None, birth_date=None, address=None):
    client = ClientPerson(
        client_code=client_code,
        name=name,
        tax_number=tax_number,
        birth_date=birth_date,
        address=address
    )
    return add_instance(client)


def create_client_company(client_code, name, tax_number=None, headquarters=None):
    client = ClientCompany(
        client_code=client_code,
        name=name,
        tax_number=tax_number,
        headquarters=headquarters
    )
    return add_instance(client)


def get_client_by_id(client_id):
    return Client.query.get(client_id)


def get_client_by_code(client_code):
    return Client.query.filter_by(client_code=client_code).first()


def get_all_clients():
    return Client.query.all()


def delete_client(client_id):
    client = get_client_by_id(client_id)
    if not client:
        return False
    return delete_instance(client)
        