user_= input ("Enter your user ID (press 1 to create account):")
if "1"  in user_id:
    email= ("Enter your user ID:")
    
    with open ("password\\email.txt,""w")as f:
        store_email=f.write(email)