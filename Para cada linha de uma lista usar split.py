'''Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt'''

fname = input("Enter file name: ")
fh = open(fname)
rd = fh.read()

#Separar as palavras do arquivo
separado = rd.split()

#Criar uma lista
lst = list()

#Para cada palavra separada do texto, adiociona-la a lista que estava vazia
for word in separado:
    if word not in lst:
        lst.append(word)
        
#Aplicar a função sort para deixar as palavras da lista em ordem alfabetica        
lst.sort()     
print(lst)
