import pandas as pd
import Levenshtein


try:
    df2 = pd.read_csv(str(sys.argv[1]))
except:
    df2 = pd.read_csv(input("Input first gffextract.csv after treat1: "))

try:
    df3 = pd.read_csv(str(sys.argv[2]))
except:
    df3 = pd.read_csv(input("Input second gffextract.csv after treat1: "))


dfan2 = df2['annotation'].tolist()
dfan3 = df3['annotation'].tolist()


dffinala = pd.DataFrame()
dffinala2 = pd.DataFrame()
dffinala3 = pd.DataFrame()
dffinalb = pd.DataFrame()
dffinalb2 = pd.DataFrame()
dffinalb3 = pd.DataFrame()

print("The run is starting")

for i in range(len(dfan2)):
    for j in range(len(dfan3)):
        var1 = str(dfan2[i])
        var2 = str(dfan3[j])
        if 13 > Levenshtein.distance(var1, var2):
            print(dfan2[i])
            print(dfan3[j])
            dffinala = dfan2[i]
            dffinalb = dfan3[j]
            dffinala2 = pd.Series(dffinala) #transforma lista dffinal em series para poder concatenar com o append na proxima linha.
            dffinalb2 = pd.Series(dffinalb)
            dffinala3 = dffinala3.append(dffinala2, ignore_index=True) #tem que ter esse ignore_index pra dar o append.
            dffinalb3 = dffinalb3.append(dffinalb2, ignore_index=True)


dffinala3 = dffinala3.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
dffinalb3 = dffinalb3.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)

dffinala3.to_csv("outfinala.csv", index=False)
dffinalb3.to_csv("outfinalb.csv", index=False)

print("The run is ended")