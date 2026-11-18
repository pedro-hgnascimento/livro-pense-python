def is_triangle(a, b, c):
    """Check if three sides can form a triangle."""
    if(a + b > c and a + c > b and b + c > a):
        print("Yes")
    else:
        print("No")

def main():
    a = int(input("Digite o valor do lado a: "))
    b = int(input("Digite o valor do lado b: "))
    c = int(input("Digite o valor do lado c: "))

    print("Os lados fornecidos podem formar um triângulo?")
    is_triangle(a, b, c)

main()