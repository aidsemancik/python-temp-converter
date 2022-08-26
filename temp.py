name = input("What's your name?")
print('Hello ', name, '!')

begin_temp = int(input('Beginning temperature?'))
begin_unit = input('In C or F?')

if begin_unit == 'C' or 'c' or 'celsius' or 'Celsius':
    end_temp = (begin_temp * 1.8) + 32
    print("Hey ", name, ", ", begin_temp, "°C", " in Farenheit is ", end_temp, "°F.")
elif begin_unit == 'F' or 'f' or 'farenheit' or 'Farenheit':
    end_temp = (begin_temp - 32) * .5556
    print("Hey ", name, ", ", begin_temp, "°F", " in Celsius is ", end_temp, "°C.")