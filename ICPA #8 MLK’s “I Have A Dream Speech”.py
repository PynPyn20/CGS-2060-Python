#
#Number Of Characters In The Speech
#

infile = open ("MLK Speech.txt", "r")
text = infile.read()
print(len(text))

infile.close()


#
#MLK’s “I Have A Dream Speech” First Paragraph
#

infile = open("MLK Speech.txt", "r")
outfile=open("MLK Speech First Para.txt","w")

text=infile.readline()
print(text, file=outfile)

infile.close()
outfile.close()