#Biblioteca
from textblob import TextBlob 

#Lendo o arquivo 'texto_limpo.txt'
file_path = 'texto_limpo.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Criando um objeto TextBlob
blob = TextBlob(text_content)

# Extração de Substantivos para identificar possíveis tópicos ou assuntos
nouns = blob.noun_phrases
print("Possíveis Tópicos ou Assuntos:")
print(nouns)

# Análise de Sentimento para entender o tom geral
sentiment = blob.sentiment
print("Análise de Sentimento:")
print(f"Polaridade: {sentiment.polarity}, Subjetividade: {sentiment.subjectivity}")