list_checked = []
duplicates = []
new_list = []
dups = []

with open("Extracted.txt") as email_list:
	for email in email_list:
		email = email.strip("\n")
		list_checked.append(email) # everyone
		
r = 1
new_list = sorted(list_checked)
for i in new_list:
	if '@' in i:
		if i not in dups:
			dups.append(i)
			with open("Dup-Removed.txt", "a") as duprem:
				duprem.write(i)	
				duprem.write("\n")
			r += 1	

print("Total E-mail After Duplicates Removal: ", r)







