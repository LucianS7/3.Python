def main():
    userinput = input ("Please type input: ")
    print (convert(userinput))

def convert(txtc):
    txtc = txtc.replace (":)","🙂")
    txtc = txtc.replace (":(","🙁")
    return txtc

main()
