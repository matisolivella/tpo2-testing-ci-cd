from app.calculadora import dividir

def main():
    print("=== Calculadora de División ===")
    
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()