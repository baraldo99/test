import subprocess
import os, shutil
import time
username = 'TheBitNinja'
reponame = 'testass'
repopath ='./'+reponame
def appentToFile(file, text):
    file1 = open(file, "a")
    file1.write(text+"\n")
    file1.close()
    return True
def writeToFile(file, text):
    file1 = open(file, "w")
    file1.write(text)
    file1.close()
    return True
def runCommand(cmd):
    print(cmd)
    return subprocess.run(cmd, cwd=repopath, shell=True)

if os.path.isdir(repopath):
    shutil.rmtree(repopath)
subprocess.run(["git", "clone", f"git@github.com:{username}/{reponame}.git"])
runCommand("git checkout develop")
runCommand('git config pull.rebase false')
subprocess.run(["git", "flow", "init", "-d", "--feature", "feature/",  "--bugfix", "bugfix/", "--release", "release/", "--hotfix", "hotfix/", "--support", "support/", "-t","''"], cwd=repopath)
# FIRST FEATURE
input("Premi Invio per procedere con la creazione della FEATURE 1")

runCommand("git flow feature start inventario")
appentToFile(repopath+"/inventario.md", "2079244")
appentToFile(repopath+"/inventario.md", "2082849")
runCommand("git add inventario.md")
runCommand('git commit -m "Aggiunto file inventario.md" -m "close #1"')
runCommand('git flow feature publish inventario')
runCommand('git flow feature finish -k inventario')
runCommand('git push origin develop')
print("FEATURE 1 creata")


# SECOND FEATURE
input("Premi Invio per procedere con la creazione della FEATURE 2")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start processori')
appentToFile(repopath+"/processori.md", "2079244")
appentToFile(repopath+"/processori.md", "2082849")
appentToFile(repopath+"/inventario.md", "- processori.md")
runCommand("git add processori.md")
runCommand("git add inventario.md")
runCommand('git commit -m "Aggiunto file processori.md" -m "Aggiornato file inventario.md" -m "close #2"')
runCommand('git flow feature publish processori')
runCommand('git flow feature finish -k processori')
print("FEATURE 2 creata")
input("Premi Invio per procedere con la sincronizzazione della FEATURE 2")
runCommand('git push origin develop')
print("FEATURE 2 creata")

input("Premi Invio per procedere con la creazione della FEATURE 5")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('mkdir periferiche')
runCommand('git flow feature start periferiche')
writeToFile(repopath+"/inventario.md", '''2079244
2082849

componenti
- processori.md
- schede_madri.md

periferiche

Elettronica Padovana
''')
writeToFile(repopath+"/periferiche/empty.txt","")
runCommand("git add inventario.md")
runCommand("git add periferiche/")
runCommand('git commit -m "Aggiunta cartella periferiche" -m "Aggiunto file temporaneo empty.txt" -m "Aggiorato file inventario.md" -m "close #5"')
runCommand("git flow feature publish periferiche")
runCommand("git flow feature finish -k periferiche")
runCommand("git push origin develop")
print("FEATURE 5 creata")


input("Premi Invio per procedere con la creazione della FEATURE 7")
runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start mouse')
writeToFile(repopath+"/periferiche/mouse.md",'''2079244
2082849
''')
writeToFile(repopath+"/inventario.md", '''2079244
2082849

componenti
- processori.md
- schede_madri.md

periferiche
- tastiere.md
- mouse.md

Elettronica Padovana
''')

runCommand("git add periferiche/")
runCommand("git add mouse.md")
runCommand("git add inventario.md")
runCommand('git commit -m "Aggiunto file mouse.md" -m "Aggiornato file inventario.md" -m "close #7"')
runCommand('git flow feature publish mouse')
runCommand('git flow feature finish -k mouse')
runCommand('git push origin develop')
print("FEATURE 7 creata")
