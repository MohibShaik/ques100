# Define a class, which have a class parameter and have a same instance parameter.

class student:
    name="person"
    def __init__(self,name=None):
        self.name=name

sujitha=student("sujitha")
print ("%s name is %s" % (student.name, sujitha.name))

obj=student()
obj.name="Mohib"
print("%s name is %s" % (student.name, obj.name))
