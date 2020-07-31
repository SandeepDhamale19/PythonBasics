print("Open file for reading or writing")
print("file: path to file")
print("mode: read, write, append, binary or text")
print("encoding: encoding to use in text mode. Default: sys.getdefaultencoding()- utf-8")
# files contain series of bytes
#Mode: Read (r), write(w), append(a)
#Selector: binary mode(b), text mode (t)
#Final mode is combination of : mode + selector e.g. 'wt' i.e. write-text

print("\n1. Write to a file.")
f = open('MyPythonFile', 'wt', encoding='utf-8')
print("\t" + str(f.write("Python is simple language."))) # returns no of chars
f.write("\nPython is programming language.")
f.write("\nPython is gaming language.")
f.close()

print("\n2. Read a file.")
r=open('MyPythonFile', 'rt', encoding='utf-8')
print("\tRead complete: " + str(r.read()))
r.close()
r=open('MyPythonFile', 'rt', encoding='utf-8')
print("\tRead to a length: " + str(r.read(32)))
r.close()
r=open('MyPythonFile', 'rt', encoding='utf-8')
print("\tRead line by line: " + str(r.readline()))
print("\tRead line by line: " + str(r.readline()))
r.close()
r=open('MyPythonFile', 'rt', encoding='utf-8')
print("\tRead all lines: " + str(r.readlines()))
r.close()

print("\n2. Append a file.")
a=open('MyPythonFile', 'at', encoding='utf-8')
a.writelines(["\nPython is data science language.", "\nPython is AI language"])
a.close()
r=open('MyPythonFile', 'rt', encoding='utf-8')
print("\tRead all lines: " + str(r.readlines()))