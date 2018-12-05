# def validate(name):
#     if len(name) < 10:
#         raise ValueError("name is too short")

# try:
#         validate('test')
# except Exception as e:
#         print(e)


from exception import NameTooShort

def validate(name):
        if len(name) < 10:
                raise NameTooShort('name is too short')
try:
        validate('test')
except NameTooShort as e:
        print(e)
