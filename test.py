import os
try:
    os.remove("dontwant.txt")
except FileNotFoundError as e:
    print("File doesn't exist")
except Exception as e:
    print("Something went wrong, e: ", e)
else:
    print("File is deleted Successfully!!")
finally:
    print("Execution Complete!!")