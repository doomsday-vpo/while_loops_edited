# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере
# дали ще успее да събере необходимата сума.
# Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход:
# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.
# Изход:
# Програмата трябва да приключи при следните случаи:
# •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o	"You can't save the money."
# o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# o	"You saved the money for {общ брой изминали дни} days."


needed_money = float(input())
current_money = float(input())

days_spending = 0
total_days = 0

while current_money < needed_money:
    action = input()
    amount = float(input())
    total_days += 1

    if action == "spend":
        current_money -= amount
        if current_money < 0:
            current_money = 0
        days_spending += 1
        if days_spending == 5:
            print("You can't save the money.")
            print(total_days)
            break
    elif action == "save":
        current_money += amount
        days_spending = 0

if current_money >= needed_money:
    print(f"You saved the money for {total_days} days.")
