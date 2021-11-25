prices = [57.8, 46.51, 97, 101.5, 54, 98.15, 34.85, 100, 5.44, 78.09, 99.9]

"""A"""
for rub in prices:
    if 0 < rub < 10:
        kop = str(rub)[2:]
    elif 100 < rub < 1000:
        kop = str(rub)[4:]
    else:
        kop = str(rub)[3:]
    print(f'"{int(rub)} руб {str(kop):02} коп"')

"""B"""
print(prices, id(prices))
prices.sort()
print(prices, id(prices))

"""C"""
rev_prices = sorted(prices, reverse=True)
print(rev_prices)

"""D"""
print(sorted((sorted(prices, reverse=True))[:5]))