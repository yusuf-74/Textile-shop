import os,uuid
def products_image_file_path(instance , filename):
    ext=os.path.splitext(filename)[1]
    filename=f'{uuid.uuid4()}{ext}'
    return os.path.join('products',instance.type ,filename)