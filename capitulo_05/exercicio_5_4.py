# Analisando a saída de um programa
def recurse(n, s):
    """Calcula a soma de n números inteiros positivos de forma recursiva."""
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)

recurse(3, 0)
recurse(5, 0)

# Testando com (-1, 0): Achei que o resultado seria 0, mas o programa entra em loop infinito. 
# Isso acontece porque a função não tem uma condição de parada para n < 0, 
# então ela continua chamando a si mesma indefinidamente.

# recurse(-1, 0)