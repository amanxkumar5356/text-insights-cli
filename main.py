import re
from collections import Counter

STOP = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
        "in", "is", "it", "of", "on", "or", "the", "to", "was", "with"}

def analyze(text):
    words = re.findall(r"\\b[\\w']+\\b", text.lower())
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    paragraphs = [p for p in re.split(r"\\n\\s*\\n", text.strip()) if p.strip()]
    common = Counter(w for w in words if w not in STOP).most_common(5)
    return {
        "Characters": len(text),
        "Characters without spaces": len(re.sub(r"\\s", "", text)),
        "Words": len(words),
        "Sentences": len(sentences),
        "Paragraphs": len(paragraphs),
        "Average word length": round(sum(map(len, words)) / len(words), 2) if words else 0,
        "Most common words": common,
    }

def main():
    print("TEXT INSIGHTS CLI")
    print("Paste your text. Type END on a separate line when finished.\\n")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    report = analyze("\\n".join(lines))
    print("\\n--- REPORT ---")
    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
