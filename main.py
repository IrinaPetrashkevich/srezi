print("Введите стороны:")
a = float(input("a = ")) #первая сторона
b = float(input("b = ")) #вторая сторона
c = float(input("c = ")) #третья сторона

if a + b > c and a + c > b and b + c > a: # сравниваем суммы всех пар сторон с оставшейся третьей стороной
    print("Треугольник существует!")
else:
    print("Треугольник не существует!")

