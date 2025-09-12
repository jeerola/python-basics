arvonimi = "Raivokkaan Asiallinen, Utelias Näkemyksellinen Onnistuja"
print(f'{arvonimi[0]}.{arvonimi[11]}.{arvonimi[23]}.{arvonimi[31]}.{arvonimi[47]}.') # Prints R.A.U.N.O.

rank = arvonimi.split() # splits arvonimi into independent words and puts them into a list
result = ""
for word in rank:
    result += (f'{word[0]}.')
print(result) # prints R.A.U.N.O