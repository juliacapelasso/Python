''' Write a program that prompts for a file name, then opens that file and reads through the file, 
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
readfile = fh.read()
#Separar as palavras do texto
conversion1 = readfile.rstrip()
#Deixar as palavras já separadas em letra MAIÚSCULA
conversion2 = conversion1.upper()
print(conversion2)