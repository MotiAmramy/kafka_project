from sqlalchemy.exc import SQLAlchemyError
from app.db.database_psql import session_maker
from app.db.models import ExplosiveContent, HostageContent, Device, User, Location



def insert_user(data):
    try:
        with session_maker() as session:
            user = User(
                email=data["email"],
                ip_address=data["ip_address"],
                username=data["username"],
                created_at=data["created_at"]
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            print(user)
            return user
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting user: {e}")
        return None

def insert_location(data, user_id):
    try:
        with session_maker() as session:
            location_data = data["location"]
            location = Location(
                latitude=str(location_data["latitude"]),
                longitude=str(location_data["longitude"]),
                city=location_data["city"],
                country=location_data["country"],
                user_id=user_id
            )
            session.add(location)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting location for user {user_id}: {e}")

def insert_device(data, user_id):
    try:
        with session_maker() as session:
            device_data = data["device_info"]
            device = Device(
                device_id=device_data["device_id"],
                browser=device_data["browser"],
                os=device_data["os"],
                user_id=user_id
            )
            session.add(device)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting device for user {user_id}: {e}")

def insert_explosive_content(sentence, user_id):
    try:
        with session_maker() as session:
            explosive_content = ExplosiveContent(
                sentence=sentence,
                user_id=user_id
            )
            session.add(explosive_content)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting explosive content for user {user_id}: {e}")

def insert_hostage_content(sentence, user_id):
    try:
        with session_maker() as session:
            hostage_content = HostageContent(
                sentence=sentence,
                user_id=user_id
            )
            session.add(hostage_content)
            session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error inserting hostage content for user {user_id}: {e}")

def process_sentences(sentences, user_id):
        try:
            if "explosive" in sentences[0].lower() or 'explos' in sentences[0].lower():
               for sentence in sentences:
                    insert_explosive_content(sentence, user_id)
            elif "hostage" in sentences[0].lower():
                for sentence in sentences:
                    insert_hostage_content(sentence, user_id)
        except Exception as e:
            print(f"Error processing sentence for user {user_id}: {e}")