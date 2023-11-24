contents = ["AWS Solutions Architect", "Python", "Linux"]

filenames = ["AWS Study Guide.txt", "Python Bootcamp.txt", "Linux guide.txt"]

"""The zip() function returns a zip object, which is an iterator of tuples where 
the first item in each passed iterator is paired together, and then the second item in each 
passed iterator are paired together etc."""

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)