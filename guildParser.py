import base64
import json
def convert(key):
    "returns name and joincode"
    raw=base64.b64decode(key).decode()
    #raw=str(raw)
    #print(raw)
    #decrypted
    data=json.loads(raw)
    #print(data)
    #data={key,name}
    return data
test="WyJ0aGUgam9lcyIsIldBR0hSViJd"