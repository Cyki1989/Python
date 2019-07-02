class IntToRoman:
    roman_number=''

    @classmethod
    def __init__(cls,latin_number):

        roman_digits=(('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
                      ('C', 100), ('XC', 90),  ('L', 50), ('XL', 40),
                      ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))

        for roman_digit in roman_digits:
            while latin_number-roman_digit[1]>=0:
                cls.roman_number+=roman_digit[0]
                latin_number-=roman_digit[1]
            if not latin_number:
                break

    @classmethod
    def __str__(cls):
        return cls.roman_number


print(IntToRoman(1910))
