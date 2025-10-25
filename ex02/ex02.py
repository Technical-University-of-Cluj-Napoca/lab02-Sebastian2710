def multiply_all(*args: int) -> int:
    result=1
    for x in args:
        result*=x
    return result

print(multiply_all(1,2,3,4,5))
print(multiply_all())
print(multiply_all(7))