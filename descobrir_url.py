=import hashlib  # Biblioteca usada para calcular hashes, como MD5

# URL base com partes que precisam ser preenchidas (substituídas pelas combinações geradas)
base_url = "https://forms.layers.education/processo-seletivo-2aae6c3{}c94fcfb415{}be95{}408b9ce91{}e846ed"

def gerar_combinacoes(tamanho, prefixo=""):
    """
    Função recursiva para gerar todas as combinações possíveis de caracteres alfanuméricos
    (letras minúsculas e números) com um tamanho específico.

    :param tamanho: Número de caracteres na combinação atual.
    :param prefixo: Prefixo da combinação que está sendo gerada.
    :yield: Retorna combinações uma por vez.
    """
    if tamanho == 0:  # Se o tamanho da combinação chegou a zero, retorna o prefixo atual
        yield prefixo
    else:
        # Para cada caractere permitido ('a' até 'z' e '0' até '9'), adiciona ao prefixo
        for char in "abcdefghijklmnopqrstuvwxyz0123456789":  
            # Gera combinações recursivamente diminuindo o tamanho
            yield from gerar_combinacoes(tamanho - 1, prefixo + char)

def encontrar_url(md5_alvo, base_url, tamanho_comb):
    """
    Procura a URL que gera o hash MD5 correspondente ao hash fornecido.

    :param md5_alvo: Hash MD5 que estamos tentando encontrar.
    :param base_url: URL base com partes substituíveis ({}).
    :param tamanho_comb: Tamanho das combinações de caracteres a serem testadas.
    :return: A URL que gera o hash MD5 correspondente, ou None se não encontrar.
    """
    # Gera combinações para preencher os 4 espaços '{}' na URL
    for comb1 in gerar_combinacoes(tamanho_comb):  
        for comb2 in gerar_combinacoes(tamanho_comb):  
            for comb3 in gerar_combinacoes(tamanho_comb):  
                for comb4 in gerar_combinacoes(tamanho_comb):  
                    # Preenche os espaços '{}' da URL com as combinações atuais
                    url_tentativa = base_url.format(comb1, comb2, comb3, comb4)
                    
                    # Calcula o hash MD5 da URL gerada
                    md5_hash = hashlib.md5(url_tentativa.encode()).hexdigest()
                    
                    # Compara o hash calculado com o hash alvo
                    if md5_hash == md5_alvo:
                        return url_tentativa  # Retorna a URL correspondente se os hashes forem iguais
    return None  # Retorna None se não encontrar correspondência

# Hash MD5 que queremos encontrar
md5_alvo = "6cc89c7e40021e6c2cb4fb1543c0ba04"

# Tamanho inicial das combinações a testar (1 caractere por padrão neste exemplo)
tamanho_comb = 1  

# Chama a função para encontrar a URL correspondente ao hash alvo
resultado = encontrar_url(md5_alvo, base_url, tamanho_comb)
if resultado:
    print(f"URL descoberta: {resultado}")  # Mostra a URL se encontrada
else:
    print("Nenhuma correspondência encontrada.")  # Mensagem caso não encontre a URL
