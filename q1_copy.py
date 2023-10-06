#Page 222
#Q1

filename = input("Input file: ")
output_filename = input("Output file: ")

file = open(filename, "r")
output_file = open(output_filename, "w")

content = file.read()
output_file.write(content)

file.close()
output_file.close()