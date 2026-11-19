"""Small input-processing helpers used by the Lab 7 fuzzing exercise."""

import re


def sender_domain(email):
    """Return a normalized domain, or an empty string for invalid input."""
    if not isinstance(email, str):
        return ""

    email = email.strip()
    if email.count("@") != 1 or any(char.isspace() for char in email):
        return ""

    local, domain = email.split("@", 1)
    if not local or not domain:
        return ""
    return domain.lower()


def first_link(text):
    """Return the first HTTP link token, or an empty string when absent."""
    if not isinstance(text, str):
        return ""

    match = re.search(r"https?://\S+", text)
    return match.group(0) if match else ""


def shout_ratio(text):
    """Return the uppercase-letter ratio, using zero for invalid/empty input."""
    if not isinstance(text, str):
        return 0.0

    letters = [char for char in text if char.isalpha()]
    if not letters:
        return 0.0

    uppercase = sum(char.isupper() for char in letters)
    return uppercase / len(letters)


def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    print("Sender Domain:", sender_domain(user_input))

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    print("First Link:", first_link(user_input))

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    print("Uppercase Ratio:", shout_ratio(user_input))


if __name__ == "__main__":
    main()
