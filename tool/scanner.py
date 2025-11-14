import chardet
def load_rules(filepath):
    rules = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                rule = line.strip()
                if rule:
                    rules.append(rule)
    except FileNotFoundError:
        print("File is not found")
    return rules

def scan_file(filepath, rules):
    found = []
    try:
        with open(filepath, "rb") as raw:
            result = chardet.detect(raw.read())
            encoding = result["encoding"]

        with open(filepath, "r", encoding=encoding, errors="ignore") as file:
            content = file.read()

            for rule in rules:
                if rule in content:
                    found.append(rule)
    except FileNotFoundError:
        print("File is not found")
    return found
