file = open("test_file.txt", "a")

file.write("asrbasdadb\n")
file.write("1234\n")

for i in range(100):
    file.write("asdfasdfasdfasf\n")

file.close()

file = open("test_file.txt", "r")

content = file.read()
print(content)

file.close()
