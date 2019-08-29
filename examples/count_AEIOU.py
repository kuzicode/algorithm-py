#思路：生成字典，使用fromkey
# string of vowels
vowels = 'aeiou'
counter = {}.fromkeys(vowels,0)

# change this value for a different result
in_str = 'Hello, have you tried our turorial section yet?'

# make it suitable for caseless comparisions
in_str = in_str.casefold()

# make a dictionary with each vowel a key and value 0
# your soultion here count the vowels

print(counter)

