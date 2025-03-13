import os
import subprocess
import time
import requests

# Configurazione GitHub
GITHUB_TOKEN = "FAKE_GITHUB_TOKEN"
REPO_OWNER = "davidebaraldo"
REPO_NAME = "test"
def create_github_issue(title, body):
    """Crea una issue su GitHub"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    data = {"title": title, "body": body}
    requests.post(url, json=data, headers=headers)

# Clonare il repository remoto se non esiste
if not os.path.exists(REPO_NAME):
    subprocess.run(["git", "clone", f"https://github.com/{REPO_OWNER}/{REPO_NAME}.git"])
os.chdir(REPO_NAME)

# Aspetta che lo sviluppatore 1 crei `develop`
while True:
    branches = subprocess.run(["git", "branch", "-r"], capture_output=True, text=True).stdout
    if "origin/develop" in branches:
        break
    print("In attesa che il primo sviluppatore crei il branch develop...")
    time.sleep(5)

subprocess.run(["git", "checkout", "develop"])
subprocess.run(["git", "pull", "--rebase", "origin", "develop"])
subprocess.run(["git", "flow", "init", "-d", "--feature", "feature/",  "--bugfix", "bugfix/", "--release", "release/", "--hotfix", "hotfix/", "--support", "support/", "-t","''"])

# 3. Creazione file schede_madri.md
create_github_issue("3 - Aggiungere Schede Madri", "Creare file schede_madri.md e aggiornare inventario.md")
subprocess.run(["git", "flow", "feature", "start", "schede_madri"])
with open("schede_madri.md", "w") as f:
    f.write("ASUS ROG STRIX B550-F\nMSI MAG Z690 TOMAHAWK\n")
with open("inventario.md", "a") as f:
    f.write("- Schede Madri\n")
subprocess.run(["git", "add", "schede_madri.md", "inventario.md"])
subprocess.run(["git", "commit", "-m", "Aggiunto file schede_madri.md"])
subprocess.run(["git", "flow", "feature", "finish", "-k", "schede_madri"])
subprocess.run(["git", "push", "origin", "develop"])

# 6. Creazione file tastiere.md
create_github_issue("6 - Aggiungere Tastiere", "Creare file tastiere.md nella cartella periferiche")
subprocess.run(["git", "flow", "feature", "start", "tastiere"])
with open("periferiche/tastiere.md", "w") as f:
    f.write("Corsair K95 RGB Platinum\nLogitech G915 TKL\n")
subprocess.run(["git", "add", "periferiche/tastiere.md"])
subprocess.run(["git", "commit", "-m", "Aggiunto file tastiere.md"])
subprocess.run(["git", "flow", "feature", "finish", "-k", "tastiere"])
subprocess.run(["git", "push", "origin", "develop"])
