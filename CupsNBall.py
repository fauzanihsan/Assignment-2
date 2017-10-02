cups = input("Input Letter :")
ball = [1,0,0]

for i in range(len(cups)):
    if cups[i] == "a":
        x = ball[0]
        ball[0] = ball[1]
        ball[1] = x
    elif cups [i] == "b":
        x = ball[1]
        ball[1]=ball[2]
        ball[2]=x
    elif cups[i] == "c":
        x = ball[0]
        ball[0]=ball[2]
        ball[2]=x
for i in range(3):
    if ball[i] == 1:
        print(i+1)






