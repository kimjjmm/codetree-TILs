class secret:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time
        
    def user_print(self):
        print(f"secret code : {self.code}")
        print(f"meeting point : {self.location}")
        print(f"time : {self.time}")

c,l,t = tuple(input().split())

s = secret(c, l, int(t))
s.user_print()