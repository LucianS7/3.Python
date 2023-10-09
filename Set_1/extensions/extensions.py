def main():
    file_name = input("Please input file name with extension: ").casefold().strip()
    file_type(file_name)

def file_type(txt):
    file_extension = txt.rpartition(".")[2]
    match file_extension:
         case "gif":
             print("image/gif")
         case "jpg":
             print("image/jpeg")
         case "jpeg":
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

main()