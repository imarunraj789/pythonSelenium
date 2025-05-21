with open('Test.txt','r') as reader:
    content = reader.readlines()
    reversedContent = reversed(content)

with open('Test.txt','w') as writer:
    for line in content:
        writer.write(line)
    for line in reversedContent:
        writer.write(line)
