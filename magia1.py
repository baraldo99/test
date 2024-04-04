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

runCommand("git flow feature start primafeature")
appentToFile(repopath+"/inventario.md", "2068226")
appentToFile(repopath+"/inventario.md", "2082852")
runCommand("git add inventario.md")
runCommand('git commit -m "aggiunto il file inventario.md" -m "close #1"')
runCommand('git flow feature publish primafeature')
runCommand('git flow feature finish -k primafeature')
runCommand('git push origin develop')
print("FEATURE 1 creata")


# SECOND FEATURE
input("Premi Invio per procedere con la creazione della FEATURE 2")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start secondafeature')
appentToFile(repopath+"/processori.md", "2068226")
appentToFile(repopath+"/processori.md", "2082852")
appentToFile(repopath+"/inventario.md", "- processori.md")
runCommand("git add processori.md")
runCommand("git add inventario.md")
runCommand('git commit -m "aggiunto il file processori.md" -m "aggiornato il file inventario.md" -m "close #2"')
runCommand('git flow feature publish secondafeature')
runCommand('git flow feature finish -k secondafeature')
print("FEATURE 2 creata")
input("Premi Invio per procedere con la sincronizzazione della FEATURE 2")
runCommand('git push origin develop')
print("FEATURE 2 creata")

input("Premi Invio per procedere con la creazione della FEATURE 5")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('mkdir periferiche')
runCommand('git flow feature start quintafeature')
writeToFile(repopath+"/inventario.md", '''2068226
2082852

componenti
- processori.md
- schede_madri.md

periferiche

Elettronica Padovana
''')
writeToFile(repopath+"/periferiche/empty.txt","")
runCommand("git add inventario.md")
runCommand("git add periferiche/")
runCommand('git commit -m "aggiunta la cartella periferiche" -m "aggiunto il file temporaneo empty.txt" -m "aggiorato il file inventario.md" -m "close #5"')
runCommand("git flow feature publish quintafeature")
runCommand("git flow feature finish -k quintafeature")
runCommand("git push origin develop")
print("FEATURE 5 creata")


input("Premi Invio per procedere con la creazione della FEATURE 7")
runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start settimafeature')
writeToFile(repopath+"/periferiche/mouse.md",'''2068226
2082852
''')
writeToFile(repopath+"/inventario.md", '''2068226
2082852

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
runCommand('git commit -m "aggiunto il file mouse.md" -m "aggiornato il file inventario.md" -m "close #7"')
runCommand('git flow feature publish settimafeature')
runCommand('git flow feature finish -k settimafeature')
runCommand('git push origin develop')
print("FEATURE 7 creata")
