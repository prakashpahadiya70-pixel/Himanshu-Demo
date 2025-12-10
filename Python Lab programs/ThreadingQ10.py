import threading
lock = threading.RLock()
def factorial(n):
    lock.acquire()
    try:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print(f"Factorial of {n} = {fact}")
    finally:
        lock.release()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
t1 = threading.Thread(target=factorial, args=(num1,))
t2 = threading.Thread(target=factorial, args=(num2,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Both factorial operations completed successfully!")