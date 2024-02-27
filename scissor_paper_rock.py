spr=["scissor","paper","rock","mud"]

print("spr:",spr)

spr.append("mud")
print("spr:",spr)

item=spr.pop()
print("popped item:",item)
print("spr:",spr)

print("scissor count:",spr.count("scissor"))

fruits=["apple","banana","orange"]
spr.extend(fruits)
print("spr",spr)

spr.remove("apple")
print("spr",spr)

another_spr=spr.copy()
print("another spr:",another_spr)

index=spr.index("paper")
print("paper is at index:",index)

spr.reverse()
print("spr",spr)

#sort ascending
spr.sort()
print("spr sorted",spr)

#sort descending
spr.sort(reverse=True)
print("spr sorted",spr)

spr.clear()
print("spr",spr)