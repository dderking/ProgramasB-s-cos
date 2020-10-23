def tradutor_morse(seq):
    aux = ''
    alfa = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(seq)):
        for e in range(26):
            if seq[i] == alfa[e]:
                aux += alfabeto[e]
                break
    return aux
