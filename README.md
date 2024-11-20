# Desafio Inicial - LAYER EDUCATION

Este projeto foi desenvolvido para resolver um desafio de força bruta em que é necessário descobrir combinações ocultas em uma URL, de forma que a URL completa gere um hash MD5 específico. O desafio envolve conhecimento de hashing, programação e geração de combinações.

# **Desafio de Descoberta de URL por Hash MD5**

Este projeto foi desenvolvido para resolver um desafio de força bruta em que é necessário descobrir combinações ocultas em uma URL, de forma que a URL completa gere um hash MD5 específico. O desafio envolve conhecimento de hashing, programação e geração de combinações.

## **Descrição**

Dado:
- Uma URL base com partes substituíveis (marcadas por `{}` ou `*`).
- Um hash MD5 específico fornecido.

Objetivo:
- Descobrir quais combinações de caracteres (alfanuméricos) substituem os placeholders na URL base, de forma que a URL completa gere o hash MD5 fornecido.

Exemplo de URL base:
```
https://forms.layers.education/processo-seletivo-2aae6c3*c94fcfb415*be95*408b9ce91*e846ed
```

Hash MD5 fornecido:
```
6cc89c7e40021e6c2cb4fb1543c0ba04
```

Resultado esperado:
- Uma URL válida onde o hash MD5 coincide com o fornecido.

## **Como Funciona**

1. O script gera combinações possíveis de caracteres (`a-z` e `0-9`) para preencher os espaços marcados na URL base.
2. Calcula o hash MD5 da URL gerada.
3. Compara o hash calculado com o hash fornecido.
4. Retorna a URL correta assim que encontra uma correspondência.

## **Requisitos**

- Python 3.6 ou superior
- Biblioteca `hashlib` (já incluída na instalação padrão do Python)

## **Como Executar**

1. Certifique-se de que o Python está instalado no seu computador.
   - [Download Python](https://www.python.org/)

2. Clone ou baixe este repositório.

3. Abra o terminal ou prompt de comando e navegue até o diretório do projeto.

4. Execute o script com o comando:
   ```bash
   python descobrir_url.py
   ```

5. O script exibirá a URL descoberta, se encontrada:
   ```
   URL descoberta: https://forms.layers.education/processo-seletivo-2aae6c3abc...e846ed
   ```
   
## **Personalização**

- **Modifique o tamanho das combinações:** 
  Edite a variável `tamanho_comb` no código para ajustar o número de caracteres nos placeholders da URL.
  ```python
  tamanho_comb = 1  # Número de caracteres para cada placeholder
  ```

- **Ajuste os caracteres possíveis:** 
  Por padrão, o script testa `a-z` e `0-9`. Para adicionar mais caracteres, edite:
  ```python
  for char in "abcdefghijklmnopqrstuvwxyz0123456789":
  ```

## **Limitações**

- O algoritmo utiliza força bruta, o que pode levar tempo dependendo do número de combinações.
- Para espaços de busca muito grandes, considere técnicas de otimização (como paralelismo ou redução do espaço de busca).

## **Estrutura do Código**

- **`base_url`**: Contém a URL base com placeholders `{}`.
- **`gerar_combinacoes`**: Função recursiva que gera todas as combinações possíveis.
- **`encontrar_url`**: Testa cada combinação, substitui na URL e verifica o hash MD5.
  
