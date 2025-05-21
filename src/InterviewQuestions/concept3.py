with open("E:/PythonSeleniumAutomation/PythonTesting/InterviewQuestions/test.txt","w") as f:
    f.write("Hello world New")

try:
    with open("E:/PythonSeleniumAutomation/PythonTesting/InterviewQuestions/test.txt","r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print(e)

finally:
    print("Final code to be executed")