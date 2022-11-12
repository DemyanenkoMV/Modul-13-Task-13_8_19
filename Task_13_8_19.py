amt_tickets = int(input('Введите количество билетов: ')) # просим ввести количество билетов на мероприятие
member_ages = []    # Создаем список, в котором будет храниться возраст участников

for i in range(0, amt_tickets):
    input_age = int(input(f'Введите возраст участника №{i + 1}:\n'))  # для каждого билета запросить возраст
    member_ages.append(input_age)               # Заполняем member_ages числами, которые вводит пользователь

    def prise(age):                               # исходя из возраста выбираем стоимость билета
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

full_prise = sum(map(prise, member_ages))          # считаем стоимость всех билетов

if amt_tickets > 3:
    full_prise = int(full_prise * 0.9)            # проводим скидку если количество билетов больше 3

print('Итоговая стоимость:', full_prise, 'руб.')





