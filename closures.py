def make_repeater_of(n):
    def repeater(string):
        assert type(string)==str,"solo puedes utilizar cadenas"
        return string * n
    return repeater

def make_division_of(divisor:int):
    def dividendo(divi:int):
        assert type(divi)==int or type(divisor)==int, "solo puede ingresar numeros"
        return divi/divisor
    return dividendo

def main():
    repeat_5 = make_repeater_of(5)    
    print(repeat_5("hola, "))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi, "))

    division_by_3= make_division_of(5)
    print(division_by_3(100))


if __name__=='__main__':
    main()