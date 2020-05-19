import pyinputplus as pyip
lookup = {
    'units':{
        '0': '',
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX'
    },
    'tens':{
        '0': '',
        '1': 'X',
        '2': 'XX',
        '3': 'XXX',
        '4': 'XL',
        '5': 'L',
        '6': 'LX',
        '7': 'LXX',
        '8': 'LXXX',
        '9': 'XC'
    },
    'hundreds':{
        '0': '',
        '1': 'C',
        '2': 'CC',
        '3': 'CCC',
        '4': 'CD',
        '5': 'D',
        '6': 'DC',
        '7': 'DCC',
        '8': 'DCCC',
        '9': 'CM'
    }
}
n = pyip.inputInt(prompt='Enter a number you want to convert:', max=4999, min=1)
units = n % 10
n = int(n / 10)
tens = n % 10
n = int(n / 10)
hundreds = n % 10
n = int(n / 10)
thousands = n % 10
n = int(n / 10)
print('M'*thousands + lookup['hundreds'][str(hundreds)] + lookup['tens'][str(tens)] + lookup['units'][str(units)])