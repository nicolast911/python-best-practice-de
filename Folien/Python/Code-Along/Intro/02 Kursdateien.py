# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Kursdateien</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## GitHub
#
# - [GitHub Seite](https://github.com/Coding-Academy-Munich/python-clean-code-de)
# - [Git Repository]()
# - [Zip-Archiv]()

# %% [markdown]
#
# ## Clonen und Updaten des Git Repositories
#
# - Um das Git-Repository zu klonen, geben Sie folgendes Kommando in der
#   Kommandozeile ein:
# - `git clone https://github.com/Coding-Academy-Munich/python-clean-code-de.git`
# - Um auf die neuen Änderungen zuzugreifen, geben Sie z.B. folgendes Kommando in der
#   Kommandozeile ein:
# - `git add -A && git commit -m "Update" && git pull --rebase`
# - Andere Workflows sind genau so möglich
# - Entwicklungsumgebungen wie PyCharm oder Visual Studio Code haben Git-Integrationen

# %% [markdown]
#
# ## Herunterladen und Entpacken des Zip-Archivs
#
# - [Zip-Archiv]()
# - Entpacken Sie das Zip-Archiv, bevor Sie mit den Dateien arbeiten

# %% [markdown]
#
# ## JupyterHub
#
# - [Coding-Academy JupyterHub](https://jh1.mhoezl.de/)
# - Login mit dem Namen aus Ihrer Email (vor dem `@`) in Kleinbuchstaben
# - Beim ersten Login können Sie ein Passwort festlegen
# - Bitte merken Sie sich dieses Passwort, Sie können es nicht selber
#   zurücksetzen oder ändern
# - Kursmaterial: [GitPuller Link]()

# %% [markdown]
#
# ## Struktur des Kurses
#
# - Top-level Ordner `folien` für die Folien
# - Unterrdner für verschiedene Dateiformate:
#   - `Html`: HTML-Dateien
#   - `Notebooks`: Jupyter Notebooks
#   - `Python`: Python Code mit Text der Folien als Kommentaren
# - Unterordner für Code-Alongs und vollständige Folien
# - Unterordner für Intro und jede der 4 Wochen des Kurses
# - Evtl. andere Top-level Ordner für zusätzliche Materialien

# %% [markdown]
#
# ### Top-Level Ordner
#
# ```
# Folien/
# ├── Html
# │   ├── Code-Along
# │   │   ├── Intro
# │   │   └── Woche 1
# │   └── Completed
# │       ├── Intro
# │       └── Woche 1
# ├── Notebooks
# │   ├── Code-Along
# │   │   ├── Intro
# │   │   └── Woche 1
# │   └── Completed
# │       ├── Intro
# │       └── Woche 1
# └── Python
#     ├── Code-Along
#     │   ├── Intro
#     │   └── Woche 1
#     └── Completed
#         ├── Intro
#         └── Woche 1
# ```

# %% [markdown]
#
# ### Notebooks Unterordner
#
# ```
# Notebooks/
# ├── Code-Along
# │   ├── Intro
# │   │   ├── 01 Herzlich Willkommen.ipynb
# │   │   ├── 02 Kursdateien.ipynb
# │   └── Woche 1
# │       ├── 01 Einführung ins Testen.ipynb
# │       ├── 02 Klassifizierung von Tests.ipynb
# │       └── img
# └── Completed
#     ├── Intro
#     │   ├── 01 Herzlich Willkommen.ipynb
#     │   ├── 02 Kursdateien.ipynb
#     └── Woche 1
#         ├── 01 Einführung ins Testen.ipynb
#         ├── 02 Klassifizierung von Tests.ipynb
#         └── img
# ```

