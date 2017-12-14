import urllib.request
import urllib.parse

def check_profanity(text_to_check):
    """
    Check profanity words from a text file
    Connect to:
    "http://wdylike.appspot.com/?q="
    to check for profanity
    :param text_to_check: text to check
    :return: True or False
    """
    url_api = "http://wdylike.appspot.com/?q="
    conn = urllib.request.urlopen(url_api + urllib.parse.quote(text_to_check))

    out = conn.read()
    if out.decode('utf-8') == "false":
        return False
    else:
        return True


def read_text():
    with open('movie_quotes.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            # Call check profanity
            if check_profanity(line.strip()):
                print("profanity alert")
            else:
                print("This line in document has no curse words")


def main():
    """
    Test Function
    """
    read_text()


if __name__ == '__main__':
    main()
    exit(0)
