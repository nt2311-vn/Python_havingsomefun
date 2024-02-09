def remove_line(line):
    local_line = str(line)
    local_line = local_line.strip("#")

    def remove_aterisk(word):
        local_word = str(word)
        local_word = local_word.lstrip("*").lstrip()
        local_word = local_word.rstrip("*").rstrip()

        return local_word

    return " ".join(map(lambda word: remove_aterisk(word), local_line.split()))


def markdown_to_text(doc_content):
    local_content = doc_content.split("\n")

    return "\n".join(map(lambda line: remove_line(line), local_content))


def main():

    print(
        markdown_to_text(
            """
# Header 1

This is a **bold statement**

I am #1

This is just plain text. No special markdown.

 

* This is a list

* lists don't need to change

 

Well sh*t.

"""
        )
    )


main()
