money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
number_of_month_without_debt = -1


while money_capital > 0:
    money_capital += salary - spend
    number_of_month_without_debt += 1
    spend *= increase + 1

print("Количество месяцев, которое можно протянуть без долгов:", number_of_month_without_debt)
