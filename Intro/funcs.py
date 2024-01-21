# keyword arguments
def greet_user(firs_name, last_name):
    print(f'{firs_name}, {last_name}')
    print("Welcome Aboard")


print('Start')
greet_user(last_name='Smith', firs_name='John')
print('End!!')


def emoji_converter(mess):
    words = mess.split(' ')
    emojis = {
        ":)": "😅",
        ":(": "😣"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input('>')
print(emoji_converter(message))

# keyword arguments always come after positional arguments


def square(num):
    return num * num


print(square(4))
