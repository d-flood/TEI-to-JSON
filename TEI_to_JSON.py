import lxml.etree as et

from to_json import verse_to_dict, save_tx
from from_tei import (get_file, pre_parse_cleanup,
                      add_underdot_to_unclear_letters,
                      parse, remove_unclear_tags,
                      tei_ns, get_verse_as_tuple)

###########################################################
###########################################################
# main

text = get_file('tx.xml')
text = pre_parse_cleanup(text)
root = parse(text)
add_underdot_to_unclear_letters(root)
text = et.tostring(root, encoding='unicode')
text = remove_unclear_tags(text)
root = parse(text)
# write_xml(root)
hands = ['firsthand', 'corrector']
siglum = root.xpath('//tei:title', namespaces={'tei': tei_ns})[0].get('n')
verses = root.xpath(f'//tei:ab', namespaces={'tei': tei_ns})
for verse in verses:
    ref = verse.get('n')
    witnesses = get_verse_as_tuple(verse, hands=hands)
    # print(witnesses)
    verse_as_dict = verse_to_dict(siglum, ref, witnesses)
    save_tx(verse_as_dict, ref)
