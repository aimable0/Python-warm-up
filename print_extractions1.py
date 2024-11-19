def print_media_type(file_name):
  
  # splitting the name to get the extension part
  name_parts = file_name.split('.')

  try:
    # matching different case if the extension exist
    match name_parts[1]:
      case "gif":
        print("image/gif")
      case "jpg" | "jpeg":
        print("image/jpeg")
      case "png":
        print("image/png")
      case "pdf":
        print("application/pdf")
      case "txt":
        print("text/plain")
      case "zip":
        print("application/zip")
      case _:
        print("application/octet-stream")
  except Exception:
    print("application/octet-stream")
    
  

def main():
  name = input('File name: ')
  print_media_type(name)

main()