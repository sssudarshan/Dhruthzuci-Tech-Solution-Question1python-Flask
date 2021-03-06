from flask import Flask,request,jsonify
import re
app=Flask(__name__)

@app.route('/find_symbols_in_names',methods=['POST'])
def find_symbols_in_names():
    res = request.json
    print(res)
    dic={}
    lst=[]
    chemicals=res.get("chemicals")
    symbols=res.get("symbols")
    for i in chemicals:
        try:
           for j in symbols:
               try:
                 pattern=j
                 indextup=(re.search(pattern,i).span())
                 if(len(indextup)!=0):
                   lower=indextup[0]
                   upper=indextup[1]
                   result=i[:lower]+'['+pattern+']'+i[upper:]
                   lst.append(result)
                   symbols.remove(i)
               except Exception as e:
                    pass
        except Exception as e:
            pass
    dic["result"]=lst
    print(dic)
    return jsonify(dic)



