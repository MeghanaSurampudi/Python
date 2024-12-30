import json
def is_complex_num(objct):
    if'__complex__'in objct:
        return complex(objct['real'],objct['img'])
    return objct
complex_object=json.loads('{__complex
