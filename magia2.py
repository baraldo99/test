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

# THIRD FEATURE
input("Premi Invio per procedere con la creazione della FEATURE 3")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start terzafeature')
appentToFile(repopath+"/schede_madri.md", "2068226")
appentToFile(repopath+"/schede_madri.md", "2082852")
appentToFile(repopath+"/inventario.md", "- schede_madri.md")
runCommand("git add schede_madri.md")
runCommand("git add inventario.md")
runCommand('git commit -m "aggiunto il file schede_madri.md" -m "aggiornato il file inventario.md" -m "close #3"')
runCommand('git flow feature publish terzafeature')
runCommand('git flow feature finish -k terzafeature')
input("Sync Locale")
runCommand('git pull origin develop')
input("Resolve merge Locale")
writeToFile(repopath+"/inventario.md", '''2068226
2082852
- schede_madri.md
- processori.md
''')
runCommand("git add inventario.md")
runCommand('git commit -m "resolve merge conflicts"')
input("push resolve merge Locale")
runCommand('git push origin develop')
print("FEATURE 3 creata")


# RELEASE V1
input("Premi Invio per procedere con la creazione della RELEASE V1")
runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow release start -F Version_1.0')
appentToFile(repopath+"/inventario.md", "\nElettronica Padovana")
runCommand("git add inventario.md")
time.sleep(2)
runCommand('git commit -m "aggiornato il file inventario.md"')
runCommand('git flow release publish Version_1.0')
runCommand('git push -f origin main')
runCommand('git flow release finish Version_1.0 -m "Version_1.0" 1.0.0')
runCommand('git push --all origin')
runCommand('git push origin --tags')
print("VERSION V1 rilasciata")

input("Premi Invio per procedere con la creazione della FEATURE 4")

runCommand('git fetch --all')
runCommand('git pull origin main')
runCommand('git flow feature start quartafeature')
runCommand("mkdir componenti")
runCommand("mv processori.md ./componenti")
runCommand("mv schede_madri.md ./componenti")
writeToFile(repopath+"/inventario.md", '''2068226
2082852

componenti
- processori.md
- schede_madri.md

Elettronica Padovana
''')
runCommand("git add inventario.md")
runCommand("git add processori.md")
runCommand("git add schede_madri.md")
runCommand("git add componenti/")
runCommand('git commit -m "aggiunta la cartella componenti"  -m "aggiornato il file inventario.md" -m "close #4"')
runCommand("git flow feature publish quartafeature")
runCommand("git flow feature finish -k quartafeature")
runCommand("git push origin develop")
print("FEATURE 4 creata")


input("Premi Invio per procedere con la creazione della FEATURE 6")

runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow feature start sestafeature')
writeToFile(repopath+"/periferiche/tastiere.md",'''2068226
2082852
''')
writeToFile(repopath+"/inventario.md", '''2068226
2082852

componenti
- processori.md
- schede_madri.md

periferiche
- tastiere.md

Elettronica Padovana
''')

runCommand("rm periferiche/empty.txt")
runCommand("git add periferiche/")
runCommand("git add tastiere.md")
runCommand("git add empty.txt")
runCommand("git add inventario.md")
runCommand('git commit -m "aggiunto il file tastiere.md" -m "rimosso il file temporaneo empty.txt" -m "aggiornato il file inventario.md" -m "close #6"')
runCommand('git flow feature publish sestafeature')
runCommand('git flow feature finish -k sestafeature')
runCommand('git push origin develop')
print("FEATURE 6 creata")


input("Premi Invio per procedere con la creazione della RELEASE V2 (Senza fare finish)")
runCommand('git fetch --all')
runCommand('git pull origin develop')
runCommand('git flow release start -F Version_2.0')
runCommand('git flow release publish Version_2.0')
runCommand('git push --all origin')
runCommand('git push origin --tags')
print("RELEASE V2 creata")
