class RomanToInt:
    int_number=0

    @classmethod
    def __init__(cls,roman_number):

        roman_digits={'M':1000, 'D':500, 'C': 100,
                      'L':50, 'X': 10, 'V':5, 'I':1}      

        roman_number=roman_number[::-1]
        
        for i in range(len(roman_number)):
            if i>0 and roman_digits[roman_number[i]] < roman_digits[roman_number[i-1]]:
                cls.int_number-=roman_digits[roman_number[i]]
            else:
                cls.int_number+=roman_digits[roman_number[i]]
 

    @classmethod
    def __str__(cls):
        return str(cls.int_number)


print(RomanToInt('MCDXIII'))
