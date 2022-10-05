import turtle

turtle.shape("turtle")
turtle.penup()
turtle.goto(-100,0) # bergerak menuju koordinat awal pada (-100,0)

# membuat persegi
turtle.pendown()
turtle.color("yellow") # mengubah warna menjadi kuning
turtle.begin_fill() # mengaktifkan mode mewarnai gambar
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

# memindahkan turtle
turtle.penup()
turtle.left(90)
turtle.forward(180)

# membuat lingkaran
turtle.pendown()
turtle.color("green") # mengubah warna menjadi hijau
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# berhenti menggambar dan menyembunyikan ikon turtle
turtle.hideturtle()
turtle.exitonclick()