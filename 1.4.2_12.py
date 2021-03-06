# 12. Інформація про групу туристів складається з прізвища, віку, статі та кольору очей. Розробити програму, яка
# після введення даних анкет виводить на екран кількість чоловіків і жінок:
# • заданого віку;
# • заданого кольору очей;
# • при необхідності (на вимогу) прізвища таких туристів, впорядкованих за алфавітом.

while True:
    surnames_l = ["Sukhanov", "Ivanova"] #Дані прізвищ людей у анкеті.
    old_l = [18, 44] #Їх вік.
    eyes_l = ['blue', 'brown'] #Колір очей.
    stat_l = ['male', 'woman'] #Стать.

    old = dict(zip(surnames_l, old_l)) #За допомогою словника поєднаємо\
    #прізвища з характеристиками. Це для того, щоб по заданому віку, \
    #кольору очей, статі визначити прізвище людини.
    eyes = dict(zip(surnames_l, eyes_l))
    stat = dict(zip(surnames_l, stat_l))#Стать потрібна для лічильника:\
    #кількість чоловіків/жінок.
  
    selected_eyes = input('Введіть потрібний колір очей: ')
    while True:
        try: #Перевірка, чи користувач дійсно ввів цифру.
            selected_old = int(input('Введіть потрібний вік: '))
            break
        except ValueError:
            print('Введіть цифру!')
    count_of_men = 0 #лічильники
    count_of_women = 0
    surnames_of_selected = [] #У разі виявлення співпадінь у анкеті\
    #та тим, що ввів користувач, ми додамо у цей список потрібні дані.

    for i in eyes:
        #Перевірка, чи співпадають дані у анкеті з тими, що\
        #ввів користувач.
        if eyes[i] == selected_eyes and old[i] == selected_old:
            #Додамо ці дані у прізвища та у кінці виведемо.
            surnames_of_selected.append(i)
            if stat[i] == 'male': #Перевірка на стать.
                count_of_men += 1
            else:
                count_of_women += 1
    print('кількість таких чоловіків: ', count_of_men)
    print('кількість таких жінок: ', count_of_women)

    #Якщо користувач захоче побачити прізвище людини з такими\
    #характеристиками, то натисне "yes".
    yes = input('введіть "yes", щоб побачти їх прізвиська: ')
    if yes == 'yes':
        print('Їх прізвиська: ' )
        for s in surnames_of_selected:
            print(s)

    #Чи бажаєте заново запустити програму?
    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
