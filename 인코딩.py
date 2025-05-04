# Class-13.py
list = [ 'a', '가']
for a in list:
    print(f"{a} => {hex(ord(a))} => {chr(ord(a))}")
    print(f"type(org)={type(a)}, org={a}")

    b = a.encode('utf-8')
    print(f"type(enc)={type(b)}, enc={b}")

    c = b.decode('utf-8')
    print(f"type(dec)={type(c)}, enc={c}")