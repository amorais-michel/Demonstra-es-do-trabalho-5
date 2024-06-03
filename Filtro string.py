#criando variavel para salvar string
str = 'X-DSPAM-Confidence: 0.8475'

#variavel que exibe o endereço da string depois de dois pontos
endereco = str.find(':')
print("endereco antes :", endereco)

#imprimindo e encontrando o endereço depois dos dois pontos
finalstring = str[endereco +1 :]
print(finalstring)

#convertendo

valorconvertido = float(finalstring)
print(valorconvertido * 2)