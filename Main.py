"""
AUTHOR - HARI OM
Python code to convert standard SOP form
to standard POS form.
"""
#function to calculate the alphabets.
def count_no_alphabets(SOP):
	i = 0
	no_var = 0
	while (SOP[i]!='+'):	
		if (SOP[i].isalpha()):	
			no_var+= 1
		i+= 1
	return no_var

# function to calculate the min terms in integers
def Cal_Min_terms(Min_terms, SOP):
	a =""
	i = 0
	while (i<len(SOP)):
		if (SOP[i]=='+'):			
			b = int(a, 2)			
			Min_terms.append(b)		
			a =""						
			i+= 1
		else:
			if(i + 1 != len(SOP) and SOP[i + 1]=="'"):
				a+='0'						
				i+= 2							
			else:
				a+='1'						
				i+= 1
	Min_terms.append(int(a, 2))			

# calculate POS form of SOP
def Cal_Max_terms(Min_terms, no_var, start_alphabet):
	Max_terms =[]					
	max = 2**no_var				
	for i in range(0, max):
		if (Min_terms.count(i)== 0):
			b = bin(i)[2:]	
			while(len(b)!= no_var):
				b ='0'+b
			Max_terms.append(b)	
	POS =""					
	for i in Max_terms:		
		POS = POS+"("		
		value = start_alphabet	
		for j in i:			
			if (j =='1'):				
				POS = POS + value+"'+"	
			else:					
				POS = POS + value+"+"	
			value = chr(ord(value)+1)	
		POS = POS[:-1]				
		POS = POS+")."					
	POS = POS[:-1]						
	return POS

# main function
def main():
	# input1
	SOP_expr ="A'B'C+A'B'C + A'BC' + AB'C'+ABC'"
	Min_terms =[]
	no_var = count_no_alphabets(SOP_expr)
	Cal_Min_terms(Min_terms, SOP_expr)
	POS_expr = Cal_Max_terms(Min_terms, no_var, SOP_expr[0])
	print ("Standard POS form of", SOP_expr, "~~~>", POS_expr)
# driver code	
if __name__=="__main__":
	main()
