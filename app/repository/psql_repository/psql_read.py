from collections import Counter
from returns.maybe import Maybe
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from toolz import pipe, partial
from app.db.database_psql import session_maker
from app.db.models import User, HostageContent, ExplosiveContent



def get_user_data_by_email(email: str) -> Maybe[User]:
    try:
        with session_maker() as session:
            user = session.query(User).filter_by(email=email). \
                options(
                    joinedload(User.device),
                    joinedload(User.location),
                    joinedload(User.explosive_content),
                    joinedload(User.hostage_content)
                ).one()
            return Maybe.from_optional(user)

    except SQLAlchemyError as e:
        print(f"Error inserting user: {e}")






def get_all_sentences_hostage():
    try:
        with session_maker() as session:
            list_of_sentences_hostage = session.query(HostageContent).all()
            all_sentences = pipe(
                list_of_sentences_hostage,
                partial(map, lambda s: s.sentence),
                list
            )
            return all_sentences

    except SQLAlchemyError as e:
        print(f"Error inserting user: {e}")
        return None


def get_all_sentences_explosive():
    try:
        with session_maker() as session:
            list_of_sentences_explosive = session.query(ExplosiveContent).all()
            all_sentences = pipe(
                list_of_sentences_explosive,
                partial(map, lambda s: s.sentence),
                list
            )
            return all_sentences

    except SQLAlchemyError as e:
        print(f"Error inserting user: {e}")
        return None




def find_most_common_word() -> Maybe[str]:
    sentences_hostage = get_all_sentences_hostage()
    sentences_explosive = get_all_sentences_explosive()
    all_sentences = pipe(
        sentences_explosive + sentences_hostage,
        list,
        "".join,
        lambda s: s.replace(".", " "),
        lambda s: s.split(),
        lambda l: Counter(l).most_common(),
        lambda l: l[0][0]
    )
    return Maybe.from_optional(all_sentences)