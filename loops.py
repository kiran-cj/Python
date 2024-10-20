
def test1():
    print("meow\n"*3, end='')

def snake_case_converter():
    name = list(input("Enter name in camel case: "))
    print(name)
    for idx, i in enumerate(name):
        name[idx] = f'_{i.lower()}' if i.isupper() else i
    print(f"New name: {''.join(name)}")

def coke_machine():
    money = 0
    denominations = [5,10,25]
    while money < 50:
        print(f"Due: {50-money}")
        coin = int(input("Insert coin: "))
        money += coin if coin in denominations else money
    print(f"Balance amount: {money-50}")

def genz_iser():
    word = list(input("Enter word to be genz_ised: "))
    vowels = ['a','e','i','o','u']
    genzed_word = []
    for i in word:
        genzed_word.append(i) if i.lower() not in vowels else None
    print(f"Genzed word: {''.join(genzed_word)}")

genz_iser()


