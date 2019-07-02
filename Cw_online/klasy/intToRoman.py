class IntToRoman:
    latin_number=''
    roman_number=''

    @classmethod
    def __init__(cls,latin_number):
        cls.latin_number=latin_number
        roman_digits=(('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1))
        for i in range(0,7,2):
            ratio=cls.latin_number//roman_digits[i][1]
            if ratio>0:
                if ratio in (1,2,3):
                    cls.roman_number+=roman_digits[i][0]*ratio
                elif ratio==4:
                    cls.roman_number+=roman_digits[i][0]+roman_digits[i-1][0]
                elif ratio in (5,6,7,8):
                    cls.roman_number+=roman_digits[i-1][0]+roman_digits[i][0]*(ratio-5)
                elif ratio in (9,10):
                    cls.roman_number+=roman_digits[i][0]*(10-ratio)+roman_digits[i-2][0]
                cls.latin_number-=roman_digits[i][1]*ratio

    @classmethod
    def __str__(cls):
        return cls.roman_number


print(IntToRoman(900))
