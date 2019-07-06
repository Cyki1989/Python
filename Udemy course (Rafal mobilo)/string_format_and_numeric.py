name="Jakub"
age=29
daysInYears=365
mesage="%s is %d years old, so is about %d days old"
print(mesage%(name,age,age*daysInYears))
mesage="{0:s} is {1:d} years old, so is about {2:d} days old"
print (mesage.format(name,age,age*daysInYears))
name="Cris"
age=17
print (mesage.format(name,age,age*daysInYears))
x=1234567890
y=12345
mesage="%d divided by %d is %d and the rest is %d"
print(mesage%(x,y,x//y,x%y))
