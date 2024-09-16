import math

def variant_6_1(x, a, k):
    b = math.sin(math.radians(20))
    return x**3 * (math.tan(x + b))**2 + 0.25*a / (k * math.sqrt(abs(x - b)))

def variant_6_2(b, x, a):
    return (b*x**2 - a) / (math.exp(a*x) - 1) + 0.1 + math.log2(4)

def variant_7_1(k, x, z, d):
    return math.log(k*x) + (1 - 0.5*k) / (4 * math.pow(abs(d*z**3 - 2), 1/3)) - 0.025 + d * math.log(3*x, 3)

def variant_7_2(x):
    phi = math.radians(28)
    return (math.sin(x + phi)**(1/3) + math.cos(x)) / (math.pi*x + 4.15 * math.pow(x**(1/4), math.exp(abs(x))))

x_val = int(input("x --> "))
a_val = int(input("a --> "))
k_val = int(input("k --> "))
b_val = int(input("b --> "))
print("\nВариант 6:")
print(f"1) S = {variant_6_1(x_val, a_val, k_val)}")
print(f"2) Q = {variant_6_2(b_val, x_val, a_val)}")

print("\nВариант 7:")
print(f"1) a = {variant_7_1(k_val, x_val, 1, 1)}")
print(f"2) y = {variant_7_2(x_val)}")