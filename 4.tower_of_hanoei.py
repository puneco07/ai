A=[3,2,1]
B=[]
C=[]

def show():
    print("A:",A,"B:",B,"C:",C)
    print()

def move(n,source,target,auxiliary):
    if n==1:
        disc=source.pop()
        target.append(disc)
        show()
        return

    move(n-1,source,auxiliary,target)
    disc=source.pop()
    target.append(disc)
    show()

    move(n-1,auxiliary,target,source)

print("Initial State:")
show()

move(3,A,C,B)
