f=open("morefile.txt")

print(f.read())

f.close()



# the same can be written by with statement


with open("morefile.txt") as f:
    f.read()
    print(f.read())

# you dont want to close this file like f.close()