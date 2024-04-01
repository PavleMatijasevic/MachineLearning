threshold = 1.5
inputs = [1, 0, 1, 0, 1]
weights = [0.7, 0.6, 0.5, 0.3, 0.4]
suma = 0

for i in range(len(inputs)):
    suma += inputs[i] * weights[i]  

activate = (suma > threshold)
print(activate)



