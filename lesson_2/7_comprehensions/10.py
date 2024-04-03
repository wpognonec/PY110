import random
def generate_uuid():
    chars = '0123456789abcdef'
    uuid = "".join([random.choice(chars) for _ in range(32)])
    uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
    return uuid

generate_uuid()