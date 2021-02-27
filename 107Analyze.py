import pandas as pd
import statistics as st

data = pd.read_csv('107Waive.csv')
print("[READ COMPLETE]")

law_29 = 0
law_31 = 0
law_33 = 0
law_35 = 0
law_39 = 0
law_51 = 0
law_51a = 0
law_51b = 0
law_51c = 0
law_51d = 0

# ------------- People vs. Companies -------------
people = 0
comp = 0
for i in data['name']:
	x = i.split()
	if(len(x) == 2):
		people += 1
	else:
		comp += 1

# ------------- Exemption Distrubution -------------
for i in data['law']:
	if(i.find('107.29') != -1):
		law_29 +=1
	if(i.find('107.31') != -1):
		law_31 +=1
	if(i.find('107.33') != -1):
		law_33 +=1
	if(i.find('107.35') != -1):
		law_35 +=1
	if(i.find('107.39') != -1):
		law_39 +=1
	if(i.find('107.51') != -1):
		law_51 +=1
	if(i.find('107.51(a)') != -1):
		law_51a +=1
	if(i.find('107.51b') != -1):
		law_51b +=1
	if(i.find('107.51(b)') != -1):
		law_51b +=1
	if(i.find('107.51(c)') != -1):
		law_51c +=1 
	if(i.find('107.51(d)') != -1):
		law_51d +=1

total_ct = (law_29 + law_31 + law_33 + law_35 + law_39 + law_51)/100

# ------------- Data Outpu -------------
print(f'# of 107.29: {law_29}')
print(f'# of 107.31: {law_31}')
print(f'# of 107.33: {law_33}')
print(f'# of 107.35: {law_35}')
print(f'# of 107.39: {law_39}')
print(f'# of 107.51: {law_51}')
print(f'# of 107.51a: {law_51a}')
print(f'# of 107.51b: {law_51b}')
print(f'# of 107.51c: {law_51c}')
print(f'# of 107.51d: {law_51d} \n')

print(f'% of 107.29: {law_29/total_ct}')
print(f'% of 107.31: {law_31/total_ct}')
print(f'% of 107.33: {law_33/total_ct}')
print(f'% of 107.35: {law_35/total_ct}')
print(f'% of 107.39: {law_39/total_ct}')
print(f'% of 107.51: {law_51/total_ct} \n')

print(f"# of people: {people}, {round(people*100/(people+comp), 1)}%")
print(f"# of companies: {comp}, {round(comp*100/(people+comp), 1)}% \n")

print("Median: ", st.median(data['law']))
print("Mode: ", st.mode(data['law']), '\n')
