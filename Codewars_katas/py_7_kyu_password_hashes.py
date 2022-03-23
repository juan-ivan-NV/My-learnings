import hashlib
pass_hash = lambda str: (hashlib.md5(bytes(str, 'utf-8'))).hexdigest()