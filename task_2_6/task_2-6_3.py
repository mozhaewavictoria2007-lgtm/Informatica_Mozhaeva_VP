don = int(input("Введите группу крови донора: "))
rep = int(input("Введите группу крови реципиента: "))
if don == 1: 
            print("Можно")
elif don == 2:
        if rep == 2 or rep == 4: 
             print("Можно")
        else:
             print("Нельзя")
elif don == 3:
        if rep == 3 or rep == 4: 
            print("Можно")
        else:
            print("Нельзя")
elif don == 4:
        if rep == 4: 
            print("Можно")
        else:
            print("Нельзя")
