class ValidityParentheses:
    is_valid=True

    @classmethod
    def __init__(cls,string):

        stack, parentheses=[],{'}':'{', ']':'[', ')':'('}

        for i in string:
            if i in parentheses.values():
                stack.append(i)
            elif len(stack)==0 or stack(parentheses[i] 

    @classmethod
    def __str__(cls):
        return str(cls.is_valid)


print(ValidityParentheses('([{])}'))
print(ValidityParentheses('()[{(})]'))
