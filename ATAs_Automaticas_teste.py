#Biblioteca
from textblob import TextBlob 

#Função para traduzir polaridade e subjectividade
def analyze_sentiment(polarity, subjectivity):
    if polarity > 0:
        sentiment = "positivo"
    elif polarity < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutro"
    
    if subjectivity > 0.5:
        subjectivity_desc = "opinativo"
    else:
        subjectivity_desc = "factual"
        
    return f"O texto é {sentiment} e {subjectivity_desc}. Sendo: \n polaridade =  {polarity}; \n subjetividade = {subjectivity}."


#Lendo o arquivo 'texto_limpo.txt'
file_path = 'texto_limpo.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Criando um objeto TextBlob
blob = TextBlob(text_content)

# Extração de SUBSTANTIVOS para identificar possíveis tópicos ou assuntos
nouns = blob.noun_phrases
print("Possíveis Tópicos ou Assuntos:")
print(nouns)

# ANÁLISE DE SENTIMENTOS para entender o tom geral
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Obtendo polaridade e subjetividade
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

# Interpretando os resultados, passando pela função
result = analyze_sentiment(polarity, subjectivity)
print("Análise de Sentimento:")
print(result)


#--------------------------- teacher class -------------------------------------
# Retorno: Polaridade: 0.023529411764705875, Subjetividade: 0.5235294117647059
# -- Polaridade --
# Valores Positivos: Indicam um sentimento positivo.
# Valores Negativos: Indicam um sentimento negativo.
# Valores Próximos de Zero: Indicam neutralidade.

# -- Subjetividade --
# Valores Próximos de 1: Indicam que o texto é muito opinativo.
# Valores Próximos de 0: Indicam que o texto é muito factual.
#--------------------------------------------------------------------------------"""

# TOKENIZAÇÃO para dividir o texto em sentenças, o que pode facilitar a análise subsequente
sentences = blob.sentences
print("Sentenças:")
for i, sentence in enumerate(sentences):
    print(f"{i+1}. {sentence}")


# Construindo a Ata
ata = f"""
ATA DA REUNIÃO

Data e Hora: [Data e Hora a ser preenchida]
Local: [Local a ser preenchido]
Participantes: [Participantes a serem preenchidos]

Tópicos Discutidos:
{', '.join(nouns)}

Resumo da Análise de Sentimento:
{result}

Decisões Tomadas:
[Decisões Tomadas a serem preenchidas]

Ações Futuras:
[Ações Futuras a serem preenchidas]

Assinaturas:
[Assinaturas a serem preenchidas]
"""

# Exibir a Ata
print("\n\n===== ATA DA REUNIÃO =====")
print(ata)