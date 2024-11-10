import base64

with open('/Users/namgoolee/repos/deepface/myproj/haarcascade_eye.xml', 'rb') as file:
    encoded_string = base64.b64encode(file.read()).decode('utf-8')
    print(encoded_string)
