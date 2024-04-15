class RomanNumber:
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    thousands = ['', 'M', 'MM', 'MMM']

    translating = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    possible_combos = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    combos_translating = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    def __init__(self, line):
        if str(line).isdigit() is True:
            if RomanNumber.is_int(line) is False:
                self.int_value = None
                print('ошибка')
                self.rom_value = None
            else:
                self.int_value = line
                self.rom_value = RomanNumber.roman_number(self)
        else:
            if RomanNumber.is_roman(line) is False:
                self.rom_value = None
                print('ошибка')
            else:
                self.rom_value = line
                self.int_value = RomanNumber.decimal_number(self)

    @staticmethod
    def is_roman(value):
        errors = 0
        for i in range(len(value)):
            if value[i] not in 'XLDCMIV':
                errors += 1
            else:
                if (i + 3 <= len(value) - 1) and (value[i] == value[i + 1] == value[i + 2] == value[i + 3]):
                    errors += 1
                else:
                    if (i + 1 <= len(value) - 1) and (
                            RomanNumber.translating[value[i]] < RomanNumber.translating[value[i + 1]]) and (
                            value[i] + value[i + 1] not in RomanNumber.possible_combos):
                        errors += 1
        if errors == 0:
            return True
        else:
            return False

    def decimal_number(self):
        result = 0
        number = self.rom_value
        while len(number) > 0:
            if (len(number) >= 3) and (number[0] == number[1] == number[2]):
                result += RomanNumber.translating[number[0]] * 3
                number = number[3:]
            elif (len(number) >= 2) and (number[0] == number[1]):
                result += RomanNumber.translating[number[0]] * 2
                number = number[2:]
            elif (len(number) >= 2) and (RomanNumber.translating[number[0]] < RomanNumber.translating[number[1]]) and (
                    number[0] + number[1] in RomanNumber.possible_combos):
                result += RomanNumber.combos_translating[number[0] + number[1]]
                number = number[2:]
            else:
                result += RomanNumber.translating[number[0]]
                number = number[1:]
        return result

    def roman_number(self):
        roman_line = ''
        if len(str(self.int_value)) == 1:
            roman_line = RomanNumber.ones[self.int_value - 1]

        elif len(str(self.int_value)) == 2:
            ten = int(str(self.int_value)[0])
            one = int(str(self.int_value)[1])
            roman_line = RomanNumber.tens[ten] + RomanNumber.ones[one]

        elif len(str(self.int_value)) == 3:
            hundred = int(str(self.int_value)[0])
            ten = int(str(self.int_value)[1])
            one = int(str(self.int_value)[2])
            roman_line = RomanNumber.hundreds[hundred] + RomanNumber.tens[ten] + RomanNumber.ones[one]

        elif len(str(self.int_value)) == 4:
            thousand = int(str(self.int_value)[0])
            hundred = int(str(self.int_value)[1])
            ten = int(str(self.int_value)[2])
            one = int(str(self.int_value)[3])
            roman_line = (RomanNumber.thousands[thousand] + RomanNumber.hundreds[hundred] + RomanNumber.tens[ten] +
                          RomanNumber.ones[one])
        return roman_line

    @staticmethod
    def is_int(value):
        if (value > 0) and (value <= 3999):
            return True
        else:
            return False

    def __repr__(self):
        return str(self.rom_value)


num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))
