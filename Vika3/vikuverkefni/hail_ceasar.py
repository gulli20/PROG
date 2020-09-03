# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~") # 126

# Every transmission starts with the line "Hail Caesar!" so the first letter, 
# once decrypted, must be H.
first_letter = line1[0]
# ...now find out what the key is
enc_letter = ord(first_letter)
h_ord = ord('H')
shift = h_ord - enc_letter
# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    # ... and the rest is up to you
    for j in line:
        enc_letter = ord(j)
        ascii_nr = enc_letter + shift
        if ascii_nr > HIGH:
            ascii_nr = ascii_nr - HIGH + (LOW - 1)
        elif ascii_nr < LOW:
            ascii_nr = (LOW - ascii_nr) - HIGH 
        dec_letter = chr(ascii_nr)
        print(dec_letter, end='')
    print()