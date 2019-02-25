import pandas as pd
cars = pd.read_csv ("C:/Users/mike/Documents/PyProject/Data/cars_csv.txt",index_col=0)
# for lab, row in cars.iterrows() :
    # print(lab + ": " + str(row['cars_per_cap']))

# x = "abc".upper()
# print(x)
# x = str.upper("abc")
# print(x)

# for lab, row in cars.iterrows() :
#     cars.loc[lab,"COUNTRY"] = row["country"].upper()

cars["COUNTRY"] = cars["country"].apply(str.upper) # preferred method
print(cars)
