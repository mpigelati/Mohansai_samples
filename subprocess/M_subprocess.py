import subprocess

cmd= "ls -la"

subprocess.call(cmd,shell=True)

ls=subprocess.call(["ls","-la"])
print(ls) # prints 0

data = subprocess.call("echo $HOME",shell=True)
print(data) # prints 0
#help(subprocess)

# In Python 2.7 or Python 3
# Instead of making a Popen object directly, you can use the subprocess.check_output() function to store output of a command in a string:

data = subprocess.check_output(["ls", "-la"])
print(data)
#Output :- b'total 16\ndrwxrwxr-x 2 mohansai mohansai 4096 Sep 14 16:24 .\ndrwxrwxr-x 5 mohansai mohansai 4096 Sep 14 15:28 ..\n-rw-rw-r-- 1 mohansai mohansai  444 Sep 14 16:24 M_subprocess.py\n-rw-rw-r-- 1 mohansai mohansai  464 Sep 14 16:23 Notes\n'


subprocess.call(["ls","-la"])
#output :-
"""
total 16
drwxrwxr-x 2 mohansai mohansai 4096 Sep 14 16:24 .
drwxrwxr-x 5 mohansai mohansai 4096 Sep 14 15:28 ..
-rw-rw-r-- 1 mohansai mohansai  444 Sep 14 16:24 M_subprocess.py
-rw-rw-r-- 1 mohansai mohansai  464 Sep 14 16:23 Notes"""


# working i
p = subprocess.Popen("pwd", stdout=subprocess.PIPE)
result = p.communicate()[0]
print (result)

command = "ls -la"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

#output = process.communicate()
#print (output[0])

#print(process.communicate())
#print(process.communicate()[0])
output = process.communicate()
print(output[0])
#print()

"""
In the Popen constructor, if shell is True, you should pass the command as a string rather than as a sequence. Otherwise, just split the command into a list:

command = ["ntpq", "-p"]  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None)

If you need to read also the standard error, into the Popen initialization, you can set stderr to subprocess.PIPE or to subprocess.STDOUT:

"""
command = "ntpq -p"  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

#Launch the shell command:
output, error = process.communicate()

