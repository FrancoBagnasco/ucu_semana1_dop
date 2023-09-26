
import re

file = open("data/mbox.txt")
data = []

for line in file:
    line = line.strip()
    number = re.findall(r'\b\d+\b', line)
    data.extend(number)
    
data = [int(number) for number in data]
    
promedio = int(sum(data) / len(data))

print(f"El promedio de todos los numeros del archivo txt es: {promedio}")