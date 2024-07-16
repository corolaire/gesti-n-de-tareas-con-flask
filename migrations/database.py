import sqlalchemy as db
import os
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.pool import StaticPool
if os.environt['stage']=='local':
    engine=db.create_engine('postgresql'://postgres:
                            root@localhost:5432/gestiontareas,echo=True)
else:
    engine=db.create_engine('postgre://'+':'.join([os.environ['rds_user']os.environ['ras_pass']])+'localhost:5432')
db_session:scoped_session(sessionmaker(engine))