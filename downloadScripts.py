import sys
import subprocess
import json
f=open('C:\\Users\\Shivam-P\\Downloads\\DataDep.json',"r")
data=json.load(f)
installed=[]
notInstalled=[]
dep="";
def installDep(depName):
    subprocess.check_call(['pip', 'install',depName])
    reqs = subprocess.check_output(['pip','freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if("panda" in installed_packages):
        installed.append(depName)
    else:
        notInstalled.append(depName)
for x in data:
    dep=x['name']+'=='+x['ver']
    installDep(dep)


print("Installed Dependencies \n")
print(installed)
print("Not Installed Dependencies\n")
print(notInstalled)
