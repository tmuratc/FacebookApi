from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
import facebook_business.adobjects.user as fb_user
import time

###################################################################################
################################################################################### 

def extract_account_ids (acc_param) :
    user = fb_user.User(fbid='me') 
    return ['act_' + i['account_id'] for i in user.get_ad_accounts(params=acc_param)] 

###################################################################################
###################################################################################  

def extract_ad_ids (acc_id,ad_param) : 
    return [i['id'] for i in AdAccount(acc_id).get_ads(params=ad_param) ] 


###################################################################################
################################################################################### 
def single_request (ad_id, ins_param, ins_field) :
    print(f'requesting ad id : {ad_id}') 
    return Ad(ad_id).get_insights(params=ins_param,fields=ins_field)  
    
###################################################################################
################################################################################### 

def repetitive_request_2 (ad_id, ins_param, ins_field, fail_wait_time) : 
    try : 
        return single_request(ad_id, ins_param, ins_field) 
    except : 
        print(f'   request for {ad_id} is failed. wait {fail_wait_time} second to try again') 
        time.sleep(fail_wait_time) 
        repetitive_request (ad_id,ins_param, ins_field,fail_wait_time)      

###################################################################################
################################################################################### 

def repetitive_request (ad_id, ins_param, ins_field, trial_count=0) : 
    try : 
        trial_count += 1 
        return single_request(ad_id, ins_param, ins_field)            
    except : 
        print(f'Request for {ad_id} is failed. Next try after {2**trial_count} seconds' ) 
        time.sleep(2**trial_count) 
        repetitive_request_2 (ad_id, ins_param, ins_field, trial_count) 

###################################################################################
################################################################################### 


