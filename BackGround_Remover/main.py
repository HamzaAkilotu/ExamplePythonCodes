from rembg import remove

input_path = "C:\\Users\\Hamza Akılotu\\OneDrive\\Desktop\\image.jpeg"
output_path = "output.png"
with open(input_path, mode="rb") as i:
    with open(output_path, mode="wb") as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)
