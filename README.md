# Home Scripts

General scripts and tools to be used for "home routines" as helpers or to automate some tasks.

## General Structure

### Scripts

The repository presents **standalone scripts**, each one at a folder named as the OS/Language they need:

- **py3**: Python scripts. Each script presents in their main docstring the instructions to use it as well as the requirements for the script to run.
- **win**: Windows batch scripts. They can be run as-is, although some might take for granted some assumption.

> Within each folder there is also a 'Readme.md' file with a TOC and clarifying all scripts.
 
### Installable utils

The repository also presents the **`home-utils` Python package**, 
which presents extra python objects that I find useful for developing, debugging and testing code.

The repository presents a `pyproject.toml` file that allows to install the utils.
To do so, run the following command:

```
pip install git+https://github.com/Jtachan/HomeScripts.git
```
