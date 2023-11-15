msg = "hello"
print(msg)

msg_encoded = msg.encode("utf-8").hex()
print(msg_encoded.decode("utf-8"))