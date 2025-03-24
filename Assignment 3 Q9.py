import re


def extract_emails(text):
    email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(email_pattern, text)


def validate_date(date_str):
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return re.fullmatch(date_pattern, date_str) is not None


def replace_word(input_str, old_word, new_word):
    word_pattern = r'\b{}\b'.format(re.escape(old_word))
    return re.sub(word_pattern, new_word, input_str)


def split_string(input_str):
    return [part for part in re.split(r'[^a-zA-Z0-9]+', input_str) if part]


# Example usage
if __name__ == "__main__":
    # Part I: Extract emails
    sample_text = "Contact us at smahlangu@afcholdings.co.zw or support@afcholdings.co.zw. Invalid email@invalid."
    print("Extracted emails:", extract_emails(sample_text))

    # Part II: Validate dates
    valid_date = "2019-05-22"
    invalid_date = "2019-05-225"
    print(f"'{valid_date}' is valid:", validate_date(valid_date))
    print(f"'{invalid_date}' is valid:", validate_date(invalid_date))

    # Part III: Replace words
    original_str = "Old habits die hard"
    replaced_str = replace_word(original_str, "habits", "patterns")
    print("Original string:", original_str)
    print("Replaced string:", replaced_str)

    # Part IV: Split string
    test_str = "Oh! what an amazing day!"
    split_result = split_string(test_str)
    print("Split result:", split_result)