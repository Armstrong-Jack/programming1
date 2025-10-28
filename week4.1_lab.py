
def celcius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
#takes an agument called celsious and convertisit to farenhiet and then returns the value

c_temp = 25
f_temp = celcius_to_fahrenheit(c_temp)
print(f"{c_temp} degrees Celsius is equal to {f_temp} degrees Fahrenheit.")