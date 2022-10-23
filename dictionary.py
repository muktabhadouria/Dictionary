"""d1 = {}
d2 = {"mukta" : "roti" , "riya" : "chawal" , "gowtham" : "dosa", "shubham":{"b":"roti","l":"biryani","d":"chicken"}}
print(d2["shubham"])
print(d2.keys())
print(d2.items())
print(d2.values())
print(d2.get("shubham")) #or print(d2["shubham"])"""


dict={"atrocity":"an act of shocking cruelty","fanatical":"marked by excessive enthusiasm for a cause or idea","pensive":"deeply or seriously thoughtful",
    "respite":"a pause from doing something","discordant":"not in agreement or harmony","eloquent":"expressing yourself readily, clearly, effectively",
    "encompass":"include in scope","imperceptible":"impossible or difficult to sense","insuperable":"incapable of being surpassed or excelled",
    "lethargy":"inactivity; showing an unusual lack of energy","lucid":"transparently clear; easily understandable","pertinacity":"persistent determination",
    "potent":"having or wielding force or authority","relapse":"deteriorate in health","resolution":"a decision to do something or to behave in a certain manner"}
search=input("enter your word")
print(dict.get(search))
#print(dict.get("atrocity"))
