from sys import argv


def add_sale(cost):
    with open('bakery.csv', 'a', encoding='utf-8-sig') as f:
        f.write(f"{float(cost):010.2f}\n")
    return cost


if __name__ == '__main__':
    cost = argv[1]
    add_sale(cost)