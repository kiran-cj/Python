
def fuel_gauge():
    while True:
        fraction = input("Enter fraction: ")
        try:
            x = int(fraction.split('/')[0])
            y = int(fraction.split('/')[1])
            print(f'Fuel left: {int((round(x/y, 2))*100)}%')
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            print('Division by zero is not possible')

    