class RomanToInt:
    int_number=0

    @classmethod
    def __init__(cls,roman_number):

        roman_digits={'M':1000, 'D':500, 'C': 100,
                      'L':50, 'X': 10, 'V':5, 'I':1}      
        last = 1
        for i in roman_number[::-1]:
            if roman_digits[i] < last:
                cls.int_number-=roman_digits[i]
            else:
                cls.int_number+=roman_digits[i]
                last=roman_digits[i]

    @classmethod
    def __str__(cls):
        return str(cls.int_number)


print(RomanToInt('MDXIII'))
