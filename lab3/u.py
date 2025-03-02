def ounces(grams):
    """Конвертирует граммы в унции"""
    return grams / 28.3495231

def is_prime(num):
    """Проверяет, является ли число простым"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

