<h1 align="center">
  𓂉 sphinx-lectern<br>
</h1>
<p align="center"><sub>Extensions for building lecture handouts & slides with <a href="https://www.sphinx-doc.org/en/master">Sphinx</a>.</sub></p>

<p align="center">
  Start with one document ➡️ instantly generate <b>lecture handouts and slides</b>
</p>

## 😎 Features

- Reveal.js!
- Automatic syntax highlighting with Pygments
- Show examples of console/terminal output
- Include code from external files
- Hint boxes!
- Render diagrams, graphs, math equations
- ...and more!

## ⚡️ Install

```shell
# With pipenv
pipenv install -e git+https://github.com/hackbrightacademy/sphinx-lectern.git#egg=sphinx-lectern

# With pip
pip install git+https://github.com/hackbrightacademy/sphinx-lectern.git#egg=sphinx-lectern
```

## 📚 Docs

Wanna learn more? [Check out our docs here](docs/).

Just... uh... don't be too disappointed that there's not much there 😬

```python
lectern_substitutions = {
    # Python executable & version
    "pyname": "Python 3",
    "py": "python3",
    "pyi": "`python3`",
    "pycmd": "`python3`:cmd:",
    # iPython
    "ipyname": "IPython",
    "ipy": "ipython3",
    "ipyi": "`ipython3`",
    "ipycmd": "`ipython3`:cmd:",
    # PIP
    "pipname": "Pip 3",
    "pip": "pip3",
    "pipi": "`pip3`",
    "pipcmd": "`pip3`:cmd:",
    # Virtualenv manager
    "venvname": "Virtualenv",
    "venv": "virtualenv",
    "venvi": "`virtualenv`",
    "venvcmd": "`virtualenv`:cmd:",
    # Text editor
    "editorname": "VS Code",
    "editor": "code",
    "editori": "`code`",
    "editcmd": "`code`:cmd:",
}
```
