def print_extension(name):
  # create a dictionary to be used while checking for extension

  media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
  
  # loop through the dictianary's key and value at the same time
  for extension, mimetype in media_types.items():
    if name.endswith(extension):
      print(mimetype)
      return
  # if the extension was not found in the list or is not on the name we print no "extension"
  print('No extension')

def main():
  text = input('File name: ')
  print_extension(text)

main()
