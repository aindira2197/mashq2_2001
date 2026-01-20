karta = input("Karta raqam kirit (16 xonali): ")
new_k = ""

for i in range(1, 17):
    new_k += karta[i-1]
    if i % 4 == 0:
        new_k += " "

print(karta)
print(new_k)


karta = input("Karta raqam kirit (16 xonali): ")
new_k = ""


for i in karta:
    if i != " ":
        new_k += i

print(karta)
print(new_k)
