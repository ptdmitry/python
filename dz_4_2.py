from requests import get

response = get('http://www.cbr.ru/scripts/XML_daily.asp').text


def currency_rates(code):
    content = response.split('<Valute ID=')
    for idx in content:
        if code.upper() in idx:
            if code.upper() == 'USD':
                code = (content[11].split('</Value>')[0][-7:]).replace(',', '.')
                return float(code)
        if code.upper() in idx:
            if code.upper() == 'EUR':
                code = (content[12].split('</Value>')[0][-7:]).replace(',', '.')
                return float(code)


print(currency_rates('EUR'), type(currency_rates('EUR')))
print(currency_rates('eur'), type(currency_rates('eur')))
print(currency_rates('USD'), type(currency_rates('USD')))
print(currency_rates('usd'), type(currency_rates('usd')))
print(currency_rates('GBP'))