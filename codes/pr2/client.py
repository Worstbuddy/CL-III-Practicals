import Pyro4

# Paste URI from server
uri = input("Enter Server URI: ")

proxy = Pyro4.Proxy(uri)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = proxy.concatenate(str1, str2)

print("Concatenated String:", result)