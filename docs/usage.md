# Usage

To use Text Match in a project

```python
import text_match
```

## Normalizer

```python
>>> from text_match import Normalizer, NormalizerOptions
>>> normalizer = Normalizer()
>>> normalizer.normalize("Hello, world!")
```

### With Options

```python
# Pass options (as a NormalizerOptions object) during initialization
>>> options = NormalizerOptions(ignore_case=True)
>>> normalizer = Normalizer(options=options)
>>> normalizer.normalize("Hello, world!")
"hello, world!"

# Pass options (as a string) during initialization
>>> normalizer_from_string = Normalizer(options="ignore_case,strip_whitespace")
>>> normalizer_from_string.normalize("Hello, world!")
"hello, world!"

# Pass options after initialization
>>> normalizer = Normalizer()
>>> normalizer.options = NormalizerOptions(ignore_case=True) # Must be a NormalizerOptions object
>>> normalizer.normalize("Hello, world!")
"hello, world!"

# Pass options during normalization (will only be applied to this normalization)
>>> normalizer = Normalizer()
>>> normalizer.normalize("Hello, world!", options=NormalizerOptions(ignore_case=True))
"hello, world!"
```

## String Contains Substring

```python
>>> from text_match import contains_substring
>>> contains_substring("Hello, world!", "world")
True
>>> contains_substring("Hello, world!", "WORLD", options="ignore_case")
True
```
