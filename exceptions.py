# Examples of exceptions

while True:
    try:
        x = int(input("Please enter a number: "))
        print("You entered: " + str(x))
    except ValueError:
        print("Oops!  That was not a number.  Try again...")
    except KeyboardInterrupt:
        print("\nCtrl-C Exiting loop")
    except:
        print("Uncaught Exception")
    finally:
        break

try:
    print("New example")
    int("345)s")
except Exception as exc:
    print("Exception Msg:" + str(exc))
    print("args:" + str(exc.args))

class MyException(Exception):
    name = ""
    code = 3

    def __init__(self, name, code):
        self.name = name
        self.code = code

try:
    print("Arg Example")
    raise MyException("Henry", -23)
except MyException as exc:
    print("Exception Msg:" + str(exc))
    print("args:" + str(exc.args))
    print("Name:" + exc.name)
    print("Code:" + str(exc. code))
