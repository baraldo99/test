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

runCommand("git flow feature start firstfeature")
appentToFile(repopath+"/inventario.md", "2076434")
appentToFile(repopath+"/inventario.md", "2076324")
runCommand("git add inventario.md")
runCommand('git commit -m "close #1" -m "Aggiunta del file inventario.md"')
runCommand('git flow feature publish firstfeature')
runCommand('git flow feature finish -k firstfeature')
runCommand('git push origin develop')
print("FEATURE 1 creata")


# SECOND FEATURE
input("Premi Invio per procedere con la creazione della FEATURE 2")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start secondfeature')
appentToFile(repopath+"/processori.md", "2076434")
appentToFile(repopath+"/processori.md", "2076324")
appentToFile(repopath+"/inventario.md", "- processori.md")
runCommand("git add processori.md")
runCommand("git add inventario.md")
runCommand('git commit -m "close #2" -m "Aggiunta del file processori.md" -m "Modificato il file inventario.md"')
runCommand('git flow feature publish secondfeature')
runCommand('git flow feature finish -k secondfeature')
print("FEATURE 2 creata")
input("Premi Invio per procedere con la sincronizzazione della FEATURE 2")
runCommand('git push origin develop')
print("FEATURE 2 creata")

input("Premi Invio per procedere con la creazione della FEATURE 5")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('mkdir periferiche')
runCommand('git flow feature start fifthfeature')
writeToFile(repopath+"/inventario.md", '''2076434
2076324

componenti
- processori.md
- schede_madri.md

periferiche

Elettronica Padovana
''')
writeToFile(repopath+"/periferiche/vuoto.txt","")
runCommand("git add inventario.md")
runCommand("git add periferiche/")
runCommand('git commit -m "close #5" -m "Aggiunta della cartella Periferiche"  -m "Aggiunta del file temporaneo vuoto.txt" -m "Modifica del file inventario.md"')
runCommand("git flow feature publish fifthfeature")
runCommand("git flow feature finish -k fifthfeature")
runCommand("git push origin develop")
print("FEATURE 5 creata")


input("Premi Invio per procedere con la creazione della FEATURE 7")
runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start seventhfeature')
writeToFile(repopath+"/periferiche/mouse.md",'''2076434
2076324
''')
writeToFile(repopath+"/inventario.md", '''2076434
2076324

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
runCommand('git commit -m "close #7" -m "Aggiunta del file mouse" -m "Modifica del file inventario"')
runCommand('git flow feature publish seventhfeature')
runCommand('git flow feature finish -k seventhfeature')
runCommand('git push origin develop')
print("FEATURE 7 creata")
