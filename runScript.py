import sys, os, config,db, functions as funcs 
from facebook_business.api import FacebookAdsApi 
from dotenv import load_dotenv  

############################################################################
############################################################################  
#parameters that will be used while requesting from Facebook Api 
acc_param = {  'time_range' : {  'since': sys.argv[1], 
                            'until': sys.argv[2] } }

ad_param = {  'time_range' : {  'since': sys.argv[1] , 
                            'until': sys.argv[2] } , 
               'filtering' : [ { 'field' : 'spend' , 
                                  'operator' : 'GREATER_THAN' , 
                                  'value' : 0 
                                  } ]   } 

ins_param = {  'time_range' : {  'since': sys.argv[1] , 
                            'until': sys.argv[2]  } ,          
         'time_increment' :  1 }  
############################################################################
############################################################################  


############################################################################
############################################################################  
# connecting api by using .env variables
load_dotenv()
print('environment variables extracted...')
FacebookAdsApi.init(access_token=os.getenv("ACCESS_TOKEN"),api_version=os.getenv("API_VERSION"))
print('connected to facebook api...') 


############################################################################
############################################################################ 
# extracting account id's 
# creating dictionary use account id's as keys and  ad id's as values  

account_ids = funcs.extract_account_ids(acc_param)
print('account ids extracted...')

ad_ids = {acc_id: funcs.extract_ad_ids(acc_id,ad_param) for acc_id in account_ids }  
#above line works slow 
print('ad ids matched with account ids...')


for key,value in ad_ids.copy().items() : 
    if len(value) == 0 : ad_ids.pop(key) 


############################################################################
############################################################################ 
#requesting data from api by iterating over ad id's 
#adding data to db

for acc_id in ad_ids.keys(): 
    
    for ad_id in ad_ids[acc_id]:    
        data = funcs.repetitive_request(ad_id, ins_param, config.field)  
        print(ad_id, ':data extracted...') 
        
        for index in range(len(data)) : 
            day = data[index]['date_start']  
            row = db.AdData(acc_id,ad_id,day,dict(data[index]))
            db.session.add(row) 
            db.session.commit() 
            print(ad_id, ':data is added to db...') 


