from pyscript import document,display

element1 = {
    "H": ("HYDROGEN", 1, 1008),
    "He": ("HELIUM", 2, 4.002602),
    "Li": ("LITHIUM", 3, 6.941),
    "B": ("BORON", 5, 10.81),
    "C": ("CARBON", 6, 12.011),
    "N": ("NITROGEN", 7, 14.007),
    "O": ("OXYGEN", 8, 15.999),
    "Fl": ("FLUORINE", 9, 18.998),
    "Ne": ("NEON", 10, 20.180),
    "Rn": ("RADON", 86, 222),
    "P": ("PHOSPHORUS", 15, 30.974),
    "Se": ("SELENIUM", 34, 78.971),
    "Br": ("BROMINE", 35, 79.904),
    "I": ("IODINE", 53, 126.90),
    "Cl": ("CHLORINE", 17, 35.45),
    "Ar": ("ARGON", 18, 39.948),
    "Kr": ("KRYPTON", 36, 83.798),
    "Xe": ("XENON", 54, 131.29),
}



def Search_element(e):
    # get the input from html
    element = document.getElementById("element1").value
    # check if the input is in the dictionary
    result = element1.get(element,  ("Element not found", "-", "-")    )
    #display result in html
    document.getElementById("Symbol").innerHTML = element
    document.getElementById("name").innerHTML = result[0]
    document.getElementById("num").innerHTML = result[1]
    document.getElementById("mass").innerHTML = result[2]
