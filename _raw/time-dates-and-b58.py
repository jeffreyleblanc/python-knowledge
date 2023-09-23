
import time
import base64

def H(text):
    print(f"\n{'-'*32}\n{text}\n{'-'*32}\n")
    return True

def GV(var_name):
    val = globals().get(var_name)
    print(f"{var_name}: ",val)

def L(*args):
    print(""); print(*args)


if H("Basic Time"):
    print("time.time() => seconds since epoch")
    epoch_sec = time.time()
    GV("epoch_sec")

    epoch_ms = int(time.time()*1000)
    GV("epoch_ms")

if H("Casting Integers"):
    epoch_ms_hex = hex(epoch_ms)
    GV("epoch_ms_hex")

    L("integers to hex:")
    for num in [0,56,7893,283300282]:
        print(f"=> {num} {hex(num)}")

    L("hex padded epoch_ms:")
    hex_epoch_ms = f"{epoch_ms_hex[2:]:>012}"
    GV("hex_epoch_ms")

    L("As base64:")
    b64_epoch_ms = base64.b64encode(bytes.fromhex(hex_epoch_ms)).decode()
    GV("b64_epoch_ms")


"""
show how large epoch_sec/ms grow 100, 500 years out
show basics of divmod for forming an encoding are
look at base58 encoding

"""

exit()

"""
# https://github.com/serengil/crypto/blob/master/python/base58.py

timehex$ python3
Python 3.11.4 (main, Jun  9 2023, 07:59:55) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> import hex
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hex'
>>> sec = int(time.time())
>>> sec
1695000777
>>> hex(sec)
'0x6507a8c9'
>>> len(hex(sec))
10
>>> sec_year = 60*60*24*365
>>> sec_year
31536000
>>> sec
1695000777
>>> sec + 1000*sec_year
33231000777
>>> hex(sec + 1000*sec_year)
'0x7bcb8d4c9'
>>> len(hex(sec + 1000*sec_year))
11


>>> N = 3333
>>> divmod(N,16)
(208, 5)
>>> hex(N)
'0xd05'
>>> divmod(208,16)
(13, 0)
>>> divmod(13,16)
(0, 13)


timehex$ apt-cache policy python3-base58
>>> import base58
>>> dir(base58)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'alphabet', 'b58decode', 'b58decode_check', 'b58decode_int', 'b58encode', 'b58encode_check', 'b58encode_int', 'bseq', 'buffer', 'iseq', 'main', 'scrub_input', 'sha256']
>>> base58.b58encode_int(345132)
b'2mbZ'
>>> import time
>>> base58.b58encode_int(int(time.time()))
b'3anKuA'
>>> base58.b58encode_int(int(time.time()))
b'3anKuC'
>>> base58.b58encode_int(int(time.time()*10))
b'SppG3Q'
>>> base58.b58encode_int(int(time.time()*100))
b'5TF9bWd'
>>> base58.b58encode_int(int(time.time()*1000))
b'mXSUxsw'
>>> base58.b58encode_int(int(time.time()*1000))
b'mXSUzBo'
>>> ms_per_year = 1000 * 60 * 60 * 24 * 365
>>> ms_per_year
31536000000
>>> base58.b58encode_int( int(time.time()*1000 + 500*ms_per_year ))
b'8uixeuC8'
>>> base58.b58encode_int( int(time.time()*1000 ))
b'mXSVQHf'
>>> base58.b58encode_int( int(time.time()*1000 )).decode()
'mXSVdZM'
>>> x = base58.b58encode_int( int(time.time()*1000 )).decode()
>>> len(x)
7
>>> f"{x:08}"
'mXSVfGt0'
>>> f"{x:>08}"
'0mXSVfGt'
>>> x = "abcdefg"
>>> f"{x:>08}"
'0abcdefg'
>>> x = "abcdefgh"
>>> f"{x:>08}"
'abcdefgh'
>>> x = "abcdefghijk"
>>> f"{x:>08}"
'abcdefghijk'
>>>
"""


