import sys 
import re

dict = {
    "1":"https://es.wikipedia.org/wiki/mazda",
    "2":"https://es.wikipedia.org/wiki/nissan",
    "3":"https://es.wikipedia.org/wiki/toyota",
    "4":"https://es.wikipedia.org/wiki/mitsubishi",
    "5":"https://es.wikipedia.org/wiki/suzuki",
    "6":"https://es.wikipedia.org/wiki/bentley",
    "7":"https://es.wikipedia.org/wiki/ferrari",
    "8":"https://es.wikipedia.org/wiki/lamborghini",
    "9":"https://es.wikipedia.org/wiki/lotus",
    "10":"https://es.wikipedia.org/wiki/bugatti",
}
for line in sys.stdin:
    if(line.split()[0] == sys.argv[1]):
        # obtener ls
        aux=re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+',line)
        max = 0
        res = 0
        for tuple in aux[1:]:
            if eval(tuple)[1] > max:
                max = eval(tuple)[1]
                res = eval(tuple)[0]
try:    
    print(res)
    print(dict[str(res)])
    print(sys.argv[1])
except:
    print("palabra no encontrada!")