class MaxLimitError(Exception):

    def __init__(self,message):
        self.message=message

    def __str__(self):
        return f"{self.__class__.__name__}:{self.messeage}"
c=0
def login(username,password):
    global c
    if username=="abc" and password=="cba":
        print("login is successful")
    else:
        print("bad credentials...")
    c+=1
    if c>2:
        raise MaxLimitError("you have reached maximum number of attempts")
    
login("ABC","CBA")
login("a","c")
login("","")
login("abc","cba")