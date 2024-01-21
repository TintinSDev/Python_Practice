# secret_number = 9
# guess_min = 0
# guess_max = 3
# while guess_min < guess_max:
#     guess = int(input('Guess: '))
#     guess_min += 1
#     if guess == secret_number:
#         print('You won!')
#         break
#     else:
#         print('You failed!!')

#for loops
# for item in 'Martin': #strings
#     print(item)
for items in ['fff', 'ggg', 'fff']:
    print (items)

for nums in range(14,21,3):
    print(nums)

prices = [10,20,30]

total = 0
for item in prices:
    total += item

print(total)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y}')

#lists and tuples unpacking where [] = lists and () = tuples
names = ('mart', 'main', 'hyer')
x, y, z = names
print(z)
#dictionaries or dicts = {}
#keys are unique
customer = {
    "name": 'MArt',
    'age': 28,
    'is_verified': True
}
print(customer['name'])

message = input('>')
words = message.split(' ')
emojis = {
    ":)": "😅",
    ":(": "😣"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
