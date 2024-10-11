def process_single_string(s):
    digits = [int(ch) for ch in s if ch.isdigit()]
    
    if digits:
        suma = sum(digits)
        product = 1
        for d in digits:
            product *= d
        return suma, product
    else:
        return 0, 0

s = input("Введіть рядок символів: ")

suma, product = process_single_string(s)
print(f"Сума цифр: {suma}")
print(f"Добуток цифр: {product}")
