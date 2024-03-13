from sys import argv
script, msisdn, name, consumer_type, tariff = argv

print("the script name",script)
print("your primary contact", msisdn)
print("your firstname", name)
print("your market segment", consumer_type)
print("your mobile line category ", tariff)

email_address, sname = argv
prompt = '>'
print(f"Hi, {sname}, your preffered contact detail is {email_address}")
print("I would like to ask you a few question")
contacts = input("what is your email address? ")
print(f"Your email address is {contacts}")
country = input("where do you live?")
hobby = input("What is your hobby?")
print(f"""Hi {sname} thank you for you feedback glad hearing from you, confirm below details.\nYour email address is {contacts}, you live in {country}.\nAnd your hobby is {hobby}.""")