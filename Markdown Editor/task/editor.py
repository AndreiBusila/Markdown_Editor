available_formatters = ["plain",
                        "bold",
                        "italic",
                        "header",
                        "link",
                        "inline-code",
                        "ordered-list",
                        "unordered-list",
                        "new-line"]

special_command = ["!done"]


def display():
    print("Available formatters:", end="")
    for i in range(0, len(available_formatters)):
        print(" {0}".format(available_formatters[i]), end="")
    print()
    print("Special commands:", end="")
    for i in range(0, len(special_command)):
        print(" {0}".format(special_command[i]), end="")
    print()


def command_header():
    text = ""
    while True:
        try:
            level_input = int(input("Level: "))
            if 1 <= level_input <= 6:
                text_input = input("Text: ")
                text = "#" * level_input + " " + text_input + "\n"
                break
            else:
                print("The level should be within the range of 1 to 6")
        except ValueError:
            print("The level should be within the range of 1 to 6")
    return text


def command_plain():
    plain_input = input("Text: ")
    text = "{0}".format(plain_input)
    return text


def command_bold():
    bold_input = input("Text: ")
    text = "**{0}**".format(bold_input)
    return text


def command_italic():
    italic_input = input("Text: ")
    text = "*{0}*".format(italic_input)
    return text


def command_inline_code():
    inline_input = input("Text: ")
    return "`{0}`".format(inline_input)


def command_link():
    label_input = input("Label: ")
    url_input = input("URL: ")
    text = "[{0}]({1})".format(label_input, url_input)
    return text


def command_new_line():
    return "\n"


def command_ordered_list():
    text = ""
    while True:
        try:
            number_input = int(input("Number of rows: "))
            if number_input > 0:
                for i in range(0, number_input):
                    text += "{0}. ".format(i+1) + input("Row #{0}: ".format(i + 1)) + "\n"
                break
            else:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("The number of rows should be greater than zero")
    return text


def command_unordered_list():
    text = ""
    while True:
        try:
            number_input = int(input("Number of rows: "))
            if number_input > 0:
                for i in range(0, number_input):
                    text += "* ".format(i + 1) + input("Row #{0}: ".format(i + 1)) + "\n"
                break
            else:
                print("The number of rows should be greater than zero")
        except ValueError:
            print("The number of rows should be greater than zero")
    return text


def done(text):
    file = open('output.md', 'w', encoding='utf-8')
    file.write(text)
    file.write("")
    file.close()


result_text = ""
while True:

    user_input = input("Choose a formatter: ")
    if user_input in available_formatters or user_input in special_command:
        if user_input == "!done":
            done(result_text)
            break
        if user_input == "header":
            result_text += command_header()
            print(result_text)
        if user_input == "plain":
            result_text += command_plain()
            print(result_text)
        if user_input == "bold":
            result_text += command_bold()
            print(result_text)
        if user_input == "italic":
            result_text += command_italic()
            print(result_text)
        if user_input == "link":
            result_text += command_link()
            print(result_text)
        if user_input == "new-line":
            result_text += command_new_line()
            print(result_text)
        if user_input == "inline-code":
            result_text += command_inline_code()
            print(result_text)
        if user_input == "ordered-list":
            result_text += command_ordered_list()
            print(result_text)
        if user_input == "unordered-list":
            result_text += command_unordered_list()
            print(result_text)

    else:
        print("Unknown formatting type or command")
