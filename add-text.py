with open("Fruits.txt","a+") as myfile:  #a+ to append the text and also to read the file
    myfile.write("\nOkra")
    myfile.seek(0)  #To place the cursor at 0th position
    content=myfile.read()
print(content)