# Template

This repository is template for [pumpkin.py] module repositories.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

## \_\_init\_\_.py

This file MUST be present in your repository.

Three values are required: 

- `__all__`: A tuple of all modules included in the repository. Every string in the tuple has to have its module directory.
- `__name__`: Name of the repository. It has to be unique and can only contain lowercase ASCII letters and a dash (`[a-z-]+`) and MUST NOT be `core` or `base`. If a repository of this name already exists, the bot will refuse it. Check the [pumpkin.py] for the list of known third-party repositories. Moderators can run the **repository list** command to show what repositores are available.
- `__version__`: Version of your repository. This MUST follow the [semver](https://semver.org/) rules.

## README.md

The readme SHOULD be present in your repository.

In this file, you should describe the reasoning for creation of the repository and its modules.

The pumpkin.py ignores this file.

## CHANGELOG.md

The changelog SHOULD be present in your repository.

For each version you create, you MUST add a second-level heading with the version number and a text content, which SHOULD be a list, but MAY be just a plain text. See the example [CHANGELOG.md](CHANGELOG.md) file.

Future versions of pumpkin.py may parse this file in order to display changelog information.

## requirements.txt

The requirements file MAY be present in the repository.

If the file exists, the bot will use standard python tools to install packages from this file. You MUST NOT add packages you are not using in your modules. Use `requirements-dev.txt` for development packages.

The pumpkin.py installs packages specified in this file.

## (module directory)

For every module specified in the `__all__` variable you MUST create a directory with a `__init__.py` file.

This file is used by the bot to load the modules (cogs), so it has to include the discord.py's `setup()` function.

You MUST include any files required for your modules to work here, or have them linked as URLs.

---

As pumpkin.py develops, this file will be updated with Github Actions or database examples.

[pumpkin.py]: https://github.com/Pumpkin-py/pumpkin.py
