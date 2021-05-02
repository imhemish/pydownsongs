import os
os.system("git add .")
message = input("Enter message: ")
os.system('git commit -m "{}"'.format(message))
os.system("git push gh master") #Gh is github remote
os.system("git push bb master") #bb is bitbucket remote
os.system("python setup.py sdist")
os.system("twine upload dist/*")
os.system("rm -r dist")
os.system("rm -r pydownsongs.egg-info")
print("Please make new release on GitHub and press Enter")
input()
os.system("git fetch gh --tags")
os.system("git push bb --tags")
print("Completed")