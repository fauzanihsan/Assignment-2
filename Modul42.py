distinct_ans = []

for i in range(10):
    x = int(input("Enter Number :"))
    if (x%42)not in distinct_ans:
        distinct_ans.append(x%42)
print("\n", "Answer :",len(distinct_ans))

