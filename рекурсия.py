# def matryoshka(n):  # n - глубина рекурсии
#     if n == 1:  # крайний случай
#         print("Матрешечка")
#     else:
#         print("Верх матрешки n=", n)
#         matryoshka(n-1)     # рекурсия
#         print("Низ матрешки n=", n)

import graphics as gr

window = gr.GraphWin("Russian game", 600, 600)
alpha = .2

def fractal_rectangle(A, B, C, D, deep=10): # deep - глубина
    if deep < 1:                            # крайний случай
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window) # *A разворачивает кортеж на отдельные значения X и Y
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 10)
window.getMouse() # Pause to view result