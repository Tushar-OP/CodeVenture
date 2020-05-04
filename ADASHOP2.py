# cook your dish her

def sequence():
    print("2 2")
    print("1 3")
    print("3 1")
    print("2 2")
    print("3 3")
    print("1 5")
    print("5 1")
    print("3 3")
    print("4 4")
    print("1 7")
    print("7 1")
    print("4 4")
    print("5 5")
    print("2 8")
    print("8 2")
    print("5 5")
    print("6 6")
    print("4 8")
    print("8 4")
    print("6 6")
    print("7 7")
    print("6 8")
    print("8 6")
    print("7 7")
    print("8 8")

if __name__=='__main__':
   try:
       t = int(input())
   except:
       t = 0
   
   
   for _ in range(t):
       r, c = map(int, input().rstrip().split())
       steps_required = 25
       
       
       if r == c and r == 1:
          print(steps_required)
          sequence()
       elif r == c:
          steps_required += 1
          print(steps_required)
          print("1 1")
          sequence()
       else:
           steps_required += 2
           z = (r+c)//2
           print(steps_required)
           print(z, z)
           print("1 1")
           sequence()
       
       
       
       
       