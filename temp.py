name = input("What's your name?")
print('Hello ', name, '!')

begin_temp = input('What is your beginning temperature?')

while not begin_temp.isdigit():
    begin_temp = input('Please enter a number.')

begin_unit = input('In C or F?')

while (begin_unit != 'C') and (begin_unit != 'F'):
    begin_unit = input('Please enter either C or F.')

if begin_unit == ('C'):
    end_temp = (int(begin_temp) * 1.8) + 32
    print("Hey " + name + ", " + str(begin_temp) + "°C in Farenheit is " +  str(end_temp) + "°F.")
elif begin_unit == ('F'):
    end_temp = (int(begin_temp) - 32) * .5556
    print("Hey " + name + ", " + str(begin_temp) + "°F in Celsius is " + str(end_temp) + "°C.")

