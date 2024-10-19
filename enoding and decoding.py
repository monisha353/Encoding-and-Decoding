import base64

def decoder():
    message = input("Message to be decoded >>")
    message_in_bytes = bytes(message,'utf-8')
    decoded_message = base64.b64decode(message_in_bytes)
    print(f"Decoded: {decoded_message}")

def encoder():
    message = input("Message to be encoded >>")
    message_in_bytes = bytes(message,'utf-8')
    encoded_message = base64.b64encode(message_in_bytes)
    print(f"Encoded: {encoded_message}")

print("Python Decoder and Encoder")

print("1. Encoder")
print("2. Decoder")
option = int(input("Select option (1/2) >>"))

if option==1:
    encoder()
elif option==2:
    decoder()
else:
    print("Error! Try Again")
    



      
