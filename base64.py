from pwn import *
r = remote('ip' , "port")
r.close()
r.recvline()
r.recvlines("N")
r.recvuntil(b'...:')
r.sendline(b'')
r.sendlineafter(b'...', )
r.interactive()
import base64
base64.b64encode(b'')
