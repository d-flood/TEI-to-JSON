# TEI to JSON

Convert TEI XML transcriptions to the format required by the ITSEE [Collation Editor](https://github.com/itsee-birmingham/standalone_collation_editor).

- This is not designed to convert every valid TEI encoding, nor will it yet properly convert any deeply tested encodings (e.g. an unclear abbreviated number). When the text of an element is more deeply nested than I have have anticipated so far, it is usually skipped.
- One JSON file per verse is created.
- An appropriate `metadata.json` file is also created.
- This is a new attempt from scratch; pre-release

## Requirements
- Python 3.6+
- `lxml` (https://pypi.org/project/lxml/)

## Usage
- To convert the example transcription and write the output files to the working directory, run `python tei_to_json.py example.xml`
- use the `-o` flag for designating the output directory. Filenames are assigned to the verse as it is encoded in the TEI file.

## Near Future
- Finish writing tests.
- Anticipate and support more complex arrangements of encodings.
- Incorporate this utility and [MarkdownTEI](https://github.com/d-flood/MarkdownTEI) into a standalone distributable GUI.
