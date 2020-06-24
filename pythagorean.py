n = int(input("enter number of test cases"))
for i in range(n):
    a,b,c = input().split()
    a2 = pow(int(a),2)
    b2 = pow(int(b),2)
    c2 = pow(int(c),2)
    if a2 == (b2+c2) or b2 == (a2+c2) or c2 == (a2+b2):
        print("pythagorean triplet")
    else: print("not pythagorean triples")


