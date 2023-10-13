def leituraFicheiros(ficheiro,new_file):
    f_copy = open(new_file, "w")
    contador = 1
    with open(ficheiro, "r") as f:

        for j in f.readlines():
            if( contador <= 31):
                contador +=1
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



def compor(name_file,final):
    with open(name_file, 'r') as arquivo_entrada, open(final, 'w') as arquivo_saida:
        for linha in arquivo_entrada:
            # Remove o ponto e vírgula no início de cada linha
            linha_modificada = linha.lstrip(';')
            arquivo_saida.write(linha_modificada)


if __name__ == '__main__':

    name_file = "DATASET/HPC2N/HPC2N-2002-2.2-cln.csv"
    new_file = "DATASET/HPC2N/HPC2N-Composto.csv"
    file = "DATASET/HPC2N/HPC2N-CompostoF.csv"
    leituraFicheiros(name_file,new_file)
    compor(new_file,file)
