import lxml.etree as et

from from_tei import (handle_lacunae, pre_parse_cleanup, 
                         add_underdot_to_unclear_letters,
                         handle_abbr)

# namespaces
tei_ns = 'http://www.tei-c.org/ns/1.0'
xml_ns = 'http://www.w3.org/XML/1998/namespace'

def test_pre_parse_cleanup():
    _IN = '<lb n="9"/>one   <supplied>two</supplied>    t<supplied>hre</supplied>e \nfour'
    expected_out = 'one[two]t[hre]e four'
    _OUT = pre_parse_cleanup(_IN)
    assert _OUT == expected_out

def test_handle_lacunae():
    _IN = '[lac] not lac [lac] not lac [three] [words] [lac] and [pa]rt[ial]'.split()
    expected_out = '___not lac___ not lac___ and [pa]rt[ial]'.split()
    _OUT = handle_lacunae(_IN)
    print(_OUT)
    assert _OUT == expected_out

def test_add_underdot_to_unclear_letters():
    _IN = '<TEI xmlns="http://www.tei-c.org/ns/1.0"><w>εκλογη<unclear>ν</unclear></w><w><unclear>wholly</unclear></w><w>p<unclear>arti</unclear>al</w></TEI>'
    expected_out = '<TEI xmlns="http://www.tei-c.org/ns/1.0"><w>εκλογη<unclear>ν̣</unclear></w><w><unclear>ẉḥọḷḷỵ</unclear></w><w>p<unclear>ạṛṭị</unclear>al</w></TEI>'
    root = et.fromstring(_IN)
    add_underdot_to_unclear_letters(root)
    _OUT = et.tostring(root, encoding='unicode')
    assert expected_out == _OUT

def test_handle_abbr():
    _IN = '<root><w><abbr>abbreviated</abbr></w><w><abbr><ns>nomina sacra</ns></abbr></w></root>'
    expected_out = 'abbreviated nomina sacra'
    root = et.fromstring(_IN) #type: et._Element
    text = []
    for abbr in root.xpath('//abbr'):
        text.append(handle_abbr(abbr))
    _OUT = ' '.join(text)
    assert expected_out == _OUT
