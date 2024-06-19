zero = "###\n# #\n# #\n# #\n###"
one = "#\n#\n#\n#\n#"
two = "###\n  #\n###\n#  \n###"
three = "###\n  #\n###\n  #\n###"
four = "# #\n# #\n###\n  #\n  #"
five = "###\n#  \n###\n  #\n###"
six = "###\n#  \n###\n# #\n###"
seven = "###\n  #\n  #\n  #\n  #"
eight = "###\n# #\n###\n# #\n###"
nine = "###\n# #\n###\n  #\n###"

dictionary = {'0':zero,'1':one,'2':two,'3':three,'4':four,'5':five,'6':six,'7':seven,'8':eight,'9':nine}
InputNumValue=(input("Enter a number:"))
StringConvInputNumValue=str(InputNumValue)
for i in StringConvInputNumValue:
    if i in dictionary.keys():
        print(dictionary[i])
