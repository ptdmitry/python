from requests import get
import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp').text


def currency_rates(code):
    content = response.split('<Valute ID=')
    year = int(content[0].split('Date=')[1][7:11])
    month = int(content[0].split('Date=')[1][4:6])
    day = int(content[0].split('Date=')[1][1:3])
    date_now = datetime.date(year, month, day)
    for idx in content:
        if code.upper() in idx:
            if code.upper() == 'USD':
                code = (content[11].split('</Value>')[0][-7:]).replace(',', '.')
                print(float(code), date_now)
        if code.upper() in idx:
            if code.upper() == 'EUR':
                code = (content[12].split('</Value>')[0][-7:]).replace(',', '.')
                print(float(code), date_now)
            else:
                print(None)

if __name__ == '__main__':
    currency_rates('EUR')
    currency_rates('USD')
    currency_rates('GBP')
else:
    print("I'm a module!")