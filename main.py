file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("power.txt") as files:
    files.write("New text. Power Is In Jesus.")
    content = files.read()
    print(content)
    files.close()

print(content)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text. ")
