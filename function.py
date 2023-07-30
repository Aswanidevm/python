# #parameters
# def say_hello(name, emoji):
#     print(f"helooo {name} howzz you {emoji}")

# #arguments
# say_hello("Aswa", "\U0001f600")

# #positional arguments
# say_hello("asswwea", "\U0001F606")
# say_hello("Aswa", "\U0001F923")


# # grinning face
# print("\N{grinning face}")
 
# # slightly smiling face
# print("\N{slightly smiling face}")
 
# # winking face
# print("\N{winking face}")

# #keyword arguments
# say_hello(emoji="\N{winking face}", name="Kedar")

#Default parameters
def say_hello(name="kedu", emoji="\N{slightly smiling face}"):
    print(f"helooo {name} howzz you {emoji}")

say_hello()