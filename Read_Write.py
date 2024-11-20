
path = r'C:\Users\Mxolisi\OneDrive\Desktop\My_file.text>'
text_to_text = input('Enter some text --> ')
text_to_text += '\n'

try:
    opened_file = open(path, 'w')
    opened_file.write("text_to_write")
except:
      print('An error occured')
finally:
       opened_file.close()
try:
    opened_file = open(path, 'r')
    content = opened_file.read()
except:
      print('An error occured')
finally:
      opened_file.close()  

print(content)

