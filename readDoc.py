
#Leitura de Arquivos em Python
'''
from tika import parser
raw = parser.from_file('livro.pdf')
print(raw['content'])
'''
# import parser object from tike


from tika import parser
import re
# opening pdf file
parsed_pdf = parser.from_file("livro.pdf")
# saving content of pdf
# you can also bring text only, by parsed_pdf['text']
# parsed_pdf['content'] returns string
data = parsed_pdf['content']
# Printing of content
# palavra a ser buscada
regex_palavras = re.compile(r'\b(\w+)\b')
# palavra a ser buscada
#busca = input('Digite a palavra desejada: ')
#print(data.find(busca))




'''
# <class 'str'>
print(type(data))
# import parser object from tike
print(" METADADOS ")
print(parsed_pdf['metadata'])
# <class 'dict'>
print(type(parsed_pdf['metadata']))
print(parsed_pdf.keys())
print(parsed_pdf['status'],type(parsed_pdf['status'] ))
'''
texto = data

def encontrar_frase(texto, palavra_chave):
    inicio_frase = texto.find(".", texto.find(palavra_chave)) + 1
    fim_frase = texto.find(".", inicio_frase)
    return texto[inicio_frase:fim_frase].strip()


palavra_chave = "Você"
frase_encontrada = encontrar_frase(texto, palavra_chave)
print(frase_encontrada)


