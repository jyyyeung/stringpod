from text_match.normalizer import Normalizer, NormalizerOptions


def test_normalize_default():
    normalizer = Normalizer()
    _options = normalizer.options
    assert not _options.strip_whitespace
    assert not _options.remove_whitespace
    assert not _options.ignore_chinese_variant
    assert not _options.ignore_case
    assert _options.nfkc


def test_normalize_options_from_string():
    options = NormalizerOptions.from_string('')
    assert not options.strip_whitespace
    assert not options.ignore_case

    options = NormalizerOptions.from_string('strip_whitespace,ignore_case')
    assert options.strip_whitespace
    assert options.ignore_case
    assert not options.remove_whitespace
    assert not options.ignore_chinese_variant
    assert options.nfkc


def test_normalize_enable_all():
    options = NormalizerOptions.enable_all()
    assert options.strip_whitespace
    assert options.remove_whitespace
    assert options.ignore_chinese_variant
    assert options.ignore_case
    assert options.nfkc


def test_normalize():
    normalizer = Normalizer()
    # By Default, nothing is done
    assert normalizer.normalize('Hello, world!') == 'Hello, world!'


def test_normalize_with_options():
    normalizer = Normalizer()
    options = NormalizerOptions(strip_whitespace=False)
    assert normalizer.normalize('Hello, world!', options) == 'Hello, world!'


def test_normalize_with_options_strip_whitespace():
    normalizer = Normalizer()
    options = NormalizerOptions(strip_whitespace=True)
    assert normalizer.normalize('  Hello, world!  ', options) == 'Hello, world!'
    assert normalizer.normalize('Hello, world!', options) == 'Hello, world!'


def test_normalize_with_options_remove_whitespace():
    normalizer = Normalizer()
    options = NormalizerOptions(remove_whitespace=True)
    assert normalizer.normalize('   Hello,    world!   ', options) == 'Hello,world!'
    assert normalizer.normalize('  Hello,    world!', options) == 'Hello,world!'


def test_normalize_with_options_ignore_chinese_variant():
    normalizer = Normalizer()
    options = NormalizerOptions(ignore_chinese_variant=True)
    assert normalizer.normalize('計算機', options) == '计算机'
    assert normalizer.normalize('你好，世界！', options) == '你好,世界!'
    assert normalizer.normalize('Computer', options) == 'Computer'


def test_normalize_with_options_ignore_case():
    normalizer = Normalizer()
    options = NormalizerOptions(ignore_case=True)
    assert normalizer.normalize('Hello, world!', options) == 'hello, world!'


def test_normalize_with_options_ignore_case_and_strip_whitespace():
    normalizer = Normalizer()
    options = NormalizerOptions(ignore_case=True, strip_whitespace=True)
    assert normalizer.normalize('    Hello, world!    ', options) == 'hello, world!'


def test_normalize_with_options_nfkc():
    normalizer = Normalizer()
    options = NormalizerOptions(nfkc=True)
    assert normalizer.normalize('１２３４５６７８９０', options) == '1234567890'
    assert normalizer.normalize('歌曲（伴奏）！，。', options) == '歌曲(伴奏)!,。'
    assert normalizer.normalize('㊋１ａ', options) == '火1a'
    # 左边是两个康熙字典的部首，右边是标准字体。
    assert normalizer.normalize('⼩不', options) == '小不'
