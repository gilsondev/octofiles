# -*- coding: utf-8 -*-

from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile


def dummy_file(name='filetest', content_type="text/plain"):
    """
    Generate a file fake to mock tests with file field in django
    models.

    :param name
        Name of file
    :param content_type
        Content Type of file. Default: text/plain
    """
    filename = "{file}.{format}".format(file=name, format=format)
    return SimpleUploadedFile(filename, b"dummy", content_type=content_type)


def dummy_image(name='fileimage', content_type='image/png'):
    """
    Generate a image file to mock tests with django models

    :param name
        Name of file
    :param content_type
        Content Type of file. Default: image/png:w
    """
    content_type, format = content_type.split('/')
    filename = "{file}.{format}".format(file=name, format=format)

    file_obj = BytesIO()
    image = Image.new("RGBA", size=(50, 50))
    image.save(file_obj, format)
    file_obj.name = filename
    file_obj.seek(0)
    return SimpleUploadedFile(filename, file_obj.read(),
                              content_type=content_type)
