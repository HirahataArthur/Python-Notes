def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new) ##substitui old por new, respectivamente (em cada elemento), coordenada 00 substituida por 01
    return text
 
def main():
    # Entrada da frase e aplicação da codificação
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase_title = phrase.title()  # Primeira letra de cada palavra em maiúscula
 
    # Dividir a frase em palavras
    words = phrase.split()
 
    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]
 
    # Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Title: ", phrase_title)
    print("Coded:", coded_phrase)
 
if __name__ == "__main__":
    main()