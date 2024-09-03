first = int(input("Введите первое:"))
second = int(input("Введите второе:"))
third = int(input("Введите третье:"))
if first == second  and first == third:
    print('Если равны, то вывести значение:', 3)
elif first == second or second == third or first == third:
    print('Если равны 2 из 3, то вывести:', 2)
if first != second and second != third and first != third:
    print('Если равных нет,то вывести:', 0)