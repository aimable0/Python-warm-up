media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

text = input('File name: ')

def print_extension(text):
  for extension, mimetype in media_types.items():
    if text.endswith(extension):
      print(mimetype)
      return
  print('No extension')

print_extension(text)