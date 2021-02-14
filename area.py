PI=3.14
radius=float(input("Enter the radius of circle:"))
area=PI*radius*radius
print("area of circle = %.2f" %area)


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
