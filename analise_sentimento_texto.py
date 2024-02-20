import nltk  # Importa a biblioteca NLTK (Natural Language Toolkit) para análise de linguagem natural
from nltk.sentiment import SentimentIntensityAnalyzer  # Importa a classe SentimentIntensityAnalyzer para análise de sentimentos

# necessário baixar apenas na primeira execução
nltk.download('vader_lexicon')  # Baixa o vader_lexicon VADER (Valence Aware Dictionary and sEntiment Reasoner) apenas na primeira execução

# Abre o arquivo "sentencas.txt" para leitura ('r' indica leitura)
with open("inputs/sentencas.txt", "r") as arquivo:
    # Lê todas as linhas do arquivo e armazena em uma lista chamada 'sentencas'
    sentencas = arquivo.readlines()
    # Une todas as strings da lista 'sentencas' em uma única string, separando-as por espaços
    texto = ' '.join(sentencas)

# Inicializa o analisador de sentimentos da NLTK
sia = SentimentIntensityAnalyzer()

# Calcula o score de sentimento do texto usando o analisador de sentimentos
score_de_sentimento = sia.polarity_scores(texto)

print(score_de_sentimento)  # Imprime o score de sentimento