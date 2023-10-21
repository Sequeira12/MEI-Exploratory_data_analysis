def leituraFicheiros(ficheiro, new_file):
    f_copy = open(new_file, "w")
    contador = 1
    with open(ficheiro, "r") as f:
        for j in f.readlines():
            if (contador <= 25):
                contador += 1
            else:
                sp = j.split(" ")
                for j in range(len(sp)):
                    if (sp[j] != ""):
                        if (j == len(sp)):
                            f_copy.write("\n")
                        else:
                            f_copy.write(sp[j])
                            f_copy.write(";")
        f_copy.close()


def compor(name_file, final):
    with open(name_file, 'r') as arquivo_entrada, open(final, 'w') as arquivo_saida:
        for linha in arquivo_entrada:
            # Remove o ponto e vírgula no início de cada linha
            linha_modificada = linha.lstrip(';')
            arquivo_saida.write(linha_modificada)
def CalculaHorasMinSegundos(tempo):
    horas = tempo // 3600 % 24  # 3600 segundos em uma hora
    minutos = (tempo % 3600) // 60  # 60 segundos em um minuto
    segundos = tempo % 60
    return horas,minutos,segundos


#FINISHED
def SemanaFileNASA(file):
    linhasAtualizadas = []
    segundosDia = 86400
    Semana = ['Sex', 'Sab', 'Dom', 'Seg', 'Ter', 'Qua', 'Qui']
    Meses = ['Out','Nov','Dez']
    DiasMeses = [31,30,31]
    mes = 0
    dia = 1
    with open(file, 'r') as ficheiro:
        contador = 0
        somaDiasMeses = 0

        for linha in ficheiro:
            if contador != 0:
                info = linha.split(";")
                SubmitTime = int(info[1]) + 3 # estes 3 segundos é por causa do inicio 0:0:3
                horas,min,segundos = CalculaHorasMinSegundos(SubmitTime)
                valor = int(SubmitTime) // segundosDia
                diaAux = valor - somaDiasMeses + 1
                DiaF = diaAux
                if(diaAux == DiasMeses[mes] + 1):
                    mes += 1
                    somaDiasMeses = 0
                    for i in range(mes):
                        somaDiasMeses += DiasMeses[i]

                    valor = valor % 7
                    DiaF = 1
                    if(mes != 3):
                        linha = linha[:-1] + ";" + Semana[valor] + ";" + str(DiaF) + ";" + Meses[mes] + ";" + str(horas) + ";" + str(min) + ";" + str(segundos) + '\n'
                    else:
                        linha = linha[:-1] + ";" + Semana[valor-1] + ";" + str(31) + ";" + Meses[mes-1] + ";" + str(int(horas - 1)) + ";" + str(min) + ";" + str(segundos) +  '\n'
                else:
                    valor = valor % 7
                    linha = linha[:-1] + ";" + Semana[valor] + ";" + str(DiaF) + ";" + Meses[mes] + ";" + str(horas) + ";" + str(min) + ";" + str(segundos) + '\n'
            else:
                linha = linha[:-1]  + "Dia de Semana" + ";" +"Dia" + ";" +"Mês" + ";" + "Horas" + ";" + "Minutos" + ";" +"Segundos" + '\n'
            linhasAtualizadas.append(linha)
            contador += 1
    with open('DATASET/NASA/NASA.csv', 'w') as arquivo:
        arquivo.writelines(linhasAtualizadas)

    print("NASA -- FEITO")

#FEITO
def SemanaFileHPCN(file):
    linhasAtualizadas = []
    segundosDia = 86400
    Semana = ['Sab', 'Dom','Seg','Ter', 'Qua', 'Qui', 'Sex']
    Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    DiasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia = 28
    mes = 5
    ano = 2002
    inicio = 6

    guardaValores = 31-28
    with open(file, 'r') as ficheiro:
        contador = 0
        somaDiasMeses = 0
        for linha in ficheiro:
            if contador != 0:
                info = linha.split(";")
                SubmitTime = int(info[1]) + 3  # Estes 3 segundos são devido ao início 0:0:3
                horas, min, segundos = CalculaHorasMinSegundos(SubmitTime)
                horas += 9
                horas = horas % 24

                valor = int(SubmitTime) // segundosDia


                diaAux = (valor - somaDiasMeses  + dia)
                DiaF = diaAux

                if diaAux > DiasMeses[mes]:
                    # Verifica se ultrapassou o mês atual
                    mes += 1

                    dia = 1
                    if mes == 12:
                        # Se o mês atual for dezembro, ajusta o ano e volta para janeiro
                        for i in range(inicio, mes):
                            guardaValores += DiasMeses[i]

                        inicio = 0

                        mes = 0
                        ano += 1




                    somaDiasMeses = 0 + guardaValores
                    for i in range(inicio,mes):
                        somaDiasMeses += DiasMeses[i]



                    dia = 1
                    valor = valor % 7
                    DiaF = 1

                valor = valor % 7
                linha = linha[:-1] + ";" + Semana[valor] + ";" + str(DiaF) + ";" + Meses[mes] + ";" + str(ano) + ";" + str(horas) + ";" + str(min) + ";" + str(segundos) + '\n'
            else:
                linha = linha[:-1] + "Dia de Semana" + ";" + "Dia" + ";" + "Mês" + ";" + "Ano" + ";" + "Horas" + ";" + "Minutos" + ";" + "Segundos" + '\n'
            linhasAtualizadas.append(linha)
            contador += 1

    with open('DATASET/HPC2N/HPC2N.csv', 'w') as arquivo:
        arquivo.writelines(linhasAtualizadas)
    print("HPC2N -- FEITO")


#FEITO
def SemanaFileSDSCBlue(file):
    linhasAtualizadas = []
    segundosDia = 86400
    Semana = ['Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom','Seg']
    Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    DiasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia = 25
    mes = 3
    ano = 2000
    inicio = 4
    guardaValores = 30 - 25
    with open(file, 'r') as ficheiro,open('DATASET/SDSC BLUE/SDSC-BLUE.csv', 'w') as arquivo:
        contador = 0
        somaDiasMeses = 0

        for linha in ficheiro:
            if contador != 0:
                info = linha.split(";")
                SubmitTime = int(info[1]) + 3  # Estes 3 segundos são devido ao início 0:0:3
                horas, min, segundos = CalculaHorasMinSegundos(SubmitTime)
                horas += 15

                horas = horas % 24

                valor = int(SubmitTime) // segundosDia

                diaAux = (valor - somaDiasMeses + dia)
                DiaF = diaAux

                if diaAux > DiasMeses[mes]:
                    # Verifica se ultrapassou o mês atual
                    mes += 1

                    dia = 1
                    if mes == 12:
                        # Se o mês atual for dezembro, ajusta o ano e volta para janeiro
                        for i in range(inicio, mes):
                            guardaValores += DiasMeses[i]

                        inicio = 0

                        mes = 0
                        ano += 1



                    somaDiasMeses = 0 + guardaValores
                    for i in range(inicio, mes):
                        somaDiasMeses += DiasMeses[i]

                    dia = 1
                    valor = valor % 7
                    DiaF = 1

                valor = valor % 7
                linha = linha[:-1] + ";" + Semana[valor] + ";" + str(DiaF) + ";" + Meses[mes] + ";" + str(ano) + ";" + str(horas) + ";" + str(min) + ";" + str(segundos) + '\n'
            else:
                linha = linha[:-1] + "Dia de Semana" + ";" + "Dia" + ";" + "Mês" + ";" + "Ano" + ";" + "Horas" + ";" + "Minutos" + ";" + "Segundos" + '\n'
            linhasAtualizadas.append(linha)
            contador += 1
            arquivo.write(linha)
    print("SDSC BLUE -- FEITO")





def SemanaFileSDSC96(file):
    linhasAtualizadas = []
    segundosDia = 86400
    Semana = [ 'Qua', 'Qui', 'Sex','Sab', 'Dom','Seg','Ter']
    Meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    DiasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia = 27
    mes = 11
    ano = 1995
    inicio = 12
    contaanos = 0
    guardaValores = 31-27
    with open(file, 'r') as ficheiro:
        contador = 0
        somaDiasMeses = 0
        for linha in ficheiro:
            if contador != 0:
                info = linha.split(";")
                SubmitTime = int(info[1]) + 57  # Estes 3 segundos são devido ao início 0:0:3
                horas, min, segundos = CalculaHorasMinSegundos(SubmitTime)
                horas += 10
                min += 53
                min = min % 60
                horas = horas % 24

                valor = int(SubmitTime) // segundosDia


                diaAux = (valor - somaDiasMeses  + dia)
                DiaF = diaAux

                if diaAux > DiasMeses[mes]:
                    # Verifica se ultrapassou o mês atual
                    mes += 1

                    dia = 1
                    if mes == 12:
                        # Se o mês atual for dezembro, ajusta o ano e volta para janeiro
                        for i in range(inicio, mes):
                            guardaValores += DiasMeses[i]

                        inicio = 0

                        mes = 0
                        ano += 1
                        contaanos += 1



                    somaDiasMeses = 0 + guardaValores
                    for i in range(inicio,mes):
                        somaDiasMeses += DiasMeses[i]



                    dia = 1
                    valor = valor % 7
                    DiaF = 1

                valor = valor % 7
                linha = linha[:-1] + ";" + Semana[valor] + ";" + str(DiaF) + ";" + Meses[mes] + ";" + str(ano) + ";" + str(horas) + ";" + str(min) + ";" + str(segundos) + '\n'
            else:
                linha = linha[:-1] + "Dia de Semana" + ";" + "Dia" + ";" + "Mês" + ";" + "Ano" + ";" + "Horas" + ";" + "Minutos" + ";" + "Segundos" + '\n'
            linhasAtualizadas.append(linha)
            contador += 1

    with open('DATASET/SDSC 96/SDSC96.csv', 'w') as arquivo:
        arquivo.writelines(linhasAtualizadas)

    print("SDSC 96 -- FEITO")




if __name__ == '__main__':
    ComporFiles = False
    ColumData = False
    ColumData2 = True


    if ComporFiles:
       # name_file = "DATASET/SDSC BLUE/SDSC-BLUE-2000-4.2-cln.csv"
        new_file = "DATASET/SDSC BLUE/SDSC-BLUE-Composto.csv"
        file = "DATASET/SDSC BLUE/SDSC-BLUE-CompostoF.csv"
       # leituraFicheiros(name_file, new_file)
        compor(new_file, file)



    if ColumData2:
        file = "DATASET/NASA/NASA-CompostoF.csv"
        SemanaFileNASA(file)


    if ColumData2:
        file = "DATASET/HPC2N/HPC2N-CompostoF.csv"
        SemanaFileHPCN(file)


    if ColumData2:
        file = "DATASET/SDSC BLUE/SDSC-BLUE-CompostoF.csv"
        SemanaFileSDSCBlue(file)



    if ColumData2:
        file = "DATASET/SDSC 96/SDSC-Par-CompostoF.csv"
        SemanaFileSDSC96(file)

