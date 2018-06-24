
ans=[]
	
def moreMoney(dep,doc,pattern,unknown):
	import os 
	os.getcwd()
	import numpy as np
	import pandas as pd
	import spacy
	from . import formula
	nlp = spacy.load('en_core_web_sm')
	from difflib import SequenceMatcher
	import re
	path_to_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0.jar'
	path_to_models_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0-models.jar'

	jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-postagger-3.8.0.jar'
	model = '/usr/local/lib/python2.7/dist-packages/nltk/tag/models/english-left3words-distsim.tagger'
	import nltk
	import pprint
	pp = pprint.PrettyPrinter(indent=4)
	from nltk import word_tokenize
	from nltk.corpus import stopwords
	from nltk.parse.corenlp import CoreNLPParser
	from nltk.tag import StanfordNERTagger
	from nltk.parse.stanford import StanfordParser
	from nltk.parse.stanford import StanfordDependencyParser
	from nltk.stem import PorterStemmer
	from nltk.tokenize import sent_tokenize
	from nltk.tag import StanfordPOSTagger
	
	dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
        #print "moreMoney"
	q_dep=[]
	pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
	ratios=[]
	answer=""
	for ent in doc.ents:
		ratios=[]
		if(ent.label_=="MONEY" or ent.label_=="CARDINAL"):
	
			q_dep=[]
			for triple in dep.triples():
				pq=clean(ent.text)
				com=clean(triple[0][0])
				com1=clean(triple[2][0])
				if(com==pq or com1==pq):
					money=pq
					q_dep.append(triple)
			q_dep = str(q_dep)
			#print "###################"
			#print q_dep
			for i in range(len(pattern)):
				m=SequenceMatcher(None,pattern["pattern"][i],q_dep)
				q=m.ratio()
				ratios.append(q)
			mx=max(ratios)
			#print len(ratios)
			ino=ratios.index(mx)
			#print ino
			answer=pattern["tag"][ino]
	#print(answer,unknown)

def find(question,name,doc,inq):
	try:
		import numpy as np
		import pandas as pd
		import spacy
	
		from . import formula
		nlp = spacy.load('en_core_web_sm')
		from difflib import SequenceMatcher
		import re
		path_to_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0.jar'
		path_to_models_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0-models.jar'

		jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-postagger-3.8.0.jar'
		model = '/usr/local/lib/python2.7/dist-packages/nltk/tag/models/english-left3words-distsim.tagger'
		import nltk
		import pprint
		pp = pprint.PrettyPrinter(indent=4)
		from nltk import word_tokenize
		from nltk.corpus import stopwords
		from nltk.parse.corenlp import CoreNLPParser
		from nltk.tag import StanfordNERTagger
		from nltk.parse.stanford import StanfordParser
		from nltk.parse.stanford import StanfordDependencyParser
		from nltk.stem import PorterStemmer
		from nltk.tokenize import sent_tokenize
		from nltk.tag import StanfordPOSTagger
		sen_list=sent_tokenize(name)
		pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
		no_sen=nltk.FreqDist(sent_tokenize(name)).N()
		dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
		final=[]
		j=0
		#print "infind {{{{{{{{{{{{{{{{"
		#print ("1")
		mmmo=[]
		for ent in doc.ents:
		    #print type(ent) 				
		    #print (ent.label_, ent.text)
		    if(ent.label_ ==u'MONEY'):
		            mmmo.append(ent.text)

		k=str(mmmo[0])
		u=str(mmmo[1])
		#print k,u
		#print ("1")
		k=k.lstrip('$')
	
		u=u.lstrip('$')
	
		k=float(k)
		u=float(u)
	
		j=0
		fin=0
		#print ("1")
		#print (question)
		for i in question:
			print (i)
			if(fin==0):
				j=j+1
				if(i[1]=="WDT" or i[1]=="WRB" or i[0]=="find" or i[1]=="WP" or i[0]=="Find" or i[0]=="FIND" or i[0]=="Calculate" or i[0]=="calculate" ):
					fin=1
					print (i)
					while(i[1]!="MD" or i[0]=="." or i[0]=="?"):
						if (i[0]=="." or i[0]=="?"):
							break
						#print(i[0])
						final.append(i[0])
						#print ("1")
						i=question[j]
						#sprint ("1")
						j=j+1

	
		p=0
		#print(final)
		sp=0
		cp=0
		gain=0
		gpercent=0
		lpercent=0
		loss=0
		unk=0
		for i in final:
			if(i=="sp" or i=="selling"):
				sp=1
				unk+=1
			if(i=="cp" or i=="cost"):
				cp=1
				unk+=1
			if (i=="gain" or i=="profit"):
				gain=1
				unk+=1
				if ("percent" in final)  or ("%" in final) or ("percentage" in final):
					gpercent=1
					if final.count("gain") >1 or final.count("profit") >1 or (final.count("gain")==1 and final.count("profit")==1):
						unk+=1
			if i=="loss" :
				loss=1
				unk+=1
				if ("percent" in final)  or ("%" in final) or ("percentage" in final):
					lpercent=1
					if final.count("loss") >1:
						unk+=1
		#print "unknown is "+str(unk)
		#print gpercent,lpercent			
		'''top = Tk()
		top.configure(background="#EEEEEE")
		top.title("Word Problem Solver")
		L1 = Label(top, text="ANSWER",bg="#EEEEEE",fg="#2cc866",font=("Helvetica", 16))
		L1.pack( side = TOP,pady=30)
		top.minsize(width=750, height=290)
		L1 = Label(top,fg="black",font=("Helvetica", 16))
		L1.pack( side = TOP,padx=20,pady=30)
		#E1 = Entry(top, bd =5,bg="grey",font=("Helvetica", 14),width=100)
		#E1.pack(ipady=50)
		'''
		#print ("5s")	
		if unk == 1:
			if sp==1 and (inq.count("gain")==1 or inq.count("profit")==1):
				answer=formula.find_sp(k,u,"gain")
				ans.append( answer)
				anss = ""
				for i in answer:
					anss+=i
					anss+="\n"
			elif cp==1 and (inq.count("gain")==1 or inq.count("profit")==1):
				answer=formula.find_cp(k,u,"gain")
				ans.append( answer)
				anss = ""
				for i in answer:
					anss+=i
					anss+="\n"
			elif sp==1 and (inq.count("loss")==1):
				answer=formula.find_sp(k,u,"loss")
				ans.append( answer)
				anss = ""
				for i in answer:
					anss+=i
					anss+="\n"
			elif cp==1 and (inq.count("loss")==1):
				answer=formula.find_cp(k,u,"loss")
				ans.append( answer)
				anss = ""
				for i in answer:
					anss+=i
					anss+="\n"
			elif gain==1 and (gpercent==0 and lpercent==0):
				answer,ur=formula.find_gain(k,u)
				ans.append( answer)
				anss = ""
				for i in answer:
					anss+=i
					anss+="\n"
			
			elif loss==1 and (gpercent==0 and lpercent==0):
				answer,ur=formula.find_loss(k,u)
				ans.append( answer)
				anss = ""
				for i in answer:
					anss+=i
					anss+="\n"
			elif gpercent==1:
				kr,u=formula.find_gain(k,u)
				answer=formula.find_gain_percent(min(k,u),max(k,u))
				ans.append( answer)
				anss = ""
				for i in kr:
					anss+=i
					anss+="\n"
					
				for i in answer:
					anss+=i
					anss+="\n"
			elif lpercent==1:
				kr,u=formula.find_loss(k,u)
				answer=formula.find_loss_percent(min(k,u),max(k,u))
				ans.append( answer)
				anss = ""
				for i in kr:
					anss+=i
					anss+="\n"
				for i in answer:
					anss+=i
					anss+="\n"
				#anss+=str(a)
		#L1.configure(text="" + anss)
		#top.mainloop()			
		#elif unk==2:
		return  (anss)
			#print "HEllo"
	except:	
		return 0		
	
	
def read(name):
	import numpy as np
	import pandas as pd
	import os
	#print (name)
	red = pd.read_csv('/home/piut/django-apps/wps/wps/patterns.csv',header=0)
	#print (name)
	return red

def clean(text):
	import numpy as np
	import pandas as pd
	import spacy
	from . import formula
	nlp = spacy.load('en_core_web_sm')
	from difflib import SequenceMatcher
	import re
	path_to_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0.jar'
	path_to_models_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0-models.jar'

	jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-postagger-3.8.0.jar'
	model = '/usr/local/lib/python2.7/dist-packages/nltk/tag/models/english-left3words-distsim.tagger'
	import nltk
	import os 
	os.getcwd()
	import pprint
	pp = pprint.PrettyPrinter(indent=4)
	from nltk import word_tokenize
	from nltk.corpus import stopwords
	from nltk.parse.corenlp import CoreNLPParser
	from nltk.tag import StanfordNERTagger
	from nltk.parse.stanford import StanfordParser
	from nltk.parse.stanford import StanfordDependencyParser
	from nltk.stem import PorterStemmer
	from nltk.tokenize import sent_tokenize
	from nltk.tag import StanfordPOSTagger
	pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
	
	dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
	ps=PorterStemmer()
	cleaned_text = text.replace(',', '')
	cleaned_text=re.sub('(\.\s)'," ",cleaned_text)
	cleaned_text=re.sub('(\.[a-zA-Z])'," ",cleaned_text)
	words=word_tokenize(cleaned_text)
	return cleaned_text



def impp(input_question):
	try:
		import numpy as np
		import os 
		os.getcwd()
		import pandas as pd
		import spacy
		from . import formula
		nlp = spacy.load('en_core_web_sm')
		from difflib import SequenceMatcher
		import re
		import nltk
		import pprint
		pp = pprint.PrettyPrinter(indent=4)
		from nltk import word_tokenize
		from nltk.corpus import stopwords
		path_to_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0.jar'
		path_to_models_jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-parser-3.8.0-models.jar'

		jar = '/usr/local/lib/python2.7/dist-packages/nltk/tag/stanford-postagger-3.8.0.jar'
		model = '/usr/local/lib/python2.7/dist-packages/nltk/tag/models/english-left3words-distsim.tagger'
		from nltk.parse.corenlp import CoreNLPParser
		from nltk.tag import StanfordNERTagger
		from nltk.parse.stanford import StanfordParser
		from nltk.parse.stanford import StanfordDependencyParser
		from nltk.stem import PorterStemmer
		from nltk.tokenize import sent_tokenize
		from nltk.tag import StanfordPOSTagger
		pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
	
		dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
		#print ("1")
		#print (os.path.exists('/home/piut/django-apps/wps/wps/patterns.csv'))
		#print ("2")	
		pattern=read('patterns.csv')
		#print ("1")	
		#print pattern
		question=input_question
		tagged_question=pos_tagger.tag(nltk.word_tokenize(question))
		doc = nlp(question)
		#print "###################################################################"
		#print doc
		#print ("2")
		result = dependency_parser.raw_parse(question)
		#pp.pprint(tagged_question)
		#print ("3")
		#return str(moreMoney(dependency,doc,pattern,unknown))
		unknown=find(tagged_question,question,doc,input_question)
		if unknown==0:
			return 0
		return unknown
  # 		fe
	except:
		return 0

def submit(question):

	problem_statement=question
	problem_statement=problem_statement.lower()
	#print ("Lower zhala")
	problem_statement=clean(problem_statement)
	#print (problem_statement)
	#print ("Clean zhala")	
	final_ans=impp(problem_statement)
	return final_ans
	
    
