import os

from pwn import *

context.arch = 'amd64'

argv = ['A' for _ in range(100)]
argv[ord('A')] = '\x00'
argv[ord('B')] = '\x20\x0a\x0d'
argv[ord('C')] = '1337'

stdin = '\x00\x0a\x00\xff'
stderr = '\x00\x0a\x02\xff'

r1, w1 = os.pipe()
r2, w2 = os.pipe()
os.write(w1, stdin)
os.write(w2, stderr)

with open('\x0a', 'w') as f:
	f.write('\x00\x00\x00\x00')

os.environ["\xde\xad\xbe\xef"] = "\xca\xfe\xba\xbe"


p = process(executable='/home/input2/input', 
	    argv=argv, 
	    stdin=r1, stderr=r2
     )

conn = remote('localhost', int(argv[ord('C')]))
conn.sendline('\xde\xad\xbe\xef')

p.interactive()
