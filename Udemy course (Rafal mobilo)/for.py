##dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
##for d in dictionary:
##    print(d,dictionary[d],sep=':\t')
##
##dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
##for k,v in dictionary.items():
##    print(k,v,sep=':\t')

text='''Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.'''

list=text.replace('\n',' ').split(' ')
dict={}
for l in list:
    if not dict.get(l):
        dict[l]=1
    else:
        dict[l]+=1
else:
    for k,v in dict.items():
        print(k,v)


 
