import pandas as pd
import sys

try:
    df = pd.read_csv(str(sys.argv[1]))
except:
    df = pd.read_csv(input("Blast/NCRF GFF extraction output: "))

anotacoes = df.annotation.str[0:-1].str.split(';product=', expand = True) #creates a var. to store the value after the split use - splits the column "annotation" with the ";product=" substring into two columns

df["annotation"] = anotacoes[1] #replaces the old "annotation" column with the second "anotacoes" var. column, the part after the ";product=" substring.

try:
    df.to_csv(sys.argv[2], index=False) #save the final dataframe to an csv.
except:
    df.to_csv(input("Output File: "), index=False)
