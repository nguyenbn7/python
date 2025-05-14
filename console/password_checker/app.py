from getpass import getpass
from hashlib import sha1
import sys
from requests import Response, get


def count_password_leaked(response: Response, hash_to_check: str):
    hashes = (line.split(":") for line in response.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def make_request_to_pwnedpasswords(first_5_hash_chars: str):
    url = "https://api.pwnedpasswords.com/range/" + first_5_hash_chars
    response = get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the api and try again"
        )
    return response


def get_password_leaked_count(password: str):
    hashed_password = sha1(password.encode("utf-8")).hexdigest().upper()
    first5_chars, tail = hashed_password[:5], hashed_password[5:]
    response = make_request_to_pwnedpasswords(first5_chars)
    return count_password_leaked(response, tail)


def main():
    running = True
    while running:
        password = getpass("Enter a password to check if it's leaked or not:")
        count = get_password_leaked_count(password)
        if count:
            print(
                f"Password you entered was found {count} times... you should probably change your password"
            )
        else:
            print(f"Password you entered was NOT found. Carry on!")

        cont = ""

        while cont != "y" and cont != "n":
            cont = input("Continue checking (y/N)?: ").lower()

        if cont != "y":
            running = False

            print("Good bye.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
