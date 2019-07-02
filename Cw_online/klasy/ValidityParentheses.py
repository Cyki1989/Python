class ValidityParentheses:
    is_valid=True

    @classmethod
    def __init__(cls,string):

        Parentheses={'{':0, '}':'{', '[':0, ']':'[', '(':0, ')':'(' }

        for i in string:
            if isinstance(Parentheses[i],str):
               Parentheses[Parentheses[i]]-=1
               if Parentheses[Parentheses[i]]<0:
                   cls.is_valid=False
                   break
            else:
                Parentheses[i]+=1
        else:
            if Parentheses['['] or Parentheses['{'] or Parentheses['(']:
               cls.is_valid=False  

    @classmethod
    def __str__(cls):
        return str(cls.is_valid)


print(ValidityParentheses('([{])}'))
print(ValidityParentheses('()[{(})]'))
