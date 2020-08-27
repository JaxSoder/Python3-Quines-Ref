#Quick writeup on Python Quines to help me not forget this interesting topic. 



#This makes a string named "te" and prints it taking in "te" again using the % and prints #out "%s" at the end because it doesnt have another variable to take in.
#NOTE: "%r" has to be used to take in RAW input. "%s" works but Quotes will be ignored

te ="example %r"
print(te%te)

#OP: [ example 'example %r' ]


#This makes a string "tp" and inside it has a "tp=%r;" allowing it to pass the entire raw string again like above.
tp = "tp=%r; print(tp%%tp)"
print(tp%tp)

#OP: [ tp='tp=%r; print(tp%%tp)'; print(tp%tp) ]

te = "te=%r; i = 25; s = 'Hello, World'; print(te%%te)"
i = 25
s = 'Hello, World'
print(te%te)

#[ te="te=%r; i = 25; s = 'Hello, World'; print(te%%te)"; i = 25; s = 'Hello, World'; print(te%te) ]

#This is a interesting because you can gather the source code of a program without the traditional writing and reading from a exteral file. Everything is internal and confined