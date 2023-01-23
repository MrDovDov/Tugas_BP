# Contoh dari function
def nama(panggil):
    print("Hello, " + panggil + "!")
nama("Dian") 

# Contoh dari recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))