from base64 import b64encode, b64decode

to_base_64 = lambda x: b64encode(x).replace('=','') 

from_base_64 = lambda x: b64decode(x + '==') 