ItemsInCart = 0

if ItemsInCart != 2:

    # raise Exception("Products Cart Count is not matching")
    pass

assert(ItemsInCart == 0)

try:
    with open('FileLog.txt', 'r') as reader:
        content = reader.readlines()
except:
    print("Somehow I reached this block because there is a failure in try block")

try:
    with open('FileLog.txt', 'r') as reader:
        content = reader.readlines()
except Exception as e:
    print(e)

finally:
    print("Cleaning up records")
