#Erhmprez
#Converting Celsius to Fahrenheit
try:
    temperature_celsius = int(input('Enter temperature in Celsius: '))
    temperature_fahrenheit = (1.8 * temperature_celsius) + 32

    print('The temperature in Fahrenheit is: ', temperature_fahrenheit)
except ValueError:
    print('Invalid value')