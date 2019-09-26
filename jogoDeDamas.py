TABULEIRO= []
MinComum = 'MinComum'
MinDama = 'MinDama'
Bloqueado = 'Bloqueado'
Vazio = 'Vazio'
MaxComum = 'MaxComum'
MaxDama = 'MaxDama'

#Representações no Tabuleiro
#peça comum do jogador mim
minComum = 347
#dama do jogador min
minDama = 349
#posição que não pode ser utilizada
bloqueado = 107
#posição que pode ser utilizada mas está vazia
vazio = 211
#peça comum do jogador max
maxComum = 5
#dama do jogador max
maxDama = 7

#dicionário com as quantidades de peças comum e damas de cada jogador
quantidades = {MinComum:12,MinDama:0,MaxComum:12,MaxDama:0}
#defini o intervalo que uma ´posição pode ter
limiteInferior = 0
limiteSuperior = 63
Max ='Max'
Min ='Min'
fator = {Min:1,Max:-1}
vencedor = 'vencedor'
jogador = 'jogador'
table = {MinComum:'',MinDama:'',MaxComum:'',MaxDama:'',vencedor:'', jogador:''}
depth = 'depth'
limite = 'limite'
values = {depth:0,limite:0}
posJogadaMin = -1
comeuMin = False
comeuMax = False

#Inicia as configurações iniciais do jogo
def DEFINIR_VALORES_MIN_MAX(lim=5, ini=1):
    global TABULEIRO
    TABULEIRO= [107,  5,107,  5,107,  5,107,  5,
                  5,107,  5,107,  5,107,  5,107,
                107,  5,107,  5,107,  5,107,  5,
                211,107,211,107,211,107,211,107,
                107,211,107,211,107,211,107,211,
                347,107,347,107,347,107,347,107,
                107,347,107,347,107,347,107,347,
                347,107,347,107,347,107,347,107]
    values[limite] = lim
    print ('\nA prufundidade de busca sera: ')
    print(values[limite])
    if ini == 1 : table[jogador] = Min
    elif True : table[jogador] = Max
    print ('\n '+ table[jogador] + ' ira comecar jogando!\n')

#Retorna o estado atual do tabuleiro
def GET_TABULEIRO():
    global TABULEIRO
    return TABULEIRO

#Retorna a quantidade de peças restante
def QUANTIDADE(TABU, comum, dama):
    TAB=[]
    TAB[:] = TABU
    cont = 0
    if len(TAB) > 0:
        pos = 1
        for i in range (1, 9):
            fim = pos+6
            while pos <= fim:
                if TAB[pos] == comum or TAB[pos] == dama: cont = cont+1
                pos = pos+2
            if (i % 2) == 0: pos = pos + 1
            elif True: pos = pos - 1
    return cont

#Verifica se o jogo acabou
#se min não tem mais peças, max é o vencedor
#se max não tem mais peças, min é o vencedor
#se min está totalmente encurralado, max é o vencedor
#se max está totalmente encurralado, min é o vencedor
def TESTE_TERMINACAO(TB):
    TA=[]
    TA[:]=TB
    table[vencedor]=''
    terminou = False
    if QUANTIDADE(TB, minComum, minDama) == 0:
        terminou = True
        table[vencedor] = Max
    elif QUANTIDADE(TB, maxComum, maxDama) == 0:
        terminou = True
        table[vencedor] = Min
    elif True:
        bloqMin = True
        bloqMax = True
        pos = 1
        for i in range (1, 9):
            fim = pos+6
            while pos <= fim:
                if bloqMin:
                    if TA[pos] <= minDama:
                        newPos = pos+7
                        if newPos <= limiteSuperior:
                            if TA[newPos] == vazio: bloqMin = False
                        newPos = pos+9
                        if newPos <= limiteSuperior:
                            if TA[newPos] == vazio: bloqMin = False
                    if TA[pos] == minDama:
                        newPos = pos-7
                        if newPos >= limiteInferior:
                            if TA[newPos] == vazio: bloqMin = False
                        newPos = pos-9
                        if newPos >= limiteInferior:
                            if TA[newPos] == vazio: bloqMin = False
                if bloqMax:
                    if TA[pos] >= maxComum:
                        newPos = pos-7
                        if newPos >= limiteInferior:
                            if TA[newPos] == vazio: bloqMax = False
                        newPos = pos-9
                        if newPos >= limiteInferior:
                            if TA[newPos] == vazio: bloqMax = False
                    if TA[pos] == maxDama:
                        newPos = pos+7
                        if newPos <= limiteSuperior:
                            if TA[newPos] == vazio: bloqMax = False
                        newPos = pos+9
                        if newPos <= limiteSuperior:
                            if TA[newPos] == vazio: bloqMax = False
                pos = pos + 2
            if (i % 2) == 0: pos = pos + 1
            elif True: pos = pos - 1
        if bloqMin: terminou = True ; table[vencedor] = Max
        elif bloqMax: terminou = True ; table[vencedor] = Min
    return terminou    
                        
                
    
    
#efetua a jogada do MIN se possível
#atualiza posJogadaMin (posição de jogada do jogador)
#retorna falso se efetuou jogada
def PROXIMA_JOGADA_MIN(posIni=-1, posFim=-1):
    global TABULEIRO
    global posJogadaMin
    global comeuMin
    continua = True
    posJogadaMin = -1
    comeuMin = False
    if continua:
        if posIni >= limiteInferior and posIni <= limiteSuperior:
            if posFim >= limiteInferior and posFim <= limiteSuperior:
                if TABULEIRO[posIni] == minComum:
                    if posFim == (posIni-7) and TABULEIRO[posFim] == vazio:
                        TABULEIRO[posIni] = vazio
                        if posFim < 8:
                            TABULEIRO[posFim] = minDama
                            quantidades[MinDama] = quantidades[MinDama] + 1
                            quantidades[MinComum] = quantidades[MinComum] -1
                        elif True: TABULEIRO[posFim] = minComum
                        continua = False
                    elif posFim == (posIni-9) and TABULEIRO[posFim] == vazio:
                        TABULEIRO[posIni] = vazio
                        if posFim < 8:
                            TABULEIRO[posFim] = minDama
                            quantidades[MinDama] = quantidades[MinDama] + 1
                            quantidades[MinComum] = quantidades[MinComum] -1
                        elif True: TABULEIRO[posFim] = minComum
                        continua = False
                    elif posFim == (posIni-14) and TABULEIRO[posFim] == vazio:
                        if TABULEIRO[posIni-7] == maxComum:
                            TABULEIRO[posIni] = vazio
                            if posFim < 8:
                                TABULEIRO[posFim] = minDama
                                quantidades[MinDama] = quantidades[MinDama] + 1
                                quantidades[MinComum] = quantidades[MinComum] -1
                            elif True: TABULEIRO[posFim] = minComum
                            TABULEIRO[posIni-7] = vazio
                            quantidades[MaxComum] = quantidades[MaxComum] -1
                            continua = False
                            comeuMin = True
                        elif TABULEIRO[posIni-7] == maxDama:
                            TABULEIRO[posIni] = vazio
                            if posFim < 8:
                                TABULEIRO[posFim] = minDama
                                quantidades[MinDama] = quantidades[MinDama] + 1
                                quantidades[MinComum] = quantidades[MinComum] -1
                            elif True: TABULEIRO[posFim] = minComum
                            TABULEIRO[posIni-7] = vazio
                            quantidades[MaxDama] = quantidades[MaxDama] -1
                            continua = False
                            comeuMin = True
                    elif posFim == (posIni-18) and TABULEIRO[posFim] == vazio:
                        if TABULEIRO[posIni-9] == maxComum:
                            TABULEIRO[posIni] = vazio
                            if posFim < 8:
                                TABULEIRO[posFim] = minDama
                                quantidades[MinDama] = quantidades[MinDama] + 1
                                quantidades[MinComum] = quantidades[MinComum] -1
                            elif True: TABULEIRO[posFim] = minComum
                            TABULEIRO[posIni-9] = vazio
                            quantidades[MaxComum] = quantidades[MaxComum] -1
                            continua = False
                            comeuMin = True
                        elif TABULEIRO[posIni-9] == maxDama:
                            TABULEIRO[posIni] = vazio
                            if posFim < 8:
                                TABULEIRO[posFim] = minDama
                                quantidades[MinDama] = quantidades[MinDama] + 1
                                quantidades[MinComum] = quantidades[MinComum] -1

                            elif True: TABULEIRO[posFim] = minComum
                            TABULEIRO[posIni-9] = vazio
                            quantidades[MaxDama] = quantidades[MaxDama] -1
                            continua = False
                            comeuMin = True
                elif TABULEIRO[posIni] == minDama:
                    if posFim == (posIni-7) and TABULEIRO[posFim] == vazio:
                        TABULEIRO[posIni] = vazio
                        TABULEIRO[posFim] = minDama
                        continua = False
                    elif posFim == (posIni-9) and TABULEIRO[posFim] == vazio:
                        TABULEIRO[posIni] = vazio
                        TABULEIRO[posFim] = minDama
                        continua = False
                    elif posFim == (posIni-14) and TABULEIRO[posFim] == vazio:
                        if TABULEIRO[posIni-7] == maxComum:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni-7] = vazio
                            quantidades[MaxComum] = quantidades[MaxComum] -1
                            continua = False
                            comeuMin = True
                        elif TABULEIRO[posIni-7] == maxDama:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni-7] = vazio
                            quantidades[MaxDama] = quantidades[MaxDama] -1
                            continua = False
                            comeuMin = True
                    elif posFim == (posIni-18) and TABULEIRO[posFim] == vazio:
                        if TABULEIRO[posIni-9] == maxComum:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni-9] = vazio
                            quantidades[MaxComum] = quantidades[MaxComum] -1
                            continua = False
                            comeuMin = True
                        elif TABULEIRO[posIni-9] == maxDama:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni-9] = vazio
                            quantidades[MaxDama] = quantidades[MaxDama] -1
                            continua = False
                            comeuMin = True
                    elif posFim == (posIni+7) and TABULEIRO[posFim] == vazio:
                        TABULEIRO[posIni] = vazio
                        TABULEIRO[posFim] = minDama
                        continua = False
                    elif posFim == (posIni+9) and TABULEIRO[posFim] == vazio:
                        TABULEIRO[posIni] = vazio
                        TABULEIRO[posFim] = minDama
                        continua = False
                    elif posFim == (posIni+14) and TABULEIRO[posFim] == vazio:
                        if TABULEIRO[posIni+7] == maxComum:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni+7] = vazio
                            quantidades[MaxComum] = quantidades[MaxComum] -1
                            continua = False
                            comeuMin = True
                        elif TABULEIRO[posIni+7] == maxDama:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni+7] = vazio
                            quantidades[MaxDama] = quantidades[MaxDama] -1
                            continua = False
                            comeuMin = True
                    elif posFim == (posIni+18) and TABULEIRO[posFim] == vazio:
                        if TABULEIRO[posIni+9] == maxComum:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni+9] = vazio
                            quantidades[MaxComum] = quantidades[MaxComum] -1
                            continua = False
                            comeuMin = True
                        elif TABULEIRO[posIni+9] == maxDama:
                            TABULEIRO[posIni] = vazio
                            TABULEIRO[posFim] = minDama
                            TABULEIRO[posIni+9] = vazio
                            quantidades[MaxDama] = quantidades[MaxDama] -1
                            continua = False
                            comeuMin = True
        if not continua: posJogadaMin = posFim
    return continua

#simula a jogada do MIN
def JOGADA_MIN(posIni, TAB, select, visitados=[]):
    jogouMin = False
    T=[]
    T[:] = TAB
    posFim = -1
    if T[posIni] == minComum:
        if select == 0:
            posFim = posIni-14
            if posFim >= limiteInferior and posFim <= limiteSuperior:
                if T[posFim] == vazio and T[posFim+7] == maxComum:
                    T[posIni] = vazio
                    if posFim < 8:
                        T[posFim] = minDama
                        quantidades[MinDama] = quantidades[MinDama] + 1
                        quantidades[MinComum] = quantidades[MinComum] -1
                    elif True: T[posFim] = minComum
                    T[posFim+7] = vazio
                    quantidades[MaxComum] = quantidades[MaxComum] - 1
                    jogouMin = True
                elif T[posFim] == vazio and T[posFim+7] == maxDama:
                    T[posIni] = vazio
                    if posFim < 8:
                        T[posFim] = minDama
                        quantidades[MinDama] = quantidades[MinDama] + 1
                        quantidades[MinComum] = quantidades[MinComum] -1
                    elif True: T[posFim] = minComum
                    T[posFim+7] = vazio
                    quantidades[MaxDama] = quantidades[MaxDama] - 1
                    jogouMin = True
            if not jogouMin and (posIni-7) >= limiteInferior and (posIni-7) <= limiteSuperior:
                posFim = posIni-7
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    if posFim < 8:
                        T[posFim] = minDama
                        quantidades[MinDama] = quantidades[MinDama] + 1
                        quantidades[MinComum] = quantidades[MinComum] -1
                    elif True: T[posFim] = minComum
                    jogouMin = True
        elif select == 1:
            if not jogouMin and (posIni-18) >= limiteInferior and (posIni-18) <= limiteSuperior:
                posFim = posIni-18
                if T[posFim] == vazio and T[posFim+9] == maxComum:
                    T[posIni] = vazio
                    if posFim < 8:
                        T[posFim] = minDama
                        quantidades[MinDama] = quantidades[MinDama] + 1
                        quantidades[MinComum] = quantidades[MinComum] -1
                    elif True: T[posFim] = minComum
                    T[posFim+9] = vazio
                    quantidades[MaxComum] = quantidades[MaxComum] - 1
                    jogouMin = True
                elif T[posFim] == vazio and T[posFim+9] == maxDama:
                    T[posIni] = vazio
                    if posFim < 8:
                        T[posFim] = minDama
                        quantidades[MinDama] = quantidades[MinDama] + 1
                        quantidades[MinComum] = quantidades[MinComum] -1
                    elif True: T[posFim] = minComum
                    T[posFim+9] = vazio
                    quantidades[MaxDama] = quantidades[MaxDama] - 1
                    jogouMin = True
            if not jogouMin and (posIni-9) >= limiteInferior and (posIni-9) <= limiteSuperior:
                posFim = posIni-9
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    if posFim < 8:
                        T[posFim] = minDama
                        quantidades[MinDama] = quantidades[MinDama] + 1
                        quantidades[MinComum] = quantidades[MinComum] -1
                    elif True: T[posFim] = minComum
                    jogouMin = True

    elif T[posIni] == minDama:
        if select == 0:
            posFim = posIni-14
            if posFim >= limiteInferior and posFim <= limiteSuperior and posFim not in visitados:
                if T[posFim] == vazio and T[posFim+7] == maxComum:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim+7] = vazio
                    quantidades[MaxComum] = quantidades[MaxComum] - 1
                    jogouMin = True
                elif T[posFim] == vazio and T[posFim+7] == maxDama:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim+7] = vazio
                    quantidades[MaxDama] = quantidades[MaxDama] - 1
                    jogouMin = True
            if not jogouMin and (posIni-7) >= limiteInferior and (posIni-7) <= limiteSuperior and (posIni-7) not in visitados:
                posFim = posIni-7
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = minDama
                    jogouMin = True
        elif select == 1:
            if not jogouMin and (posIni-18) >= limiteInferior and (posIni-18) <= limiteSuperior and (posIni-18) not in visitados:
                posFim = posIni-18
                if T[posFim] == vazio and T[posFim+9] == maxComum:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim+9] = vazio
                    quantidades[MaxComum] = quantidades[MaxComum] - 1
                    jogouMin = True
                elif T[posFim] == vazio and T[posFim+9] == maxDama:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim+9] = vazio
                    quantidades[MaxDama] = quantidades[MaxDama] - 1
                    jogouMin = True
            if not jogouMin and (posIni-9) >= limiteInferior and (posIni-9) <= limiteSuperior and (posIni-9) not in visitados:
                posFim = posIni-9
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = minDama
                    jogouMin = True
        elif select == 2:
            if not jogouMin and (posIni+14) >= limiteInferior and (posIni+14) <= limiteSuperior and (posIni+14) not in visitados:
                posFim = posIni+14
                if T[posFim] == vazio and T[posFim-7] == maxComum:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim-7] = vazio
                    quantidades[MaxComum] = quantidades[MaxComum] - 1
                    jogouMin = True
                elif T[posFim] == vazio and T[posFim-7] == maxDama:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim-7] = vazio
                    quantidades[MaxDama] = quantidades[MaxDama] - 1
                    jogouMin = True
            if not jogouMin and (posIni+7) >= limiteInferior and (posIni+7) <= limiteSuperior and (posIni+7) not in visitados:
                posFim = posIni+7
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = minDama
                    jogouMin = True
        elif select == 3:
            if not jogouMin and (posIni+18) >= limiteInferior and (posIni+18) <= limiteSuperior and (posIni+18) not in visitados:
                posFim = posIni+18
                if T[posFim] == vazio and T[posFim-9] == maxComum:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim-9] = vazio
                    quantidades[MaxComum] = quantidades[MaxComum] - 1
                    jogouMin = True
                elif T[posFim] == vazio and T[posFim-9] == maxDama:
                    T[posIni] = vazio
                    T[posFim] = minDama
                    T[posFim-9] = vazio
                    quantidades[MaxDama] = quantidades[MaxDama] - 1
                    jogouMin = True
            if not jogouMin and (posIni+9) >= limiteInferior and (posIni+9) <= limiteSuperior and (posIni+9) not in visitados:
                posFim = posIni+9
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = minDama
                    jogouMin = True
    if not jogouMin: T=[]
    return T


#simula a jogada do MAX
def JOGADA_MAX(posIni, TAB, select, visitados=[]):
    jogouMax = False
    T=[]
    T[:]=TAB
    posFim = -1
    if T[posIni] == maxComum:
        if select == 0:
            posFim = posIni+14
            if posFim >= limiteInferior and posFim <= limiteSuperior:
                if T[posFim] == vazio and T[posFim-7] == minComum:
                    T[posIni] = vazio
                    if posFim > 55:
                        T[posFim] = maxDama
                        quantidades[MaxDama] = quantidades[MaxDama] + 1
                        quantidades[MaxComum] = quantidades[MaxComum] -1
                    elif True: T[posFim] = maxComum
                    T[posFim-7] = vazio
                    quantidades[MinComum] = quantidades[MinComum] - 1
                    jogouMax = True
                elif T[posFim] == vazio and T[posFim-7] == minDama:
                    T[posIni] = vazio
                    if posFim > 55:
                        T[posFim] = maxDama
                        quantidades[MaxDama] = quantidades[MaxDama] + 1
                        quantidades[MaxComum] = quantidades[MaxComum] -1
                    elif True: T[posFim] = maxComum
                    T[posFim-7] = vazio
                    quantidades[MinDama] = quantidades[MinDama] - 1
                    jogouMax = True
            if not jogouMax and (posIni+7) >= limiteInferior and (posIni+7) <= limiteSuperior:
                posFim = posIni+7
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    if posFim > 55:
                        T[posFim] = maxDama
                        quantidades[MaxDama] = quantidades[MaxDama] + 1
                        quantidades[MaxComum] = quantidades[MaxComum] -1
                    elif True: T[posFim] = maxComum
                    jogouMax = True
        elif select == 1:
            if not jogouMax and (posIni+18) >= limiteInferior and (posIni+18) <= limiteSuperior:
                posFim = posIni+18
                if T[posFim] == vazio and T[posFim-9] == minComum:
                    T[posIni] = vazio
                    if posFim > 55:
                        T[posFim] = maxDama
                        quantidades[MaxDama] = quantidades[MaxDama] + 1
                        quantidades[MaxComum] = quantidades[MaxComum] -1
                    elif True: T[posFim] = maxComum
                    T[posFim-9] = vazio
                    quantidades[MinComum] = quantidades[MinComum] - 1
                    jogouMax = True
                elif T[posFim] == vazio and T[posFim-9] == minDama:
                    T[posIni] = vazio
                    if posFim > 55:
                        T[posFim] = maxDama
                        quantidades[MaxDama] = quantidades[MaxDama] + 1
                        quantidades[MaxComum] = quantidades[MaxComum] -1
                    elif True: T[posFim] = maxComum
                    T[posFim-9] = vazio
                    quantidades[MinDama] = quantidades[MinDama] - 1
                    jogouMax = True
            if not jogouMax and (posIni+9) >= limiteInferior and (posIni+9) <= limiteSuperior:
                posFim = posIni+9
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    if posFim > 55:
                        T[posFim] = maxDama
                        quantidades[MaxDama] = quantidades[MaxDama] + 1
                        quantidades[MaxComum] = quantidades[MaxComum] -1
                    elif True: T[posFim] = maxComum
                    jogouMax = True
    elif T[posIni] == maxDama:
        if select == 0:
            posFim = posIni+14
            if posFim >= limiteInferior and posFim <= limiteSuperior and posFim not in visitados:
                if T[posFim] == vazio and T[posFim-7] == minComum:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim-7] = vazio
                    quantidades[MinComum] = quantidades[MinComum] - 1
                    jogouMax = True
                elif T[posFim] == vazio and T[posFim-7] == minDama:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim-7] = vazio
                    quantidades[MinDama] = quantidades[MinDama] - 1
                    jogouMax = True
            if not jogouMax and (posIni+7) >= limiteInferior and (posIni+7) <= limiteSuperior and (posIni+7) not in visitados:
                posFim = posIni+7
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    jogouMax = True
        elif select == 1:
            if not jogouMax and (posIni+18) >= limiteInferior and (posIni+18) <= limiteSuperior and (posIni+18) not in visitados:
                posFim = posIni+18
                if T[posFim] == vazio and T[posFim-9] == minComum:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim-9] = vazio
                    quantidades[MinComum] = quantidades[MinComum] - 1
                    jogouMax = True
                elif T[posFim] == vazio and T[posFim-9] == minDama:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim-9] = vazio
                    quantidades[MinDama] = quantidades[MinDama] - 1
                    jogouMax = True
            if not jogouMax and (posIni+9) >= limiteInferior and (posIni+9) <= limiteSuperior and (posIni+9) not in visitados:
                posFim = posIni+9
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    jogouMax = True
        elif select == 2:
            if not jogouMax and (posIni-14) >= limiteInferior and (posIni-14) <= limiteSuperior and (posIni-14) not in visitados:
                posFim = posIni-14
                if T[posFim] == vazio and T[posFim+7] == minComum:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim+7] = vazio
                    quantidades[MinComum] = quantidades[MinComum] - 1
                    jogouMax = True
                elif T[posFim] == vazio and T[posFim+7] == minDama:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim+7] = vazio
                    quantidades[MinDama] = quantidades[MinDama] - 1
                    jogouMax = True
            if not jogouMax and (posIni-7) >= limiteInferior and (posIni-7) <= limiteSuperior and (posIni-7) not in visitados:
                posFim = posIni-7
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    jogouMax = True
        elif select == 3:
            if not jogouMax and (posIni-18) >= limiteInferior and (posIni-18) <= limiteSuperior and (posIni-18) not in visitados:
                posFim = posIni-18
                if T[posFim] == vazio and T[posFim+9] == minComum:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim+9] = vazio
                    quantidades[MinComum] = quantidades[MinComum] - 1
                    jogouMax = True
                elif T[posFim] == vazio and T[posFim+9] == minDama:
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    T[posFim+9] = vazio
                    quantidades[MinDama] = quantidades[MinDama] - 1
                    jogouMax = True
            if not jogouMax and (posIni-9) >= limiteInferior and (posIni-9) <= limiteSuperior and (posIni-9) not in visitados:
                posFim = posIni-9
                if T[posFim] == vazio :
                    T[posIni] = vazio
                    T[posFim] = maxDama
                    jogouMax = True
    if not jogouMax: T=[]
    return T

#min max com corte alfa e beta
#utilizando uma função de utilidade para ajudar os casos em que o último estado
#não é um estado de terminação
def MinMaxAB(tab, player, dept, alf, bet, listaMin, listaMax):
    state=[]
    state[:]=tab
    if dept >= values[limite] or TESTE_TERMINACAO(state): return FUNCAO_UTILIDADE(state, player)
    elif player == Min:
        i=1
        pos = 1
        continua = True
        while i<9 and continua:
            fim = pos+6
            while pos <= fim and continua:
                if state[pos]== minComum or state[pos] == minDama:
                    listMin = []
                    listMax = []
                    listMin[:] = listaMin
                    listMax[:] = listaMax
                    listMin = listMin + [pos]
                    for j in range(4):
                        TempMin=[]
                        TempMin[:]=JOGADA_MIN(pos, state, j, listaMin)
                        if len(TempMin) != 0:
                            val = MinMaxAB(TempMin, Max, dept+1, alf, bet, listMin, listMax)
                            if val < bet:
                                bet=val
                            if alf >= bet: continua=False
                pos = pos+2
            if (i % 2) == 0: pos = pos + 1
            elif True: pos = pos - 1
            i = i + 1
        state=[]
        return bet
    elif player == Max:
        i=1
        pos = 1
        continua=True
        while i<9 and continua:
            fim = pos+6
            while pos <= fim and continua:
                if state[pos] == maxComum or state[pos] == maxDama:
                    listMin = []
                    listMax = []
                    listMin[:] = listaMin
                    listMax[:] = listaMax
                    listMax = listMax + [pos]
                    for j in range(4):
                        TempMax=[]
                        TempMax[:]=JOGADA_MAX(pos, state, j, listaMax)
                        if len(TempMax) != 0:
                            val = MinMaxAB(TempMax, Min, dept+1, alf, bet, listMin, listMax)
                            if val > alf:
                                alf=val
                            if alf >= bet: continua = False
                pos = pos+2
            if (i % 2) == 0: pos = pos + 1
            elif True: pos = pos - 1
            i = i + 1
        state=[]
        return alf

#metodo chamado a cada jogada
#cont define quantas jogas serão efetuada
#por default 2, uma para o jogador humano e a outra para a máquina    
def PROXIMA_JOGADA(cont=2, pIni=1, pFim=-1):
    global TABULEIRO
    global posJogadaMin
    global comeuMin
    global comeuMax
    k=0
    jogou = False
    table[jogador]=Min
    while not TESTE_TERMINACAO(TABULEIRO) and k < cont and not jogou:
        if table[jogador]== Max:
            values[depth]=0
            AL=-999
            BT=999
            AUX=[]
            posJogada = -1
            continua=True
            i=1
            pos = 1
            while i<9 and continua:
                fim = pos+6
                while pos <= fim and continua:
                    if TABULEIRO[pos] == maxComum or TABULEIRO[pos] == maxDama:
                        for j in range(4):
                            TABU=[]
                            TABU[:]= JOGADA_MAX(pos, TABULEIRO, j)
                            if len(TABU) != 0:
                                listMax = [pos]
                                listMin = []
                                avaliacao = MinMaxAB(TABU,Min,values[depth]+1,AL,BT+1, listMin, listMax)
                                if avaliacao > AL:
                                    AL=avaliacao
                                    AUX[:]=TABU
                                    posJogada = ACHAR_POSICAO_FINAL(TABULEIRO, AUX)
                                if AL >= BT:    
                                    continua=False
                    pos = pos+2
                if (i % 2) == 0: pos = pos + 1
                elif True: pos = pos - 1
                i=i+1
            TABULEIRO[:]=AUX
            values[depth] = values[depth]+1
        
        elif table[jogador]== Min:
            jogou = PROXIMA_JOGADA_MIN(pIni, pFim)
             
        if table[jogador]==Max:
            if not COMER_DENOVO(posJogada, comeuMax): table[jogador]=Min
            else: cont = cont+1
        elif table[jogador]==Min:
            if not COMER_DENOVO(posJogadaMin, comeuMin): table[jogador]=Max
            else: cont = cont+1
        k=k+1

#Encontra a posição de jogada do Max quando MinMaxAB() retorna um valor melhor que alfa
def ACHAR_POSICAO_FINAL(TA, TB):
    global comeuMax
    comeuMax = False
    posFim=-1
    i = 1
    pos = 1
    alterado = 0
    while i<9:
        fim = pos+6
        while pos <= fim:
            value = TA[pos] - TB[pos]
            if value != 0: alterado = alterado +1
            if value == 204 or value == 206:
                posFim = pos
            pos = pos +2
        if (i % 2) == 0: pos = pos + 1
        elif True: pos = pos - 1
        i=i+1
    if alterado == 3: comeuMax = True
    return posFim
    

#verifica se um jogador pode comer denovo
def COMER_DENOVO(pos, comeu):
    global TABULEIRO
    denovo = False
    if comeu:
        if TABULEIRO[pos] == minComum or TABULEIRO[pos] == minDama:
            posFim = pos-14
            if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                if TABULEIRO[pos-7] == maxComum and TABULEIRO[posFim] == vazio: denovo = True
                elif TABULEIRO[pos-7] == maxDama and TABULEIRO[posFim] == vazio: denovo = True
            posFim = pos-18
            if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                if TABULEIRO[pos-9] == maxComum and TABULEIRO[posFim] == vazio: denovo = True
                elif TABULEIRO[pos-9] == maxDama and TABULEIRO[posFim] == vazio: denovo = True
            if TABULEIRO[pos] == minDama:
                posFim = pos+14
                if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                    if TABULEIRO[pos+7] == maxComum and TABULEIRO[posFim] == vazio: denovo = True
                    elif TABULEIRO[pos+7] == maxDama and TABULEIRO[posFim] == vazio: denovo = True
                posFim = pos+18
                if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                    if TABULEIRO[pos+9] == maxComum and TABULEIRO[posFim] == vazio: denovo = True
                    elif TABULEIRO[pos+9] == maxDama and TABULEIRO[posFim] == vazio: denovo = True

        elif TABULEIRO[pos] == maxComum or TABULEIRO[pos] == maxDama:
            posFim = pos+14
            if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                if TABULEIRO[pos+7] == minComum and TABULEIRO[posFim] == vazio: denovo = True
                elif TABULEIRO[pos+7] == minDama and TABULEIRO[posFim] == vazio: denovo = True
            posFim = pos+18
            if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                if TABULEIRO[pos+9] == minComum and TABULEIRO[posFim] == vazio: denovo = True
                elif TABULEIRO[pos+9] == minDama and TABULEIRO[posFim] == vazio: denovo = True
            if TABULEIRO[pos] == minDama:
                posFim = pos-14
                if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                    if TABULEIRO[pos-7] == minComum and TABULEIRO[posFim] == vazio: denovo = True
                    elif TABULEIRO[pos-7] == minDama and TABULEIRO[posFim] == vazio: denovo = True
                posFim = pos-18
                if (posFim) >= limiteInferior and (posFim) <= limiteSuperior:
                    if TABULEIRO[pos-9] == minComum and TABULEIRO[posFim] == vazio: denovo = True
                    elif TABULEIRO[pos-9] == minDama and TABULEIRO[posFim] == vazio: denovo = True
        
    return denovo
        

#verifica se um valor é par
def PAR(value):
    if (value%2) == 0: return True
    elif True: return False

#O tabuleiro foi preenchido com valores inteiros e primos
#de acordo com a referencia no início do código
#a função realiza cálculos com esses números para efetuar o valor que diga se uma jogda é boa ou não
def FUNCAO_UTILIDADE(TABE, jogador):
    TAB=[]
    TAB[:]=TABE
    retorno=0
    A=1
    B=10
    C=19
    f=0
    for i in range(6):
        for j in range(6):
            funcao = (TAB[A]*TAB[A])+TAB[B]+(TAB[C]*3) #A²+B+3C - funçao quadrada
            if jogador == Max:
                if funcao == 45567 or funcao == 45573: f=f-15
                elif funcao == 1301 or funcao == 1307 or funcao == 122033: f=f-8
                elif funcao == 1277 or funcao == 1283: f=f-9
                elif funcao == 665 or funcao == 689 or funcao == 44549: f=f-4
                elif funcao == 663 or funcao == 687 or funcao == 44543: f=f-2
                elif funcao == 122439: f=f+6
                elif funcao == 44569 or funcao == 45575 or funcao == 122441: f=f+4
                elif funcao == 251 or funcao == 275: f=f+18
                elif funcao == 257 or funcao == 281: f=f+24
                elif funcao == 120641: f=f+30
                elif funcao == 1005 or funcao == 1029 or funcao == 44889: f=f+49
                elif funcao == 1007 or funcao == 1031 or funcao == 44891: f=f+56
            elif jogador == Min:
                if funcao == 1005 or funcao == 1029: f=f-35
                elif funcao == 1283 or funcao == 1307 or funcao == 122033: f=f-16
                elif funcao == 1277 or funcao == 1301: f=f-18
                elif funcao == 45911 or funcao == 45917 or funcao == 122783: f=f-4
                elif funcao == 45909 or funcao == 45915 or funcao == 121391: f=f-2
                elif funcao == 44889: f=f+6
                elif funcao == 1007 or funcao == 1031 or funcao == 44891: f=f+4
                elif funcao == 121661 or funcao == 121667: f=f+9
                elif funcao == 123053 or funcao == 123059: f=f+12
                elif funcao == 122027: f=f+30
                elif funcao == 45567 or funcao == 45573 or funcao == 122439: f=f+14
                elif funcao == 45569 or funcao == 45575 or funcao == 122441: f=f+16
            if PAR(j):
                A=A+2
                C=C-2
            elif True:
                B=B+2
                C=C+4
        if PAR(i):
            A=A+1
            B=B+1
            C=C+1
        else:
            A=A+3
            B=B+3
            C=C+3
        retorno = f
    return retorno
        


