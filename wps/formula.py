def find_gain(cp,sp):
	ans=[]
	
	ans.append("The cost price is $"+str(cp))
	ans.append("The selling price is $"+str(sp))
	ans.append("The formula to calculate gain is $"+ " (selling price - cost price) ")
	ans.append("The gain is "+ str(abs(sp-cp)))
	return ans,abs(sp-cp)
def find_loss(cp,sp):
	ans=[]
	ans.append("The cost price is $"+str(cp))
	ans.append("The selling price is $"+str(sp))
	ans.append("The formula to calculate loss is $"+ " (cost price - selling price) ")
	ans.append("The loss is "+ str(abs(cp-sp)))
	return ans,abs(cp-sp)
def find_sp(cp,x,sr):
	ans=[]
	if sr=="gain":
		sp=cp+x
		ans.append("The cost price is $"+str(cp))
		ans.append("The "+str(sr)+" is $" + str(x))
		ans.append("The selling price is $"+str(cp+x))
		return ans
	else:
		sp=abs(cp-x)
		ans.append("The cost price is $"+str(cp))
		ans.append("The "+str(sr)+" "+" is $" + str(x))
		ans.append("The selling price is $"+str(abs(cp-x)))
		return ans
		
def find_cp(cp,x,sr):
	ans=[]
	if sr=="loss":
	
		ans.append("The selling price is $"+str(cp))
		ans.append("The "+str(sr)+" "+" is $" + str(x))
		ans.append("The cost price is $"+str(abs(cp+x)))
		return ans
	else:
		ans.append("The selling price is $"+str(cp))
		ans.append("The "+str(sr)+" is $" + str(x))
		ans.append("The cost price is $"+str(abs(cp-x)))
		return ans
def find_loss_percent(loss,cp):
	ans=[]
	ans.append("The cost price is $"+str(cp))
	ans.append("The loss is $"+ str(loss))
	ans.append("The formula to calculate loss percent is "+ " (cost price - selling price)/ cost price *100 ")
	v=(loss/cp)*100
	ans.append("The loss percent is "+str(v))
	return ans
def find_gain_percent(gain,cp):
	ans=[]
	ans.append("The cost price is $"+str(cp))
	ans.append("The gain is $"+ str(gain))
	ans.append("The formula to calculate gain percent is "+ " (selling price - cost price)/ cost price *100 ")
	v=(gain/cp)*100
	ans.append("The gain percent is "+str(v))
	return ans

