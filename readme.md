# Ads in Facebook are structured in hierarchies referred to as 'levels:' 
    -Facebook Business Account
    -Ad Account
    -Campaigns  
    -Ad sets 
    -Ads 
**All entities have one to many relation from top to bottom.** 

**To get data "Insights API" will be used.** 

# Prerequisites to make Insights API call : 
    1. Creating an app under Facebook Business Account.
    2. Set permissions for app to read campaign data. 
    3. Create an access token in app.  

# To run script variables in the .env file must be set :  
    1. ACCESS_TOKEN 
    2. API_VERSION 
    3. PG_HOST
    4. PG_DB 
    5. PG_USER
    6. PG_PWD
    7. PG_PORT


# While running runScript.py file 2 arguments must be assigned :
    1. Start Date : YYYY-AA-DD 
    2. End Date   : YYYY-AA-DD 




        
