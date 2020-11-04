def encrypt_this(text):
    string = [] 
    for word in text.split(' '):
        encripted = []
        if len(word) == 0:
            return ' '.join(string)
        elif len(word) == 1:
            encripted.append(ord(word))
        elif len(word) == 2:
            encripted.append(ord(word[0]))
            encripted.append(word[-1])
        elif len(word) == 3:
            encripted.append(ord(word[0]))
            encripted.append(word[-1])
            encripted.append(word[1])
        else:
            encripted.append(ord(word[0]))
            encripted.append(word[-1])
            encripted.append(word[2:-1])
            encripted.append(word[1])
        new = [str(x) for x in encripted]
        string.append(''.join(new))
    #print(text.split(' '))
    return ' '.join(string)