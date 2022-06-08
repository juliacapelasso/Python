'''  Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

handle = open("mbox-short.txt")
counts = dict()
lst = list()
count = 0

#Fazer a função verificar cada linha no arquivo mbox-short.txt
#Iniciar uma condicional para selecionar todas as linhas que começam com a palavra "From"
#Remover os espaços em branco na frase utilizando o rstrip() e a função split() para separar palavra por palavra 
#Selecionar a 6ª palavra de cada uma dessas linhas
#Separar a palavra desejada dos dois pontos que a acompanha
#Juntar a palavra desejada a lista criada 
for line in handle:
    if line.startswith("From "):
        words = line.rstrip().split()
        words = words[5]
        words = words.split(':')
        lst.append(words[0])
                
#Para cada item presente na lista, retornar o valor atual da chave i e do valor na posição 0
#Cada vez que passar por esse loop, somar 1
for i in lst:
    counts[i] = counts.get(i,0) + 1
        
#Para cada chave e cada valor no dicionário counts, ordernar as horas, localizadas na chave (k), em ordem crescente
for k, v in sorted(counts.items()):
    print(k,v)