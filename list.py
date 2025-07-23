#
# a list of list
matrix = [[0,1],[3,4]]

#a list of numbers from 0 to 20
numbers = list(range(20))
print(numbers)

#print every characters in a list
example = list("HONG")
print(example)

#print the last index in a list
print(matrix[-1])

#change from small letter to capital letter
example1 = ["a","b","c","d"]
#example1[-1] = "B"
print(example1)

#print from 1st index to the next 3 element
print(example1[0:3])

#create list from 0 to 10
example4 = list(range(11))

#take every other element
print(example4[::2])

#example5
example5 = ["A","B","C"]
print(example5[::2])

#unpacking list
example6 = [1,2,3,4,4,4,4,5]
first, second, *other =example6
print(first)
print(other)

#list of 2 elements
hannah_parker_phones = ["+1 978-385-3123", "+1 610-684-1514"]
tim_neely_phones = ["+1 503-831-5725", "+1 530-832-3841"]
print(tim_neely_phones[-1])
print("Phone Number of Dr. Hannah Parker:", hannah_parker_phones)
#print the first phone
print("prefered Phone Number of Dr. Hannah Parker:", hannah_parker_phones[0])

hannah_parker_emails = ["hannahp@unk.edu", "hannah7897@gmail.com"]
print("Preferred Email of Dr. Hannah Parker:", hannah_parker_emails[0])
print(hannah_parker_emails[-1])
print(hannah_parker_emails[-2])

hannah_parker_interests = {"topology", "applied mathematics", "number theory"}
tim_neely_interests = {"statistics", "labor economics", "applied mathematics", "medieval literature"}
matt_harford_interests = {"software development", "statistics", "applied mathematics", "number theory"}
mithuna_patel_interests = {"quantum mechanics", "general relativity"}

tim_neely_emails = ["tim@mij.edu", "neelo@outlook.com"]
matt_harford_phones = ["+44 07872-179187", "+44 01279-877139"]
matt_harford_emails = ["statistics@nru.ac.uk", "mattharx@yahoo.co.uk"]
mithuna_patel_phones = ["+61 (08)87150531", "+61 (08)90881262"]
mithuna_patel_emails = ["mithuna.patel@nua.edu.au", "pattmit66@gmail.com"]

hannah_parker = [hannah_parker_phones, hannah_parker_emails, hannah_parker_interests]
tim_neely = [tim_neely_phones, tim_neely_emails, tim_neely_interests]
matt_harford = [matt_harford_phones, matt_harford_emails, matt_harford_interests]
mithuna_patel = [mithuna_patel_phones, mithuna_patel_emails, mithuna_patel_interests]

# Inspecting hannah_parker
print("Information about Dr. Hannah Parker:", hannah_parker)

# This is a list of lists that have lists inside!
directory = [
    hannah_parker,
    tim_neely,
    matt_harford,
    mithuna_patel
]

#print(directory)
print("This is Hannah Parker Interest",hannah_parker_interests)
print("this is Hannah Parker Phone Number", hannah_parker_phones)

#this is a set inside a list
example7 = [1,2, {"amazon","smbc","hsbc","amazon"},1]
print(example7)


print("Dr Matt Phone 0139:",directory[2][0][1])