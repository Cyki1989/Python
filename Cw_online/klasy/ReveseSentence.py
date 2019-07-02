
def revese_sentence(sentence):
    rev_sentence=''
    word=''    
    for char in sentence[::-1]:
        if char == ' ':
            word = word[::-1]
            rev_sentence += word + ' '
            word = ''
        else:
            word += char
    word=word[::-1]
    rev_sentence += word
    return rev_sentence 

print (revese_sentence('Ala ma kota'))


