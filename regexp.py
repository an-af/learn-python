# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# Dengan regex, aku bisa mencocokan karakter

# -- Code --

#1. Import Re, module untuk menjalankan operasi reguler expresion
import re

#2. variabel text, text yang akan di cek
txt = "hello world somebody.."

#3. Membuat notasi reguler expresion | ^
result = re.search("^hell", txt)

if result :
    print("match")
else:
    print("no match")

# -- Code -- #
# [20 Juli 25]
