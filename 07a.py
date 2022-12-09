import sys


def lr(dirs, name, indent=""):
    for d in dirs[name]["dirs"]:
        print(indent, d, dirs[name+d+"/"]["total_size"])
        lr(dirs, name + d + "/", indent + " ")
    for f in dirs[name]["files"]:
        print(indent, f)

def total_size(dirs, name):
    dirs[name]["seen"] = True
    if "total_size" in dirs[name]:
        return dirs[name]["total_size"]

    s = 0
    for d in dirs[name]["dirs"]:
        s += total_size(dirs, name + d + "/")
    for f in dirs[name]["files"]:
        s += dirs[name]["files"][f]

    dirs[name]["total_size"] = s
    return s


cd = ""
dirs = {}

for line in sys.stdin:
    parts = line.rstrip().split()
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "/":
                cd = "/"
            elif parts[2] == "..":
                cd = cd.rsplit("/", 2)[0] + "/"
            else:
                cd += parts[2] + "/"

            if cd not in dirs:
                dirs[cd] = {"dirs": [], "files": {}}
        continue

    if parts[0] == "dir":
        dirname = cd + parts[1] + "/"
        if dirname not in dirs:
            dirs[dirname] = {"dirs": [], "files": {}}
        dirs[cd]["dirs"].append(parts[1])
    else:
        dirs[cd]["files"][parts[1]] = int(parts[0])


total_size(dirs, "/")
lr(dirs, "/")

suma = 0
for d in dirs:
    s = dirs[d]["total_size"]
    if s <= 100000:
        suma += s

print(suma)
