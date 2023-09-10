#  ****************IN PROGRESS ********************


import subprocess

p1 = subprocess.Popen(['echo', 'bobbyhadz.com'])
p2 = subprocess.Popen(['echo', 'google.com'])

exit_code1 = p1.wait()
print(exit_code1)

exit_code2 = p2.wait()
print(exit_code2)



# import subprocess

# p1 = subprocess.Popen(['sleep', '5'])
# p2 = subprocess.Popen(['sleep', '5'])

# exit_code1 = p1.wait(timeout=8)
# print(exit_code1)

# exit_code2 = p2.wait(timeout=4)
# print(exit_code2)

