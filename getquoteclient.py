from getquote import quoteoftheday


qml = 85 #Quote Max Lenght - can be set by caller for example.


qll = qml +1 
while qll >= qml:
    quote = quoteoftheday()
    qll = len(quote.quote_text)
    print("******************************")
    print("getting a quote under "+str(qml)+" lenght")
    print("current lenght is "+str(qll)+"\n")
print("final lenght is "+str(qll))

#print("Now trying to slice the text in chunks")
text_max = len(quote.quote_text)

text_line_max = 34 # Max number of chars per line
text_line = []
textbuffer = ""
#Split the quote into words in an array
quote_words = quote.quote_text.split()
# print(quote_words)
wl = len(quote.quote_text)
#See if the total is larger than the text_line_max value set.
if text_max > text_line_max:
    l = 0
    ql = len(quote_words)
    while l < ql:
        textbuffer = textbuffer + quote_words[l] + " "
        l += 1
        #print(textbuffer)
        if len(textbuffer) > text_line_max:
            text_line.append(textbuffer)
            textbuffer = ""
        #print(l)
    if (len(textbuffer)):
        text_line.append(textbuffer)    
else :
    text_line.append(quote.quote_text)

# Get number of arrays generated    
qs = len(text_line)
qc = 0
while qc < qs:
    print(text_line[qc])
    qc += 1
print("- "+quote.quote_author)


