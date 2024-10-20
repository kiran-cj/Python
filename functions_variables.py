def test1():
    a = input("Niggesh? ")
    print(a.title())
    print(input("Anti-Niggesh? "))

def test2():
    n=100000.5270935
    print(f'{10000:,}')
    print(round(n,3))

def test3():
    print((input("Input something: ")).lower())
    print((input("Input Sentence: ")).replace(' ', '...'))

def convert_emoticon(sentence):
    return sentence.replace(':)', '🙂').replace(':(', '🙁')

def test4():
    sentence = convert_emoticon(input("Enter the sentence: "))
    print(f"Converted sentence: \n\t{sentence}")

def test5():
    c = 300000000
    try: mass = int(input("Enter mass of object: "))
    except:
        print("Enter numerical value ... exiting")
        quit()
    print(f"Energy = {(mass*(c**2)):,} Joules")
