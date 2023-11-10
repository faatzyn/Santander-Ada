# Limites -> Aplicações

# Função
# f(x) = x²-1 / 2x² -x -1 -> função racional (f(x) = h(x) / g(x))

# olhando para a função g(x) - > 2x² -x - 1, onde a = 2, b = -1 e c = 1
# reescrevendo a função ao igual a zero -> 2x² -x -1 = 0 -> (x-1).(2x+1) = 0 //
# Quando igualamos a zero, é possível encontrar as raizes do polinômio.
# nesse caso:
#     (x-1) . (2x+1) -> 
#     para x-1 = 0 -> x = 1
#     para 2x+1 = 0 -> x = -1/2
#     Sendo assim, quando x for 1 ou -1/2, a função é igual a zero.
#     Exemplo:
#         x = 1 -> 2.(1)² - 1.(1) - 1 -> 2.1 - 1.1 - 1 -> 2 - 1 - 1 -> 0 //
#         x = -1/2 -> 2.(-1/2)² - 1.(-1/2) - 1 -> 2.(1/4) - 1.(-1/2) - 1 -> 2/4 + 1/2 - 1 -> 1/2 + 1/2 - 1 -> 0 //

#     Dessa forma, Domínio de (f(x)) -> pertence aos Reais com exceção de 1 e -1/2.
#     D(f) = ℝ \ {1,-1/2}

#     f(x) = x²-1 / 2x² -x -1 -> reescrevendo pela decomposição -> f(x) = x²-1 / (x-1) . (2x+1)
#     decomposição da função h(x) = x²-1 -> (x-1).(x+1)
#     Substituo
#     f(x) = (x-1).(x+1) / (x-1).(2x+1), posso eliminar o (x-1) por ter em cima e em baixo
#     f(x) = (x+1) / (2x+1) -> x+1 / 2x+1

#     resumindo, X pertence aos Reais desde que removemos o valor de 1 e -1/2.
#     X ∈ ℝ \{1, -1/2}

#     Removes esse números pois não temos limites para eles
#     f(1) tem divisão por 0 e f(-1/2) também tem divisão por zero.
#     ∉ f(1) ; f(-1/2)

#     Podemos fazer qual o limite de f(x), quando x tende a uma das raizes
#     lim f(x) com x -> oo

import numpy as np
import matplotlib.pyplot

def f(x):
    return (x**2-1)/(2*x**2-x-1)

# print(f(0.99999))
# print(f(1.00001))

# O Limite da função para quando x tende 1
# lim x=>1 / 2x+1 x->1 = 1+1/2.1+1 = 2/3 // 0.666666666666666

# print(f(-0.49999999))
# print(f(-0.50000001))
# O Limite da função para quando x tende -1/2
# lim x=>-1/2 / 2(x)+1 x->-1/2 = -1/2 + 1 / 2.-1/2 + 1 = 1/2 / -1+1  -> 0.5 / 0  Indefinido
# sendo assim, como vimos com os valores que se aproximam de -1/2, pelo lado positivo ou negativo temos:
# lim f(x) -> x->-1/2+ = +oo
# lim f(x) -> x->-1/2- = -oo
# ou seja, não tem limites para x->-1/2
# ∉ lim f(x) x-> -1/2

# Qual o limite da função para x -> +oo e para x -> -oo
# f(x) = x+1 / 2x+1 ----distributiva---> x (1 + 1/x) / x (2 + 1/x) com isso eu corto os x em evidência
# f(x) = 1 + 1/x / 2 + 1/x ------- como 1/x tende a 0 ---> 1 / 2
# assim: lim f(x) x->+-oo = 1/2
# print(f(1000))
# print(f(-1000))