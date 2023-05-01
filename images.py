import binascii

# Open in binary mode (so you don't read two byte line endings on Windows as one byte)
# and use with statement (always do this to avoid leaked file descriptors, unflushed files)
with open('1790ad43-f2f6-4d18-b16f-2ee497b2aef5.png', 'rb') as f:
    # Slurp the whole file and efficiently convert it to hex all at once
    hexdata = binascii.hexlify(f.read())
    # Print the hex data
    print(hexdata)