# Text Match

[![pypi](https://img.shields.io/pypi/v/text-match.svg)](https://pypi.org/project/text-match/)
[![python](https://img.shields.io/pypi/pyversions/text-match.svg)](https://pypi.org/project/text-match/)
[![Build Status](https://github.com/jyyyeung/text-match/actions/workflows/dev.yml/badge.svg)](https://github.com/jyyyeung/text-match/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/jyyyeung/text-match/branch/main/graphs/badge.svg)](https://codecov.io/github/jyyyeung/text-match)

Matching texts across languages

* Documentation: <https://jyyyeung.github.io/text-match>
* GitHub: <https://github.com/jyyyeung/text-match>
* PyPI: <https://pypi.org/project/text-match/>
* Free software: MIT

## Features

* Normalize text with options
* Check if a text contains a substring

## Usage

### Contains

```bash
text-match contains "Hello, world!" "world"
text-match contains "  Hello, world!  " "lo, wor" --options "strip_whitespace,ignore_case"
text-match contains "歌曲（純音樂）" "(纯音乐)" --options "ignore_chinese_variant"
```

### Normalize

```bash
text-match normalize "Hello, World!!!"
text-match normalize "    Hello,   World!!!" --options "all"
text-match normalize "歌曲（純音樂）" --options "ignore_chinese_variant"
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
