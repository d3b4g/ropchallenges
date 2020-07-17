from pwn import *

#context.log_level = 'debug'
context.arch = 'amd64'
sh = gdb.debug("./ropmev2")
sh.recvline()
padding = cyclic(400)
sh.sendline(padding)
log.info(" Leaking stack address")
sh.interactive()
