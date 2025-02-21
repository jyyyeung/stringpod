# String Pod

[![pypi](https://img.shields.io/pypi/v/stringpod.svg)](https://pypi.org/project/stringpod/)
[![python](https://img.shields.io/pypi/pyversions/stringpod.svg)](https://pypi.org/project/stringpod/)
[![Build Status](https://github.com/jyyyeung/stringpod/actions/workflows/dev.yml/badge.svg)](https://github.com/jyyyeung/stringpod/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/jyyyeung/stringpod/branch/main/graphs/badge.svg)](https://codecov.io/github/jyyyeung/stringpod)

Matching texts across languages

* Documentation: <https://jyyyeung.github.io/stringpod>
* GitHub: <https://github.com/jyyyeung/stringpod>
* PyPI: <https://pypi.org/project/stringpod/>
* Free software: MIT

## Features

* Normalize text with options
* Check if a text contains a substring

## Usage

### Contains

```bash
stringpod contains "Hello, world!" "world"
stringpod contains "  Hello, world!  " "lo, wor" --options "strip_whitespace,ignore_case"
stringpod contains "歌曲（純音樂）" "(纯音乐)" --options "ignore_chinese_variant"
```

### Normalize

```bash
stringpod normalize "Hello, World!!!"
stringpod normalize "    Hello,   World!!!" --options "all"
stringpod normalize "歌曲（純音樂）" --options "ignore_chinese_variant"
```

## Normalizer Options

* `strip_whitespace`: Strip whitespace (leading and trailing) from the text (default: `False`)
* `remove_whitespace`: Remove whitespace (all whitespace characters) from the text (default: `False`)
  * `strip_whitespace` will not be needed if `remove_whitespace` is `True`
* `ignore_chinese_variant`: Ignore Chinese variant (default: `False`)
* `ignore_case`: Ignore case (default: `False`)
  * English will be converted to lowercase
  * Chinese will be converted to simplified Chinese
* `nfkc`: Normalize to NFKC (default: `True`)

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
