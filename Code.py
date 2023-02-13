import tabula

pdf_path = "C:/Users/User/OneDrive - ABES/Desktop/Assignment2_walnut/keppel-corporation-limited-annual-report-2018.pdf"

# Extract table from PDF file, page number = 69
dfs = tabula.read_pdf(pdf_path, pages='69')

print(len(dfs))

# Write dataframe to CSV file
dfs[0].to_csv("first_table.csv")

import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("first_table.csv")

# Write the DataFrame to an Excel file
df.to_excel("output.xlsx", index=False)

#Refining the Table extracted

df2=pd.read_excel("C:/Users/User/OneDrive - ABES/Desktop/Research_Intership/Assignment2_walnut/output.xlsx")

df2.to_csv("data1.csv")
df2=pd.read_csv("data1.csv",header=None)
df3=df2.iloc[1:]
df3.to_excel("output2.xlsx", index=False)
