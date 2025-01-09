a = {} # Empty dictionary

marks = {
    "Anshu" : 90,
    "Saransh" : 100,
    "Salina" : 50,
    90: "Raj"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Salina": 60, "Dipesh": 60})

# print(marks)

print(marks.get("Anshu1"))   # Prints none
print(marks["Anshu1"])      # Returns an error
