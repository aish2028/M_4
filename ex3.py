def cast_vote(age):
    assert age>=18,"Age should not be <18,it was:{age}"
    print("thank you for voting....")
try:
    age=int(input("enter the age:"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print("you entered valid age...")
finally:
    print("End....")