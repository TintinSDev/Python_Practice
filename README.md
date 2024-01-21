# DPYTHON_PRACTICE
number = random.randint(1,10)
mini_guess = 0
maxi_guess = 5
while mini_guess < maxi_guess:
    guess = int(input("Let's play a silly game. Guess a number between 1 and 10: "))
    mini_guess += 1
    if guess == number:
        print('YOU ARE LUCKY CHAP!!')
        break
    else:
        print("You's a sucker")

## qrcode generator
import qrcode

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

if __name__ == "__main__":
    data_to_encode = input("Enter the data to encode: ")
    file_path = input("Enter the file path to save the QR code (e.g., 'qrcode.png'): ")

    generate_qr_code(data_to_encode, file_path)
    print(f"QR code saved to {file_path}")
