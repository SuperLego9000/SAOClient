import base64
import json
def decode(key):
    raw=base64.b64decode(key).decode()
    #raw=str(raw)
    #print(raw)
    #decrypted
    data=json.loads(raw)
    #print(data)
    #data={key,name}
    return data
def encode(arr):
    raw=json.dumps(arr)
    raw=base64.b64encode(bytes(raw,"utf-8")).decode()
    return raw
test="WyJ0aGUgam9lcyIsIldBR0hSViJd"
if __name__=="__main__":
    x=encode(["joe gang","abcxyz"])
    y=decode(x)
    print(x,y)