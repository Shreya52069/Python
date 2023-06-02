import subprocess


version = subprocess.run(['python3', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pyversion = version.stdout()
versionnumber = pyversion.split(' ')
nums = versionnumber[1].split('.')
number = str(nums[0]+nums[1])

print(pyversion)
print(versionnumber)
print(nums)
print(number)