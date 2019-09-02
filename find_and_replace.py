#!/usr/bin/python
# -*- coding: utf-8 -*- 
import fileinput

OPERATIONS = {
      '🍡': "add",
      '🤡': "clone",
      '📐': "divide",
      '😲': "if_zero",
      '😄': "if_not_zero",
      '🏀': "jump_to",
      '🚛': "load",
      '📬': "modulo",
      '⭐': "ultiply",
      '🍿': "pop",
      '📤': "pop_out",
      '🎤': "print_top",
      '📥': "push",
      '🔪': "sub",
      '🌓': "xor",
      '⛰': "ump_top",
      '🥇': "acc1",
      '🥈': "acc2",
      '1️⃣': "1",
      '0️⃣': "0", 
      '6️⃣': "6",
      '2️⃣': "2",
      '3️⃣': "3",
      '5️⃣': "5",
      '8️⃣': "8",
      '7️⃣': "7",
      '9️⃣': "9",
      '4️⃣': "4",
      '⌛': "exit"
  }

text = "my_list.txt"
#fields = {"Adding": "BBBB", "python": "CCCC"}
fields = OPERATIONS
tmp_file = "tmp_file.txt"
w = open(tmp_file, 'w', encoding="utf8")

for line in open(text, 'r', encoding="utf8"):
    for f_key, f_value in fields.items():
            if f_key in line.rsplit():
                line = line.replace(f_key, f_value)
                w.write(line + " ")
            #w.write("\n")
    
w.close()