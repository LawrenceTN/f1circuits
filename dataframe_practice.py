# Adding into github

# 0. go to directory
# 1. git init (initialize repository)
# 2. git add . (add all current files in pwd)
# 3. git status (to check what will be added)
# 4. git commit -m "message here" (commit what's in the status and provide msg)
# 5. git remote add origin "https://github.com/LawrenceTN/f1circuits.git" (copy the git repository url and then all added files will be pushed)
# 6. git push -u origin master (this will prompt user/pwd)                                

import pandas as pd 

df = pd.read_csv('circuits.csv')

# Select the top 5 head df entries
print(df.head(5))

print('\n')

# Select rows and columns by with loc: Better if you only know the name of the column
print(df.loc[3, 'name']) # Gives the 'Name' of row index 3
print(df.loc[3:5, 'name']) # Gives name from index 3 to index 5 (as well are their row index). Loc is inclusive  

print('\n')

# Select rows and columbs with iloc: Better/Faster if you know the index numbers. 
print(df.loc[0, 'name']) # Select row index 0, and you can either call a column by name or index again
print(df.iloc[0, 2]) # Selecting row index 0, and column index 2 is the name again (FASTER, HOW IT SHOULD BE USED)
print(df.iloc[3:5, 2]) # Iloc is exclusive when splicing

print('\n')

# Querying: Selecting df based off boolean expressions
print(df.query('circuitId > 50'))

print('\n')

# Filtering: based off regular expressions
print(df[df['country'].isin(['United States', 'France', 'USA'])]) # .isin = IN (SQL). Difficult part is df[df['asdf']

print('\n')

# Data sorting
print(df.groupby(df['circuitRef'].apply(len)).groups) # Sorting the data by length of the circuitRef

# Data Cleaning
print(df.notna()) # Will check for null values in the entire data frame
df.dropna(subset=['name']) # This will delete any null values in the 'name' column
