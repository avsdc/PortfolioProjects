# Importing Libraries..
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash
from string import punctuation
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Dictionary where keys are letters of the English alphabet, and values are a series of dots/dashes.
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '!': '-.-.--', ':': '--...', ';': '-.-.-.', '?': '..--..', '.': '.-.-.-',
                   "'": '.----.', ',': '--..--'}

# list out keys and values separately
keys_list = list(morse_code_dict.keys())
print(keys_list)
values_list = list(morse_code_dict.values())
print(values_list)

#initialize strings used in function index, textToMorseCode and MorseCodeToText

output_string = " "
out_str = " "
in_str = " "
ltr_str = " "
last_ltr_lst = " "


class MyForm(FlaskForm):
    input = TextAreaField('Input')
    output = TextAreaField('Output')
    submit = SubmitField(label='Submit')


@app.route('/', methods=['POST', 'GET'])
def index():
    global string2, string3
    form = MyForm()

    if form.validate_on_submit():
        # string1 takes a string from input text area on the form

        string1 = form.input.data

        #total_digits and total_letters determine number of digits and number of letters in string1

        total_digits = len(re.findall('[0-9]', string1))
        total_letters = len(re.findall('[A-z]', string1))

        #list comprehension to find index of last letter in each word in the string

        space = ' '
        last_ltr_lst = [pos - 1 for pos, char in enumerate(string1) if char == space]

        string1.lstrip(" ")

        # if there are letters/digits in the string, function textToMorseCode is executed, else if there are dots and dashes in the input string,
        #morseCodeToText is executed.

        if total_letters > 0 and total_digits >= 0:
            string2 = textToMorseCode(string1, last_ltr_lst)

        elif ((string1.find('.') != -1) or (string1.find('-') != -1)):
            string2 = morseCodeToText(string1)

        # index.html is rendered on the form and string2 is displayed in output textarea.
        return render_template('index.html', form=form, data=string2)
    return render_template('index.html', form=form)


def textToMorseCode(input_string, last_ltr_lst):
    global output_string
    input_string.lstrip(" ")

    for char in input_string:
        #print(f"LAST:{last_ltr_lst}")
        # print(char)
        # if char is alphanumeric, and index of char is not in the last_ltr_lst i.e. char is a letter in the beginning or middle of the word, then the
        # if block statements are executed, the output string gets concatenated with the morse code encoding for the character and a space.
        # In the else part, if character is a space, a / gets concatenated to the output string, if the character is at the end of a word, it is encoded
        # using the morse_code_dict. In all other cases, i.e. when there are punctuation marks, the morse_code_dict for punctuation gets encoded and concatenated
        # to the output_string.

        if char.isalpha() and (input_string.index(char) not in last_ltr_lst):
            char = char.upper()
            # print(char)
            output_string = output_string.strip()
            output_string = output_string + morse_code_dict[char] + " "
            #print(output_string)
        else:
            if char == " ":
                output_string = output_string + '/'
            elif char.isalpha() and (input_string.index(char) in last_ltr_lst):
                char = char.upper()
                output_string = output_string.strip()
                output_string = output_string + morse_code_dict[char]
            else:
                output_string = output_string.strip()
                output_string = output_string + morse_code_dict[char]
    return output_string


def morseCodeToText(in_str):
    global ltr_str, out_str

    # if a char in the morse code string i.e. in_str has a '.' or '-', the dot or dash gets inserted into the ltr_str. If the char is not a dot or dash,
    # in the else part if the char is a space, the ltr_str is decoded(for a key in the morse_code_dict), and key concatenated to out_str, if the char is a /,
    # ltr_str is decoded, and key and a space is concatenated to the out_str. The ltr_str for the punctuation mark at the end of the string is decoded after
    # the for loop execution completes, and out_str is returned from the morseCodeToText function.

    for char in in_str:
        if char == '.' or char == '-':
            ltr_str = ltr_str + char
            #print(ltr_str)
        else:
            if char == " ":
                # print key with val ltr_str
                ltr_str = ltr_str.lstrip(" ")
                pos = values_list.index(ltr_str)
                #print(keys_list[pos])
                out_str = out_str + keys_list[pos]
                out_str.strip(" ")
                #print(f"space:{out_str}")
                ltr_str = " "
            elif char == "/":
                # print key with val ltr_str
                ltr_str = ltr_str.lstrip(" ")
                pos = values_list.index(ltr_str)
                #print(keys_list[pos])
                out_str = out_str + keys_list[pos] + " "
                out_str.strip(" ")
                #print(f"slash: {out_str}")
                ltr_str = " "


    ltr_str = ltr_str.lstrip(" ")
    pos = values_list.index(ltr_str)
    #print(keys_list[pos])
    out_str = out_str + keys_list[pos]
    out_str.strip(" ")
    out_str.capitalize()
    #print(f"punc:{out_str}")

    return out_str


if __name__ == '__main__':
    app.run()
