# -*- coding: utf-8 -*-


from flask import Flask, render_template, session, redirect, url_for,request
import telnetlib

app = Flask(__name__)


#==============================================================================
# 1. At least 1 letter between [a-z]
# 
# 2. At least 1 number between [0-9]
# 
# 3. At least 1 letter between [A-Z]
# 
# 4. At least 1 character from [$#@]
# 
# 5. Minimum length of transaction password: 6
# 
# 6. Maximum length of transaction password: 12
#==============================================================================

def validation(password):
    #1
    letter_type = []
    special = '$#@'
    for letter in password:
        if letter.isdigit():
            letter_type.append(0)
        elif letter.isupper():
            letter_type.append(1)
        elif letter.islower():
            letter_type.append(2)            
        elif letter in special:
            letter_type.append(3)
    if set(letter_type).issubset([0,1,2,3]) and (len(password)>=0) and (len(password)<=12):	
        return True
    else:
        return False
       
@app.route('/')
def hello():
    title = "Password Validator Application"
    return render_template('entry.html', the_title=title)


@app.route('/result',methods=['GET','POST'])
def do_search():
    title1 = "Authentication failure! Try again please."
    title2 = "Authentication passed! Login successfully!!!"
    userName = request.form.get('userName',None)
    password = request.form.get('password',None)
    result =  validation(password)
    HOST=r'10.10.10.3'
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(userName.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    a=tn.read_until(b"Username: ",timeout=0.5)
    if len(a)<2:
        return render_template('entry.html', the_title=title1)
    tn.write(b"terminal length 0\n")
    tn.write(b"show version\n\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    return render_template('result.html',the_title=title2,userName=userName,password=password,the_results=(result and True))

	
@app.route('/entry',methods=['GET','POST'])
def entry_page():
    title = "Password Validator Application"
    return render_template('entry.html', the_title=title)

if __name__ == '__main__':
    app.run()
