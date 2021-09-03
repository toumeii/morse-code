mc_letters_numbers = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}
mc_punctuation = {
    '&': '.-...',
    "'": '.----.',
    '@': '.--.-.',
    ')': '-.--.-',
    '(': '-.--.',
    ':': '---...',
    ';': '-.-.-.',
    ',': '--..--',
    '=': '-...-',
    '!': '-.-.--',
    '.': '.-.-.-',
    '-': '-....-',
    '_': '..--.-',
    '$': '...-..-',
    '*': '-..-',
    '+': '.-.-.',
    '"': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    ' ': '|'
}

print('Morse Code Generator')
print('\nNote: Words will be separated by a "|"\n')

text = input('Type in what you want to turn into Morse Code:\n').upper()

morse = ''
invalid = ''
check = True
for character in text:
    if character not in mc_letters_numbers:
        if character not in mc_punctuation:
            check = False
            invalid += character

if check:
    for char in text:
        if char in mc_letters_numbers:
            morse += mc_letters_numbers[char] + ' '
        elif char in mc_punctuation:
            morse += mc_punctuation[char] + ' '
if morse == '':
    print(f'There was an invalid character({invalid}). Please try again.')
else:
    print(morse)
