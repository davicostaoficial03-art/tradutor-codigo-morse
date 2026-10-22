# Importa a biblioteca winsound, disponível no Windows,
# utilizada para reproduzir sons com uma frequência e duração específicas.
import winsound

# Importa a biblioteca time, utilizada para criar pausas na execução.
import time


# Cria um dicionário que relaciona cada letra do alfabeto
# e cada algarismo ao seu respectivo código Morse.
# O ponto (.) representa um sinal curto, e o traço (-) representa
# um sinal longo.
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}


# Define a frequência dos sinais sonoros em hertz (Hz).
# Quanto maior a frequência, mais agudo será o som.
FREQ = 700

# Define a duração de um ponto em milissegundos.
DOT = 100

# Define a duração de um traço como três vezes a duração de um ponto.
DASH = DOT * 3

# Define a pausa entre os sinais de letras diferentes, em segundos.
PAUSE_LETTER = 0.3

# Define a pausa entre palavras diferentes, em segundos.
PAUSE_WORD = 0.7


# Define a função responsável por reproduzir os sinais sonoros
# correspondentes a uma sequência de código Morse.
# O parâmetro "codigo" recebe uma sequência de pontos e traços.
def tocar(codigo):

    # Percorre cada símbolo da sequência recebida.
    for s in codigo:

        # Verifica se o símbolo atual é um ponto.
        if s == '.':

            # Reproduz um som de frequência FREQ durante DOT milissegundos.
            winsound.Beep(FREQ, DOT)

        # Verifica se o símbolo atual é um traço.
        elif s == '-':

            # Reproduz um som três vezes mais longo que o ponto.
            winsound.Beep(FREQ, DASH)

        # Aguarda 0,1 segundo antes de processar o próximo símbolo.
        # Essa pausa separa os sinais sonoros.
        time.sleep(0.1)


# Define a função responsável por converter um texto em código Morse.
# O parâmetro "texto" recebe a mensagem digitada pelo usuário.
def texto_para_morse(texto):

    # Converte todas as letras do texto para maiúsculas.
    # Isso permite utilizar as chaves do dicionário MORSE,
    # que estão representadas em letras maiúsculas.
    texto = texto.upper()

    # Cria uma lista vazia para armazenar os códigos Morse
    # correspondentes aos caracteres da mensagem.
    morse = []

    # Percorre cada caractere do texto recebido.
    for c in texto:

        # Verifica se o caractere existe como chave no dicionário.
        if c in MORSE:

            # Adiciona à lista o código Morse correspondente
            # ao caractere encontrado.
            morse.append(MORSE[c])

        # Verifica se o caractere é um espaço entre palavras.
        elif c == ' ':

            # Adiciona uma barra para representar a separação
            # entre palavras na mensagem codificada.
            morse.append('/')

        # Caracteres que não estão no dicionário e não são espaços
        # são ignorados pelo código original.

    # Junta os elementos da lista em uma única string.
    # O espaço entre aspas separa os códigos de letras diferentes.
    # Por exemplo, ['...', '---'] torna-se '... ---'.
    return ' '.join(morse)


# Inicia um laço infinito para permitir que o usuário
# converta e reproduza várias mensagens.
while True:

    # Solicita uma mensagem ao usuário.
    # Se ele pressionar Enter sem digitar nada, a mensagem será vazia.
    mensagem = input(
        "Digite uma mensagem ou aperte enter pra finalizar : "
    )

    # Verifica se o usuário enviou uma mensagem vazia.
    if not mensagem:

        # Interrompe o laço e encerra o programa.
        break

    # Converte a mensagem digitada para código Morse
    # chamando a função definida anteriormente.
    codigo = texto_para_morse(mensagem)

    # Exibe uma linha em branco e o título da seção.
    print("\nCódigo Morse:")

    # Exibe a sequência de pontos, traços e barras gerada.
    print(codigo)

    # Informa que a reprodução dos sinais sonoros será iniciada.
    print("aguarde...")

    # Divide o código Morse pelas barras, separando as palavras.
    # Cada elemento de "codigo.split('/')" representa uma parte
    # da mensagem correspondente a uma palavra.
    for palavra in codigo.split('/'):

        # Remove espaços externos da palavra codificada
        # e separa os códigos das letras pelos espaços.
        # Cada elemento de "palavra.strip().split()" corresponde
        # ao código Morse de uma letra.
        for letra in palavra.strip().split():

            # Reproduz o som correspondente ao código Morse da letra.
            tocar(letra)

            # Aguarda o intervalo definido entre letras.
            time.sleep(PAUSE_LETTER)

        # Depois de reproduzir todos os códigos da palavra,
        # aguarda o intervalo definido entre palavras.
        time.sleep(PAUSE_WORD)
