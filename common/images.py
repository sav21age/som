
import os
import uuid

# def get_image_path(instance, filename):
#     f = os.path.splitext(filename)
#     return '{0}-{1}{2}'.format(f[0], random.randint(10000, 99999), f[1])

def get_image_path(instance, filename):
    f = os.path.splitext(filename)
    return 'images/{0}{1}'.format(uuid.uuid1().hex, f[1].lower())
