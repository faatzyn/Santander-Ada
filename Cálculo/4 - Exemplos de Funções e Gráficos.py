import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
# Função constante
# f(x) = C -> V(t) = 20 -> valor final não varia de acordo com o tempo
plt.title("Função constante, linear") # reta horizontal
x = np.linspace(-10,10,10000)
y = 20*np.ones(x.shape)
# plt.plot(x, y, label='Constante')

# Função Linear
# f(x) = ax + b -> valor final varia de acordo com 'x'
# P(d) = 5 + 2d -> Função Linear -> Reta
y2 = 5 + 2*x
# plt.plot(x,y2, label='Linear')

# Função Quadrática
# f(x) = ax² +bx + c -> adiciona um termo quadrático -> polinômio de grau 2
# f(x) = 5 - 5t² 
y3 = 5-5*x**2
# plt.plot(x,y3, label='Quadrática')

# Função polinômial de grau n
# f(x) = an x^n + an1 x^n-1 + ..... a2x² + a1x + a0
# n = 2 -> a2x² + a1x + a0
# n = 1 -> a1x + a0
# n = 3 -> a3x³ + a2x² + a1x + a0
# f(x) = x³ + 10x² + 5x
y4 = x**3 + 10*x**2 + 5*x
# plt.plot(x,y4, label='Função de Grau 3')

# Funções Racionais
# f(x) = P(x) / Q(x) -> uma função que é igual uma função sobre outra função
# Exemplo -> f(x) = 1/x
# Energia Potencial de Leonard Jones, energia entre duas moléculas
# V(r) = A / r^12 - B/r^6 onde A e B são constantes
# f(x) = 5^-15 * ((1/x)^12 - (9.6/x)**6)
x = np.linspace(0.1,0.5,10000)
y5 = (5**-15) * ((1/x)**12 - (9.6/x)**6)
# plt.plot(x,y5, label='Racionail')

# Funções Trigonométricas
# f(x) = sin(x)
# f(x) = cos(x)
# f(x) = tg(x) = sin(x) / cos(x)
x = np.linspace(-10,10,10000)
y6 = np.sin(x)
# plt.plot(x,y6, label='Trigonométricas - Seno')
y7 = np.cos(x)
# plt.plot(x,y7, label='Trigonométricas - Cos')

# Funções exponenciais
# f(x) = ce^bx
# N(t) = N.e^rt
x = np.linspace(-10,10,10000)
y8 = np.exp(x)
# plt.plot(x,y8, label='Exponencial')

# Funções Sigmóide -> Ciência de Dados -> Redes Neurais, tem limite de 0 e 1; não ultrapassa esses valores
# Sigma(x) -> f(x) = 1 / 1+e^-x
x = np.linspace(-10,10,10000)
y9 = 1 / (1+np.exp(-x))
plt.plot(x, y9, label='Sigmóide')

plt.grid(True)
plt.legend()
plt.show()