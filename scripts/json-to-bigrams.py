import json
from collections import Counter
from fugashi import Tagger

INPUT = "0001.jsonl"
OUTPUT = "kana-bigrams.tsv"

tagger = Tagger()

def kata_to_hira(s):
    out = []
    for ch in s:
        code = ord(ch)
        if 0x30A1 <= code <= 0x30F6:
            out.append(chr(code - 0x60))
        else:
            out.append(ch)
    return "".join(out)

def reading_of_text(text):
    result = []

    for word in tagger(text):
        feat = word.feature

        # UniDic usually exposes kana/pronunciation fields.
        reading = None

        for attr in ("kana", "pron"):
            if hasattr(feat, attr):
                value = getattr(feat, attr)
                if value and value != "*":
                    reading = value
                    break

        if not reading:
            # Keep already-kana surface forms
            reading = word.surface

        reading = kata_to_hira(reading)

        for ch in reading:
            if (
                "\u3041" <= ch <= "\u3096"
                or ch in "、。ー"
            ):
                result.append(ch)

    return "".join(result)

counts = Counter()

with open(INPUT, encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        line = line.strip()

        if not line:
            continue

        obj = json.loads(line)
        text = obj.get("text", "")

        reading = reading_of_text(text)

        for a, b in zip(reading, reading[1:]):
            counts[a + b] += 1

        if line_no % 1000 == 0:
            print(f"Processed {line_no:,} documents")

total = sum(counts.values())

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("rank\tbigram\tcount\tpercentage\n")

    for rank, (bigram, count) in enumerate(counts.most_common(), 1):
        pct = count / total * 100
        f.write(f"{rank}\t{bigram}\t{count}\t{pct:.6f}\n")

print(f"Done: {OUTPUT}")
print(f"Total bigrams: {total:,}")
