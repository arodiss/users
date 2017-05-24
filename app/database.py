from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+mysqldb://root:root@db:3306/users', pool_recycle=3600)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
    prefill_db_if_necessary()


def prefill_db_if_necessary():
    from models.user import User
    if db_session.query(User).count() == 0:
        admin = User("admin", "admin")
        db_session.add(admin)
        db_session.commit()