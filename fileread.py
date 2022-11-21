# f = open("prabakaran_cv.doc",'r')
# print(f.read())

# import docx
# def readtxt(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragrapha:
#         fullText.append(para.text)
#     return '\n'.join(fullText)
# print(readtxt('prabakaran_cv.doc'))


with open('new.txt', 'r') as f:
    print(f.readline());
    with open('abc.txt', 'w') as f1:
        f1.write("mobile")
        # print(f.readline())
        for d in f:
            f1.write(d)
            f1.write(d)
print('new');






