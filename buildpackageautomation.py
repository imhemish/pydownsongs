# Enusre git config --local is done
# Ensure gh and bb remotes are added
import os
import sys
os.system("git add .")
message = input("Enter message: ")
os.system('git commit -m "{}"'.format(message))
os.system("git push gh master") #Gh is github remote
os.system("git push bb master") #bb is bitbucket remote
os.system("python setup.py sdist")
os.system("twine upload dist/*")
if sys.platform == "win32":
    os.system("deltree dist")
    os.system("deltree pydownsongs.egg-info")
else:
    os.system("rm -r dist")
    os.system("rm -r pydownsongs.egg-info")
print("Please make new release on GitHub and press Enter")
input()
os.system("git fetch gh --tags")
os.system("git push bb --tags")
print("Completed")