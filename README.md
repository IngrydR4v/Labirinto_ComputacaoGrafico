# Computação Gráfica - Labirinto 🖼️

<f2 align = "left"> **O seguinte projeto possui o objetivo de construir um labirinto por meio de conhecimentos com fractal Hilbert.**</f2> 
<img src="labirinto.gif" align="center"/>
<hr> </hr>

# Importando o módulo Turtle
<p>Para utilizar um módulo no Python, utilizamos o comando import (importar) seguido do nome do módulo que queremos importar. Após a importação, já podemos utilizar todos os objetos e funções que o módulo disponibiliza.<p>   
  
    import turtle
<p>Para definir uma função para desenhar a curva de Hilbert recursivamente, use:<p>   
  
    def hilbert(turtle, order, size, angle):
    if order == 0:
        return
    else:
        turtle.right(angle)
        hilbert(turtle, order-1, size, -angle)
        turtle.forward(size)
        turtle.left(angle)
        hilbert(turtle, order-1, size, angle)
        turtle.forward(size)
        hilbert(turtle, order-1, size, angle)
        turtle.left(angle)
        turtle.forward(size)
        hilbert(turtle, order-1, size, -angle)
        turtle.right(angle)
  
<p> Cria uma janela gráfica de tartaruga: </p>

    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Hilbert Fractal")

<p> Crie agora, uma tartaruga e defina suas propriedades:</p>
  
    tess = turtle.Turtle()
    tess.speed(0)
    tess.penup()
    tess.goto(-200, 0)
    tess.pendown()
    tess.pensize(2)

<p> Chame a função Hilbert para desenhar o fractal:</p>

    hilbert(tess, 5, 10, 90)

<p> Feche a janela de gráficos da tartaruga ao clicar:</p>

    turtle.done()
