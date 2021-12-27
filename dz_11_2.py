class Division:
    def __init__(self, n_1, n_2):
        self.n_1 = n_1
        self.n_2 = n_2

    @staticmethod
    def zero_div(n_1, n_2):
        try:
            return n_1 / n_2
        except:
            return f"Делить на ноль нельзя"


print(Division.zero_div(12, 2))
print(Division.zero_div(12, 0))





# a = Division(4, 2)
# # print(a)
#
# try:
#     a = Division(4, 0)
#     # print(a)
# except ZeroEx as err:
#     print(f"Делить на ноль нельзя")
#     # try:  # Обработка исключения, недостаточно денег у покупателя
#     #     customer_1.buy(stock.cars[1])  # Покупка авто - достаём из склада stock авто - хранится только 1
#     # except NotEnMoneyEx as err:
#     #     print(f"Need more {err.needle - err.current}")  # Сколько ещё нужно денег