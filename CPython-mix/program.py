import subprocess

print("Inside Python file: ....")
subprocess.call(["gcc", "myCprogram.c"])
subprocess.call("./b.out")
print("Task is done.")
