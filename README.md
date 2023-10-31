# Questão 4 - encryptThis

 - Disciplina: Análise, Projeto e Desenvolvimento Ágil
 - Professor: Diogo Winck
 - Integrantes do Projeto: Beatriz Mayorka de Aguiar e Guilherme Victor Borges Pereira

# Criptografando Mensagens com Python: A Magia da Função encryptThis

A programação frequentemente nos permite explorar conceitos complexos de maneira prática e divertida. Neste projeto, iremos mergulhar em um desafio interessante: criar uma função chamada encryptThis(message) que criptografa uma mensagem de texto de acordo com regras específicas. A ideia é que cada palavra em uma mensagem seja transformada de acordo com um conjunto de instruções. Esta função é uma excelente oportunidade para aprender sobre manipulação de strings, operações de caracteres e, claro, a criação de testes unitários para garantir sua precisão.

## Implementando a Função encryptThis em Python

A função encryptThis recebe uma mensagem que é uma string contendo palavras separadas por espaços e a criptografa de acordo com as seguintes regras:

1. O primeiro caractere de cada palavra é convertido para o seu código ASCII.
2. O segundo caractere da palavra é trocado com o último caractere.

Por exemplo, a palavra "Hello" seria criptografada como "72olle" de acordo com essas regras.

## Lógica por Trás da Criptografia

A primeira etapa para implementar essa função é dividir a mensagem em palavras. Isso pode ser feito facilmente em Python usando o método split(). Em seguida, percorremos cada palavra e aplicamos as transformações especificadas. A lógica básica é a seguinte:

1. Obtenha o código ASCII do primeiro caractere da palavra.
2. Troque o segundo e o último caractere da palavra.
3. Concatene o código ASCII com a palavra modificada.

Isso nos dará a palavra criptografada. Repita esse processo para todas as palavras na mensagem, mantendo a estrutura original das palavras separadas por espaços.

## Testando a Função

Uma parte fundamental da programação é garantir que sua função funcione corretamente. Para isso, criaremos pelo menos quatro testes unitários para a função encryptThis. Cada teste abordará diferentes cenários, incluindo palavras de diferentes comprimentos e mensagens com várias palavras. 

Por exemplo, um teste unitário pode ser:

```ruby
python
def test_encryptThis():
    assert encryptThis("Hello") == '72olle'  # Teste para palavra de cinco letras
```
