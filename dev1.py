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

# Inizializza Git Flow se non è stato ancora fatto
subprocess.run(["git", "init"])
subprocess.run(["git", "checkout", "-b", "develop"])
subprocess.run(["git", "push", "-u", "origin", "develop"])
subprocess.run(["git", "flow", "init", "-d", "--feature", "feature/",  "--bugfix", "bugfix/", "--release", "release/", "--hotfix", "hotfix/", "--support", "support/", "-t","''"])

# 1. Creazione del file inventario.md
create_github_issue("1 - Creazione file Inventario", "Creare il file inventario.md")
subprocess.run(["git", "flow", "feature", "start", "inventario"])
with open("inventario.md", "w") as f:
    f.write("## Inventario dei prodotti\n")
subprocess.run(["git", "add", "inventario.md"])
subprocess.run(["git", "commit", "-m", "Aggiunto file inventario.md"])
subprocess.run(["git", "flow", "feature", "finish", "-k", "inventario"])
subprocess.run(["git", "push", "origin", "develop"])

# 2. Creazione del file processori.md
create_github_issue("2 - Aggiungere Processori", "Creare il file processori.md e aggiornare inventario.md")
subprocess.run(["git", "flow", "feature", "start", "processori"])
with open("processori.md", "w") as f:
    f.write("Intel i9-13900K\nAMD Ryzen 9 7950X\n")
with open("inventario.md", "a") as f:
    f.write("\n- Processori\n")
subprocess.run(["git", "add", "processori.md", "inventario.md"])
subprocess.run(["git", "commit", "-m", "Aggiunto file processori.md"])
subprocess.run(["git", "flow", "feature", "finish", "-k", "processori"])
subprocess.run(["git", "push", "origin", "develop"])

# Attende che lo sviluppatore 2 completi "Schede Madri"
while not os.path.exists("schede_madri.md"):
    print("In attesa della creazione del file schede_madri.md...")
    time.sleep(5)
subprocess.run(["git", "pull", "--rebase"])

# 5. Creazione della cartella periferiche e del file mouse.md
create_github_issue("5 - Sezione Periferiche", "Creare cartella periferiche e file vuoto per Git")
subprocess.run(["git", "flow", "feature", "start", "periferiche"])
os.makedirs("periferiche", exist_ok=True)
with open("periferiche/.keep", "w") as f:
    f.write("")  # File vuoto per Git
subprocess.run(["git", "add", "periferiche/.keep"])
subprocess.run(["git", "commit", "-m", "Creata cartella periferiche"])
subprocess.run(["git", "flow", "feature", "finish", "-k", "periferiche"])
subprocess.run(["git", "push", "origin", "develop"])

create_github_issue("7 - Aggiungere Mouse", "Creare il file mouse.md nella cartella periferiche")
subprocess.run(["git", "flow", "feature", "start", "mouse"])
with open("periferiche/mouse.md", "w") as f:
    f.write("Logitech MX Master 3\nRazer DeathAdder V2\n")
subprocess.run(["git", "add", "periferiche/mouse.md"])
subprocess.run(["git", "commit", "-m", "Aggiunto file mouse.md"])
subprocess.run(["git", "flow", "feature", "finish", "-k", "mouse"])
subprocess.run(["git", "push", "origin", "develop"])
