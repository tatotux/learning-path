from sys import argv
from os.path import exists

script, from_exscript1, to_exscript2 = argv

print(f"Copying from {from_exscript1} to {to_exscript2}")

in_file = open(from_exscript1).read()
print(in_file)
print(f"The input file is {len(in_file)} bytes long")

print(f"Does the output file exist? {exists(to_exscript2)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file=open(to_exscript2,'a')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
