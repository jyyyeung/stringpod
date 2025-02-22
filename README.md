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
* Parse numbers from text
* Compare pinyin of two texts

## Usage

### Contains

Check if a text contains a substring, with options.

```bash
stringpod contains "Hello, world!" "world"
stringpod contains "  Hello, world!  " "lo, wor" --options "strip_whitespace,ignore_case"
stringpod contains "歌曲（純音樂）" "(纯音乐)" --options "ignore_chinese_variant"
```

### Normalize

Normalize text to a standard form.

```bash
stringpod normalize "Hello, World!!!"
stringpod normalize "    Hello,   World!!!" --options "all"
stringpod normalize "歌曲（純音樂）" --options "ignore_chinese_variant"
```

### Normalizer Options

* `strip_whitespace`: Strip whitespace (leading and trailing) from the text (default: `False`)
* `remove_whitespace`: Remove whitespace (all whitespace characters) from the text (default: `False`)
  * `strip_whitespace` will not be needed if `remove_whitespace` is `True`
* `ignore_chinese_variant`: Ignore Chinese variant (default: `False`)
* `ignore_case`: Ignore case (default: `False`)
  * English will be converted to lowercase
  * Chinese will be converted to simplified Chinese
* `nfkc`: Normalize to NFKC (default: `True`)

### Number Parser

Parse numbers from text.

```bash
stringpod number "One hundred and twenty-three"
stringpod number "One hundred and twenty-three" --language "en"
```

### Number Parser Options

* `language`: Language of the number (default: `en`)

### Compare Pinyin

Compare pinyin of two texts.

```bash
stringpod cmp-pinyin "你好" "你号"
stringpod cmp-pinyin "你好" "你号" --options "with_tone"
stringpod cmp-pinyin "你好" "你号" --options "spoken_tone"
```

### Pinyin Options

* `with_tone`: Whether to include the tone (default: `False`)
* `spoken_tone`: Whether to use the spoken tone (default: `False`)

## Development

```bash
poetry install -E dev -E docs -E test
poetry run pre-commit install
```

### CLI Application

```bash
poetry run python -m stringpod.cli --help
```

### Python API

```bash
poetry run python -m stringpod.stringpod --help
```

### Testing

```bash
poetry run pytest # Run Pytest
poetry run python -m stringpod.stringpod -v # Run Doctests
```

## Credits

Core packages:

* [number-parser](https://github.com/scrapinghub/number-parser)
* [pypinyin](https://github.com/mozillazg/python-pinyin)
* [opencc](https://github.com/BYVoid/OpenCC)
* [jieba](https://github.com/fxsjy/jieba)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
