list = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
# by inbuilt functions
print(max(list))
print(min(list))

# programatically

max = list[0]
for i in range(len(list)):
    if list[i] > max:
        max = list[i]
print(max)

min = list[0]
for i in range(len(list)):
    if list[i] < min:
        min = list[i]
print(min)
