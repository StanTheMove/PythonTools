from scanner import load_rules, scan_file
def main():
    rules_path = 'rules.txt'
    test_file_path = 'testfile/yara_23.exe'

    rules = load_rules(rules_path)

    found_rules = scan_file(test_file_path, rules)

    file_name = test_file_path.split('/')[-1]

    if not found_rules:
        print("File is clean")
    else:
        print(f"File is infected with rules: {', '.join(found_rules)}")

if __name__ == "__main__":
    main()