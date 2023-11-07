from collections import Counter

string= " Hello Hello Hellllo"
result= Counter(string)
result= max(result, key=result.get)

print("Most frequent character: ",result)