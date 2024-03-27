import flet as ft
from flet.matplotlib_chart import MatplotlibChart as mplt
import matplotlib.pyplot as plt

# Resolvendo o erro -> "UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail. fonte: stackoverflow.com
import matplotlib
matplotlib.use('agg')

def main(page: ft.Page):
    page.title = 'Graficos'

    txt1 = ft.Text('Grade Curricular - Fisisca 2024')

    alunos = ['Ana', 'Carlos', 'David', 'Karine', 'Daniel',
              'Carmen', 'Danilo', 'Angela', 'Jhon', 'Vanessa']
    
    notas = [78, 73, 96, 88, 79, 80, 74, 90, 89, 91]

    fig, ax = plt.subplots()
    ax.bar(alunos, notas)
    ax.set_title('Física - 2024')
    ax.set_ylabel('Notas')

    page.add(txt1, mplt(fig, expand=True))

ft.app(target=main)    