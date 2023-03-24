import os 
from dotenv import load_dotenv 
load_dotenv()
from sqlalchemy import create_engine

############################################################################
############################################################################ 
#database connection string 
conn_str = "postgresql://{}:{}@{}:{}/{}".format(os.getenv("PG_USER"), 
                                                os.getenv("PG_PWD"),
                                                os.getenv("PG_HOST"), 
                                                os.getenv("PG_PORT"), 
                                                os.getenv("PG_DB"))
#creating sql engine and connecting to db 
engine_pg = create_engine(conn_str, echo=True)                                                     
conn_pgsql_alc = engine_pg.connect()  
print("connected to database...") 
############################################################################
############################################################################ 


############################################################################
############################################################################ 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, String, Text, JSON, Date

#creating base to map obejct data and table 
Base = declarative_base() 

#creating table objects under a class
class AdData(Base) : 
    __tablename__ = "Ad_Data" 
    
    account_id = Column("account_id", String) 
    ad_id = Column("ad_id", String, primary_key=True) 
    day = Column("day", Date, primary_key=True) 
    data = Column("data", JSON)
      
    
    def __init__(self,accoount_id,ad_id,day,data) : 
        self.account_id = accoount_id 
        self.ad_id = ad_id 
        self.day = day 
        self.data = data 
print('Base and table object is created...')       
############################################################################
############################################################################ 

############################################################################
############################################################################  
from sqlalchemy.orm import sessionmaker  
Base.metadata.create_all(bind=engine_pg)
Session = sessionmaker(bind=engine_pg)
session = Session() 

print('session started...')