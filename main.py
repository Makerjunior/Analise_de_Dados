# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Pandas Exemplos

import  pandas as pd

pd.Series(data=5)

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
pd.Series(lista_nomes) # Cria uma Series com uma lista de nomes
dados = {
'nome1': 'Howard',
'nome2': 'Ian',
'nome3': 'Peter',
'nome4': 'Jonah',
'nome5': 'Kellie',
}
pd.Series(dados) # Cria uma Series com um dicionári


  
print(dados)