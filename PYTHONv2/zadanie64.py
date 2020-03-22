lista=[1,2,3,4,5]
tup=(1,2,3,4,5) #tuple to lista której nie można modyfikować
dz={"imie":"Anna","nazwisko":"kowalska"} #dzienniki mają nazwane indeksy np. "imie"
                                        # i można do nich przypisać wszystko + wywołujemy tylko po NAZWIE INDEKSU

n="1 2 3 4 5 6"
lst=list(n.split()) #list() robi liste np. ze stringów albo z tuple

lst=[1,2,3]
print(sum(lst)) #sum() sumuje listy,tuple itp
print(set(lst)) #set() zmiana na list z tumple, na dzienniki itp
