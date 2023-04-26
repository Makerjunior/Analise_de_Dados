from tika import parser
import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import numpy as np
from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
import io

# Inicializar o tokenizador GPT-2 medium
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')

# Criar o modelo GPT-2 medium com uma camada de classificação de linguagem no topo
model = TFGPT2LMHeadModel.from_pretrained('gpt2-large')

# Compilar o modelo
model.compile(loss=model.compute_loss, optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5))

# Carregar os dados de treinamento a partir do PDF
with open('livro.pdf', 'rb') as file:
    parsed_pdf = parser.from_file(file)
    text_data = ''
    for page in parsed_pdf.pages:
        text_data += page.extract_text()

# Pré-processar o texto
preprocessed_text = text_data.replace('\n', ' ')

# Tokenizar o texto pré-processado
tokenized_text = tokenizer.encode(preprocessed_text, return_tensors='tf')

# Criar um tensor de rótulos de máscara de atenção para treinamento
input_ids = tokenized_text[:, :-1].numpy()
labels = np.copy(input_ids)
labels[labels == tokenizer.pad_token_id] = -100

# Preparar os dados de entrada e saída para treinamento
input_ids = input_ids.tolist()[0]
attention_mask = tokenized_text.tolist()[0]

x_train = {'input_ids': np.array([input_ids]), 'attention_mask': np.array([attention_mask])}

labels = labels.tolist()[0]
attention_mask = tokenized_text.tolist()[0]

y_train = {'lm_labels': np.array([labels]), 'attention_mask': np.array([attention_mask])}

# Treinar o modelo
model.fit(x=x_train, y=y_train, epochs=10, batch_size=32)

# Loop para perguntar e responder
while True:
    # Receber a entrada do usuário
    question = input("Digite sua pergunta: ")

    # Concatenar a pergunta com um separador
    input_text = question + ' [SEP]'

    # Tokenizar a entrada concatenada
    tokenized_input = tokenizer.encode(input_text, return_tensors='tf')
    input_dict = {'input_ids': tokenized_input, 'attention_mask': tf.ones_like(tokenized_input)}

    # Gerar a resposta a partir dos tokens gerados pelo modelo
    output_tokens = model.generate(tokenized_input, max_length=1000, do_sample=True, num_return_sequences=1)
    output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

    # Imprimir a resposta gerada pelo modelo
    print(output_text)