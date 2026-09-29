import json
from collections import Counter
from fugashi import Tagger

cat ./*.jsonl > combined.jsonl

INPUT="combined.jsonl"

INPUT = "combined.jsonl"
OUTPUT = "japanese-wiki.json"

NAME = "llm-jp-wikipedia"

tagger = Tagger()

chars = Counter()
bigrams = Counter()
skipgrams = Counter()
skipgrams2 = Counter()
skipgrams3 = Counter()
trigrams = Counter()


def kata_to_hira(s):
    out = []

    for ch in s:
        code = ord(ch)

        # Katakana → hiragana
        if 0x30A1 <= code <= 0x30F6:
            out.append(chr(code - 0x60))
        else:
            out.append(ch)

    return "".join(out)


def valid_char(ch):
    return (
        "\u3041" <= ch <= "\u3096"
        or ch in "、。ー"
    )


def reading_of_text(text):
    result = []

    for word in tagger(text):
        feat = word.feature
        reading = None

        for attr in ("kana", "pron"):
            if hasattr(feat, attr):
                value = getattr(feat, attr)

                if value and value != "*":
                    reading = value
                    break

        if not reading:
            reading = word.surface

        reading = kata_to_hira(reading)

        for ch in reading:
            if valid_char(ch):
                result.append(ch)

    return "".join(result)


def add_document(stream):
    # Individual characters
    chars.update(stream)

    # Adjacent characters
    for i in range(len(stream) - 1):
        bigrams[stream[i:i+2]] += 1

    # One character between
    # A _ B
    for i in range(len(stream) - 2):
        skipgrams[stream[i] + stream[i+2]] += 1

    # Two characters between
    # A _ _ B
    for i in range(len(stream) - 3):
        skipgrams2[stream[i] + stream[i+3]] += 1

    # Three characters between
    # A _ _ _ B
    for i in range(len(stream) - 4):
        skipgrams3[stream[i] + stream[i+4]] += 1

    # Adjacent trigrams
    for i in range(len(stream) - 2):
        trigrams[stream[i:i+3]] += 1


with open(INPUT, encoding="utf-8") as f:

    for line_no, line in enumerate(f, 1):
        line = line.strip()

        if not line:
            continue

        obj = json.loads(line)

        text = obj.get("text", "")

        stream = reading_of_text(text)

        if stream:
            add_document(stream)

        if line_no % 1000 == 0:
            print(f"Processed {line_no:,} documents")


char_total = sum(chars.values())
bigram_total = sum(bigrams.values())
skipgram_total = sum(skipgrams.values())
skipgram2_total = sum(skipgrams2.values())
skipgram3_total = sum(skipgrams3.values())
trigram_total = sum(trigrams.values())


def percentages(counter, total):
    if total == 0:
        return {}

    return {
        item: count / total * 100
        for item, count in counter.most_common()
    }


output = {
    "name": NAME,

    "char_total": char_total,
    "bigram_total": bigram_total,
    "skipgram_total": skipgram_total,
    "skipgram2_total": skipgram2_total,
    "skipgram3_total": skipgram3_total,
    "trigram_total": trigram_total,

    "chars": percentages(chars, char_total),
    "bigrams": percentages(bigrams, bigram_total),
    "skipgrams": percentages(skipgrams, skipgram_total),
    "skipgrams2": percentages(skipgrams2, skipgram2_total),
    "skipgrams3": percentages(skipgrams3, skipgram3_total),
    "trigrams": percentages(trigrams, trigram_total),
}


with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(
        output,
        f,
        ensure_ascii=False,
        indent="\t"
    )


print()
print("Done!")
print(f"Output: {OUTPUT}")
print()
print(f"Characters:  {char_total:,}")
print(f"Bigrams:     {bigram_total:,}")
print(f"Skipgrams:   {skipgram_total:,}")
print(f"Skipgrams 2: {skipgram2_total:,}")
print(f"Skipgrams 3: {skipgram3_total:,}")
print(f"Trigrams:    {trigram_total:,}")
