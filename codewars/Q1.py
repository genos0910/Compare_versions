input_str ="is2 Thi1s T4est 3a"
#input_str =""
def order(sentence):
    if sentence==None :
        return " "
    words=[]
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                words.append(word)
    return " ".join(words)

stance = order(input_str)
print(stance)
