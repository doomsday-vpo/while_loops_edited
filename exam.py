# Напишете програма, в която Марин решава задачи от изпити,
# докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка.
# Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход:
# •	На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6]
# Изход:
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
# o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.



bad_grades_limit = int(input())
bad_grades_count = 0
total_score = 0
problem_count = 0
last_problem = ""

while True:
    problem_name = input()

    if problem_name == "Enough":
        average_score = total_score / problem_count
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problem_count}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())
    total_score += grade
    problem_count += 1
    last_problem = problem_name

    if grade <= 4:
        bad_grades_count += 1
        if bad_grades_count >= bad_grades_limit:
            print(f"You need a break, {bad_grades_count} poor grades.")
            break

