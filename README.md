[![Actions Status](https://github.com/evg671ZXC/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/evg671ZXC/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/5d6233e935c3dad8a66e/maintainability)](https://codeclimate.com/github/evg671ZXC/python-project-49/maintainability)

<h1>Brain-games</h1>

This pack of five mini-games is designed to get your brain working

<h2>Links</h2>

This project was built using these tools:
| Tool          | Version         | Description                                         |
|:-------------:|:---------------:|:----------------------------------------------------|
|[poetry](https://python-poetry.org/)|"1.7.1"          | Python dependency management and packaging made easy|
|[pip](https://pypi.org/project/pip/)|"23.3.2"| Package installer for python                        |
|[prompt](https://pypi.org/project/prompt/)|"^0.4.1"         | Prompt and verify user input on the command line    |
<h2>Installation and how to use</h2>

*Tested on CPython 3.10*

#### Cloned this repository into its current folder:
```
git clone https://github.com/evg671ZXC/python-project-49.git
```
#### For the package to work correctly it is necessary to use [Poetry](https://python-poetry.org/):

**If this setting is not needed, run the command:*
```
poetry config virtualenvs.in-project true
```
#### After execution, commands from the [Makefile](https://guides.hexlet.io/ru/makefile-as-task-runner/) will become available to us:
**It is recommended not to install third-party packages in the global environment*
```
make install
```

#### This command collects archives of source code:
```
make build
```
#### To install a package from the operating system, use the command:
```
make package-install
```
### Let's check that everything was installed correctly:
```
brain-games
```

<h2>Description</h2>

```
brain-even
```

*Game to find the parity of a number*

[![asciicast](https://asciinema.org/a/MY2JsDQBLqTH1ZFvSofIZZvUQ.svg)](https://asciinema.org/a/MY2JsDQBLqTH1ZFvSofIZZvUQ)

```
brain-calc
```

*Game «add in your mind»*

[![asciicast](https://asciinema.org/a/Dx5tkQ0AsbKzkQjivGt940lPi.svg)](https://asciinema.org/a/Dx5tkQ0AsbKzkQjivGt940lPi)

```
brain-gcd
```

*Find the greatest common divisor*

[![asciicast](https://asciinema.org/a/KRjzL0i4uFgsRYDRavJfUC2xD.svg)](https://asciinema.org/a/KRjzL0i4uFgsRYDRavJfUC2xD)

```
brain-progression
```

*Here you will try to find the missing term of the arithmetic progression*

[![asciicast](https://asciinema.org/a/Y1X9V3GSnbvsWEXA1p4LEVIe9.svg)](https://asciinema.org/a/Y1X9V3GSnbvsWEXA1p4LEVIe9)

```
brain-prime
```

*Try to find a prime number from the given numbers*

[![asciicast](https://asciinema.org/a/eVpMnzLkPtFoHVQ4cW99m8UlB.svg)](https://asciinema.org/a/eVpMnzLkPtFoHVQ4cW99m8UlB)

### brain-games all

[![asciicast](https://asciinema.org/a/fSWR3KR2pxK5ghBRhOW62bJjC.svg)](https://asciinema.org/a/fSWR3KR2pxK5ghBRhOW62bJjC)