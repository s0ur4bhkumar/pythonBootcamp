# file = None
# try:
#     file = open("./day30/file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("./day30/file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"{error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human Height should not be over 3 meters.')

bmi = weight/height**2
print(bmi)