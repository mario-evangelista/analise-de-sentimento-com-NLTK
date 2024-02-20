# Análise de Sentimento com NLTK

Este repositório contém um código Python para análise de sentimentos usando a biblioteca NLTK (Natural Language Toolkit).

## Descrição
O código realiza a análise de sentimentos em um conjunto de sentenças fornecido em um arquivo de texto. Ele utiliza o VADER (Valence Aware Dictionary and sEntiment Reasoner), que é um lexicon e uma ferramenta de análise de sentimentos que é especialmente bem ajustada para análise de texto de mídia social.

## Como Usar
1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale a biblioteca NLTK usando `pip install nltk`.
3. Execute o seguinte comando para baixar o lexicon VADER:
    ```bash
    nltk.download('vader_lexicon')
    ```
4. Execute o script Python fornecido, garantindo que você tem um arquivo de texto chamado `sentencas.txt` no diretório `inputs/`.
5. O script imprimirá o score de sentimento das sentenças contidas no arquivo.

## Análise de Sentimento
Para analisar o sentimento de uma sentença, utilizamos a classe SentimentIntensityAnalyzer que nos dá uma pontuação/score de intensidade de sentimento de determinadas sentenças.
Primeiro, vamos importar essa classe e instanciá-la:
```ruby
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
```
A classe SentimentIntensityAnalyzer() possui o método polarity_scores() que gera as pontuações/scores.

Vejamos um exemplo:
```ruby
score_de_sentimento = sia.polarity_scores(texto)
print(score_de_sentimento)
{'neg': 0.032, 'neu': 0.904, 'pos': 0.064, 'compound': 0.3164}
```
Print / Saída:
```ruby
{'neg': 0.032, 'neu': 0.904, 'pos': 0.064, 'compound': 0.3164}
```
As pontuações exibidas tem um valor de -1 a 1, do tipo float, para as chaves neg (sentimento negativo), neu (sentimento neutro), pos (sentimento positivo) e compound (sentimento dos três anteriores combinados). Esta pontuação é exatamente o cálculo da valência emocional. A pontuação composta de  "0.3164" indica um resultado acima de 0, portanto o conjunto de senteças denotam um sentimento positivo. 

## Requisitos
- Python
- NLTK

## Autor
Este código foi escrito por [Mário Evangelista/Autor](https://github.com/mario-evangelista).

Sinta-se à vontade para contribuir ou fazer sugestões de melhorias.
