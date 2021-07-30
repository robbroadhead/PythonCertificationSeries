# Examples of lambda

def addone(x: int) -> int:
    return x + 1

print("addone(1)")
print(str(addone(1)))

print("lambda x: x + 1")
val = (lambda x: x + 1)(1)

print(val)

print("lambda x,y: x + y")
val = (lambda x,y: x + y)(3,2)
print(val)

mylam = lambda x,y: x * y
print(mylam(2,3))

mylam2 = lambda x,y,z: x * y * z
print(mylam2(2,3,4))

addv = lambda x: x + 1
subt = lambda x: x - 1

result = addv(addv(addv(subt(subt(1)))))
print(result)

result2 = (lambda *args: sum(args))(1,2,3)
print(result2)
result3 = (lambda **kwargs: sum(kwargs.values()))(a=1,b=2,c=3)
print(result3)

print(str(addone(1)))

