from sqlalchemy.orm import declarative_base

Base = declarative_base()



from .user import User
from .device import Device
from .location import Location
from .hostage_content import HostageContent
from .explosive_content import ExplosiveContent