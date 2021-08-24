n = int(input())
cod = "".join(input().split())

msg = bytearray.fromhex(cod)
msg = msg.decode()

print(msg)

#fonte: https://www.delftstack.com/pt/howto/python/hex-to-ascii-python/