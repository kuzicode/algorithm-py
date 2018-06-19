#思路：很简单，遍历列表使用len()求最长
names = ["Joshua Zhao", "XiaoLee", "Ze", "Josh"]
longest = names[0]

# your solution here
for name in names:
    if len(name) > len(longest):
        longest = name

print(longest) 
 
 
