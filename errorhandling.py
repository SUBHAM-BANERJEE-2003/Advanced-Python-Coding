try:
    a = int(input())
    b = int(input())
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print("Can't divide by zero. System says: ", e)
except ValueError as e:
    print("Invalid input. System says: ", e)
else:
    print("The code was executed successfully with no errors.")
finally:
    print("This message will always get printed")


# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is:")

# try:
#     for i in range(1, 11):
#         print(f"{a} * {i} = {int(a) * i}")
# except:
#     print("Invalid Input!")
# except Exception as e:
#     print("Sorry.. Invalid Input.some error has occured")
#     print(e)

# print("End of lines. these will always show. even if any error is there as we are handling the error")
# print("This should print. but if error it won't print it if no try except.")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer. ")
# except IndexError:
#     print("Index out of bounds.")

# try:
#     tup1 = (1,2,3,4,5)
# tup1.insert(2,9)
#     l = list(tup1)
#     l.insert(2,9)
#     print(l)
#     print(tup1)
# except AttributeError:
#     print("we cannot insert elements in tuple")

# try:
#     dict = {"name": "Rayees", "age":23, "roll":41, "DOB": "23/05/2003"}
#     print(dict["name"])
#     print(dict["aadhar"])
# except KeyError:
#     print("Key doesnt exist in the dictionary")
