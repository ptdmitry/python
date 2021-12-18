import re

email_address = ['someone@geekbrains.ru', 'greeply@gmail.com']


def email_parse(email_address):
    RE_MAIL = re.compile(r'(?P<username>\b\w+)@(?P<domain>\b\w+\.\b\w+)', re.IGNORECASE)
    print(RE_MAIL.match(email_address).groupdict())


for i in email_address:
    email_parse(i)