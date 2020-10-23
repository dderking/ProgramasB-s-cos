def tem_afinidade(l1, l2):
    cont = 0
    for i in range(len(l1)):
        for e in range(len(l2)):
            if l1[i] == l2[e]:
                cont +=1
    if cont >= 3: return True
    return False
