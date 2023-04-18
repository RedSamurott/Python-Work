row_input=int(input("How many rows? "))
column_input=int(input("How many columns? "))
df=(row_input-1)*(column_input-1)
matrix_a=[]
matrix_b=[]
matrix_c=[]
matrix_d=[]
matrix_e=[]
row=[]
sum_row=[]
sum_column=[]

for x in range(1,row_input+1):
    row=[]
    for y in range(1,column_input+1):
        cell=float(input("What is the data that goes in cell row "+str(x)+" column "+str(y)+"? "))
        row.append(cell)
    matrix_a.append(row)

for x in range(0,row_input):
    sum_row.append(sum(matrix_a[x]))
for x in range(0,column_input):
    placehold=[]
    sum_column_placehold=[]
    for y in range(0,row_input):
        placehold=matrix_a[y]
        sum_column_placehold.append(placehold[x])
    sum_column.append(sum(sum_column_placehold))
        
for x in range(0,row_input):
    row=[]
    for y in range(0,column_input):
        cell=(sum_row[x]*sum_column[y])/sum(sum_row)
        row.append(cell)
    matrix_b.append(row)

for x in range(0,row_input):
    row=[]
    for y in range(0,column_input):
        cell=((float(matrix_a[x][y])-float(matrix_b[x][y])) ** 2.0)/float(matrix_b[x][y])
        row.append(cell)
    matrix_c.append(row)



for x in range(0,row_input):
    row=[]
    for y in range(0,column_input):
        cell=round(matrix_b[x][y],4)
        row.append(cell)
    matrix_d.append(row)
for x in range(0,row_input):
    row=[]
    for y in range(0,column_input):
        cell=round(matrix_c[x][y],4)
        row.append(cell)
    matrix_e.append(row)

row=[]
for x in range(0,len(matrix_c)):
    row.append(sum(matrix_c[x]))

print("Expected values and chi-squared values are...")
for x in range(0,row_input):
    print(matrix_d[x])
for x in range(0,row_input):
    print(matrix_e[x])
z=sum(row)
print("chi-squared = "+str(round(z,4)))