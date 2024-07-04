import pywhatkit as pw

text = input("Enter text:")

pw.text_to_handwriting(text, "hw.png", [0,0,138])
print("Done!")