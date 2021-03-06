# Environment

## Architecture

Pyslvs is a Graphical User Interface (GUI) program written in Python.
After installed Python launcher on your platform,
the programming script can be compiled as an executable file.

In development state, Pyslvs including several dynamic libraries,
which are need to be compiled first.

## Python Versions

The module `pyslvs-ui` and its kernel `pyslvs` support pre-built libraries for at least three platforms.

The actual test and deployment platforms on CI/CD service:

| Platforms (64-bit) | Windows | macOS | Ubuntu |
|:------------------:|:-------:|:-----:|:------:|
| Python 3.8 | O | O | O |
| Python 3.9 | O | O | O |

**Other platforms must build from source and take care about the Python dependencies.**

## Editable Mode

Pyslvs-UI and its kernel are follow PEP 517 with `pip` tool.
The package and dependencies can be installed through:

```bash
pip install -e .
```

Extra requirements can be installed through:

```bash
pip install -e .[scipy,slvs]
```

During developing, we can add a `--no-deps` option to update our package without to checking dependencies.

### Ubuntu and macOS

It is recommended to use [pyenv](https://github.com/pyenv/pyenv),
which will be more easier to handle Python version instead of using system Python.
So any operation about Python will not required `sudo` or `--user` option.

```bash
# Install supported version of Pyslvs
# The devlopment tools need to prepare first (like openssl, sqlite3)
pyenv install --list  # show all available versions
pyenv install 3.8.0
pyenv global 3.8.0
python --version  # Python 3.8.0
pip --version  # pip 19.2.2 from /home/user/.pyenv/versions/3.8.0/lib/python3.8/site-packages/pip (python 3.8)
```

### Windows

+ [Pyenv-win](https://github.com/pyenv-win/pyenv-win)
+ [Official Python](https://www.python.org) for Windows 64 bit.

Shell script tool: Git bash, [MinGW] or [Msys 2].

Dummy name `PYTHON_PATH` is a location where your Python installed.

+ Use `where python` command to find the executable path directly.
+ The path might be `~\.pyenv\pyenv-win\versions\3.x.x` if you installed by pyenv-win.
+ Virtual environment will be subject to the original location where you installed.

=== "Visual C++"
    Install from [official website](https://visualstudio.microsoft.com/downloads).

    ```batch
    REM Apply patches
    platform\set_pycompiler.bat %PYTHON_PATH% msvc
    ```

=== "Msys"
    Use [Msys 2] and [MinGW] 64-bit,
    they also can be installed by Windows package manager [Chocolatey](https://chocolatey.org/).

    ```batch
    REM The program path should be added in to environment variable (with administrator).
    setx Path "C:\tools\msys64\usr\bin;%Path%" /M
    ```

    ```bash
    # Install tools for Msys.
    # Open the "mingw64.exe" shell.
    choco install msys2

    # Install MinGW
    pacman -S mingw-w64-x86_64-gcc

    # Install patch
    pacman -S patch

    # Run as an executable
    ./platform/set_pycompiler $PYTHON_PATH mingw32
    ```

[Msys 2]: http://www.msys2.org/
[MinGW]: https://sourceforge.net/projects/mingw-w64/

### Qt Designer (Development)

PyQt5 and its additional modules are now packed into the wheel file that most of platform can install them directly.

You need to get original Qt tools for development, which can be used to design the *.ui files,
they are not the requirement if you just want to run Pyslvs.

Download and install [Qt5] to get the tools.

=== "Ubuntu"
    ```bash
    sudo apt install qttools5-dev-tools
    ```

=== "Windows"
    ```bash
    pip install pyqt5-tools
    ```

### Fcitx QIMPanel Plugins on Linux

The Fcitx input method support is depanded on the plugins of PyQt.
Copy the libraries from `/usr/lib/x86_64-linux-gnu/qt5/plugins/` into `python/site-packages/PyQt5/Qt/plugins/`.

The plugins is `platforminputcontexts/libfcitxplatforminputcontextplugin.so`.

!!! warning
    Please note that some PyQt plugins are version depended,
    so the AppImage distributions are exclude these supports.

## Kernels Requirement

About the development tools, please see [Editable Mode](#editable-mode).

### Pyslvs Kernel

[Pyslvs] is the core library of this project.
The version should be same as Pyslvs-UI.

It's a critical dependency of Pyslvs-UI.

```bash
pip install pyslvs
```

### Python-Solvespace Kernel

[Python-Solvespace] is a Python binding of [Solvespace] geometric constraint solver,
which is an extra solver option of Pyslvs-UI.

It can be installed through two ways:

```bash
pip install pyslvs-ui[slvs]
pip install python-solvespace
```

## Distributions

Packing Pyslvs-UI into no Python environment.

### Ubuntu

Use shell command to pack into [AppImage].
Because of it is more suitable with PyQt module than [PyInstaller].

After following operation, the executable file is in a folder named `out`.
The script also install `virtualenv` automatically if no executable command.

!!! warning
    Check the `glibc` version from `ldd --version`,
    it must be equal or higher than package's.

### Windows and macOS

Use [PyInstaller] with `virtualenv`, they will install automatically if no executable command.

After following operation, the executable file is in a folder named `dist`.

!!! note
    The Windows platform version requirement is same as the Python that packed.

On macOS, PyInstaller will generate two executable files (refer [here](https://pyinstaller.readthedocs.io/en/stable/usage.html#building-mac-os-x-app-bundles)).

```bash
# Run Unix-like executable file.
# Can not run it directly in Finder.
./executable --use-arguments-here

# Run macOS app file. (Can not use any arguments)
# Same as double click it in Finder.
open ./executable.app
```

!!! warning
    The version of macOS must be equal or higher than executable's.

## Documentation

This documentation is built by [MkDocs](https://www.mkdocs.org/).

If you want to demo the site in localhost, install MkDocs and the documentation requirements.

```bash
pip install mkdocs
pip install -r doc-requirements.txt
```

Start the local server:

```bash
mkdocs serve
```

The file `mkdocs.yml` and the contents of directory `docs` is a MkDocs project.
The markdown files are the resources of this site.

[PyInstaller]: https://www.pyinstaller.org/
[Solvespace]: http://solvespace.com
[Qt5]: https://www.qt.io/download/
[AppImage]: http://appimage.org

[Python-Solvespace]: https://github.com/KmolYuan/solvespace/tree/python
[Pyslvs]: https://github.com/KmolYuan/pyslvs
