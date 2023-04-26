'''
Para criar um neurônio capaz de aprender com textos, precisamos definir uma forma de representar as palavras como
entradas numéricas para o neurônio. Uma possível abordagem é usar a técnica de vetorização de texto,
que transforma cada palavra em um vetor de números.

Aqui está um exemplo de como podemos modificar a classe Neuronio para incluir essa funcionalidade:
'''

from tika import parser
import  random
import  numpy as np
from sklearn.feature_extraction.text import CountVectorizer
class Neuronio:
    def __init__(self, num_entradas):
        # atributos do neurônio
        self.pesos = [random.uniform(-1, 1) for _ in range(num_entradas)]
        self.bias = random.uniform(-1, 1)

    def ativacao(self, entradas):
        # calcula a soma ponderada das entradas e pesos + bias
        somatorio = sum(
            [x * w for x, w in zip(entradas, self.pesos)]) + self.bias
        # aplica função de ativação (sigmoid)
        resultado = 1 / (1 + pow(2.71828, -somatorio))
        return resultado


class NeuronioTexto:
    def __init__(self, tam_vetorizacao):
        # atributos do neurônio
        self.pesos = np.array([random.uniform(-1, 1)
                              for _ in range(tam_vetorizacao)])
        self.bias = random.uniform(-1, 1)

    def ativacao(self, vetor_texto):
        # calcula a soma ponderada do vetor de texto e pesos + bias
        somatorio = np.dot(vetor_texto, self.pesos) + self.bias
        # aplica função de ativação (sigmoid)
        resultado = 1 / (1 + pow(2.71828, -somatorio))
        return resultado

    def treinar(self, vetor_texto, saida_desejada, taxa_aprendizado):
        # faz a predição para o vetor de entrada
        predicao = self.ativacao(vetor_texto)
        # calcula o erro
        erro = saida_desejada - predicao
        # atualiza os pesos e o bias
        self.pesos += taxa_aprendizado * erro * vetor_texto
        self.bias += taxa_aprendizado * erro

'''
Aqui está um exemplo de como podemos modificar a classe Neuronio para incluir essa funcionalidade:

'''

# ######################################### Saida do neurônio #################################################################
raw = parser.from_file('livro.pdf')
#print(raw['content'])

# criando um objeto NeuronioTexto com um vetor de tamanho 100
neuronio_texto = NeuronioTexto(100)

# definindo um texto
texto = raw['content']

# vetorizando o texto
vetorizador = CountVectorizer(max_features=100)
vetor_texto = vetorizador.fit_transform([texto]).toarray()
#print(vetor_texto[0][0])
# obtendo a saída do neurônio para o vetor de texto dado
saida_texto = neuronio_texto.ativacao(vetor_texto[0][0])

print("Vetor de saida do neurônio :")
print(saida_texto)

for vetor in vetor_texto:
    saida_texto = neuronio_texto.ativacao(vetor)
    saida_int = int(round(saida_texto))
    print("\n\nSaida do neurônio em inteiro :"+str(saida_int))

########################################### Treinamento do neurõnio #############################################################################

raw = parser.from_file('livro.pdf')
texto = raw['content']

# definir conjunto de dados de treinamento com saídas desejadas
dados_treinamento = [
    {'texto': 'exemplo de texto positivo', 'saida': 1},
    {'texto': 'exemplo de texto negativo', 'saida': 0},
    # adicionar mais textos com suas respectivas classificações
]

# vetorizar os textos do conjunto de dados de treinamento
vetorizador = CountVectorizer(max_features=100)
matriz_treinamento = vetorizador.fit_transform(
    [dado['texto'] for dado in dados_treinamento]).toarray()

# criar objeto NeuronioTexto com tamanho de vetorização igual ao número de colunas da matriz
neuronio_texto = NeuronioTexto(matriz_treinamento.shape[1])

# treinar o neurônio com o conjunto de dados de treinamento
for i, dado in enumerate(dados_treinamento):
    vetor_texto = matriz_treinamento[i]
    saida_desejada = dado['saida']
    neuronio_texto.treinar(vetor_texto, saida_desejada, taxa_aprendizado=2)

# obter saída do neurônio para o vetor de texto dado
saida_texto = neuronio_texto.ativacao(vetor_texto)

print("Vetor de saída do neurônio:")
print(saida_texto)
