from hashlib import sha1


def get_hash(str, salt=None):
    if salt:
        str += salt
    sh = sha1()
    sh.update(str.encode('utf-8'))
    return sh.hexdigest()
