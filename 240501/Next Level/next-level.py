class info:
    def __init__(self,user_id='codetree',level=10):
        self.user_id = id
        self.level = level

        
usr1=info()
usr2=info()

usr1.user_id = "codetree"
usr1.level = 10

user_id, level = input().split()

usr2.user_id = user_id
usr2.level = int(level)

print(f"user {usr1.user_id} lv {usr1.level}")
print(f"user {usr2.user_id} lv {usr2.level}")