import bibtexparser
import sys
import os

# Blacklist fields (BibDesk + JabRef noise)
BLACKLIST_FIELDS = {
    "date-added", "date-modified", "priority", "file", "bdsk-url-1",
    "owner", "timestamp", "groups", "rating", "readstatus"
}

def clean_bib(input_file, output_file):
    if os.path.exists(output_file):
        raise FileExistsError(f"Output file already exists: {output_file}")

    with open(input_file, encoding="utf-8") as f:
        bib_db = bibtexparser.load(f)

    for entry in bib_db.entries:
        for field in list(entry.keys()):
            if field in BLACKLIST_FIELDS:
                del entry[field]

    with open(output_file, "w", encoding="utf-8") as f:
        bibtexparser.dump(bib_db, f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 clean_bib.py input.bib output.bib")
    else:
        clean_bib(sys.argv[1], sys.argv[2])