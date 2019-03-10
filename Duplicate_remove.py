a = ['one','two','two','three']
b = set(a)
c = list(b)
print(c)

globvar = 0
def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1
def print_globvar():
    print globvar     # No need for global declaration to read value of globvar
set_globvar_to_one()
print_globvar()
