from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

from app.db.database_psql import session_maker
from app.db.models import User, HostageContent


def get_user_data_by_email(email):
    try:
        with session_maker() as session:
            user = session.query(User).filter_by(email=email). \
                options(
                    joinedload(User.device),
                    joinedload(User.location),
                    joinedload(User.explosive_content),
                    joinedload(User.hostage_content)
                ).one()
            return user

    except SQLAlchemyError as e:
        print(f"Error inserting user: {e}")
        return None




