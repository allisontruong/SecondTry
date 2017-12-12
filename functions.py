def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
        return
    print("Odd")

if __name__ == "__main__":
    # Test
    even_or_odd(3)
    even_or_odd(4)
    print(__name__)
