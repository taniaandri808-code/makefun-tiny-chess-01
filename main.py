import urllib.request,json,os,time
U=os.environ.get("MAKEFUN_ENV_URL","http://localhost:8198")
def req(e,d={}):
 try:return json.loads(urllib.request.urlopen(urllib.request.Request(f"{U}{e}",data=json.dumps(d).encode(),headers={"Content-Type":"application/json"})).read().decode())
 except Exception:
  if d or e!="/game":raise
  time.sleep(2);return req(e,d)
P,N,B,R,Q,K=1,2,3,4,5,6
V=[0,100,320,330,500,900,20000,0,0,100,320,330,500,900,20000]
ON=(-33,-31,-18,-14,14,18,31,33)
OB=(-17,-15,15,17)
OR=(-16,-1,1,16)
OQ=OB+OR
def s2u(s):return chr(97+(s&7))+str((s>>4)+1)
class Engine:
 def __init__(self):self.n=0
 def parse(self,fen):
  b=[0]*128
  p=fen.split()
  for i,row in enumerate(p[0].split('/')):
   c=0
   for ch in row:
    if ch.isdigit():c+=int(ch)
    else:b[(7-i)*16+c]={'P':1,'N':2,'B':3,'R':4,'Q':5,'K':6,'p':9,'n':10,'b':11,'r':12,'q':13,'k':14}[ch];c+=1
  self.t=0 if p[1]=='w' else 8
  self.b=b
 def moves(self):
  m=[]
  b,us=self.b,self.t
  them=8-us
  for sq in range(128):
   if sq&0x88:continue
   p=b[sq]
   if not p or(p&8)!=us:continue
   pt=p&7
   if pt==P:
    f=16 if us==0 else -16
    r=sq>>4
    ns=sq+f
    if(ns&0x88)==0 and not b[ns]:
     if r==(6 if us==0 else 1):
      for pr in(Q,R,B,N):m.append((sq,ns,pr))
     else:m.append((sq,ns,0))
     if r==(1 if us==0 else 6) and not b[sq+f+f]:m.append((sq,sq+f+f,0))
    for df in(-1,1):
     ns=sq+f+df
     if(ns&0x88)==0 and b[ns] and(b[ns]&8)==them:
      if r==(6 if us==0 else 1):
       for pr in(Q,R,B,N):m.append((sq,ns,pr))
      else:m.append((sq,ns,0))
   elif pt==N:
    for o in ON:
     ns=sq+o
     if(ns&0x88)==0 and(not b[ns] or(b[ns]&8)==them):m.append((sq,ns,0))
   elif pt in(B,R,Q):
    for o in(OQ if pt==Q else(OB if pt==B else OR)):
     ns=sq+o
     while(ns&0x88)==0:
      t=b[ns]
      if not t:m.append((sq,ns,0))
      else:
       if(t&8)==them:m.append((sq,ns,0))
       break
      ns+=o
   elif pt==K:
    for o in OQ:
     ns=sq+o
     if(ns&0x88)==0 and(not b[ns] or(b[ns]&8)==them):m.append((sq,ns,0))
  return m
 def make(self,m):
  sq,ns,pr=m
  b=self.b
  p,cap=b[sq],b[ns]
  b[ns]=(p&~7)|pr if pr and(p&7)==P and(ns>>4 in(0,7)) else p
  b[sq]=0
  self.t=8-self.t
  return(sq,ns,p,cap,pr)
 def unmake(self,m,u):
  sq,ns,p,cap,pr=u
  self.b[sq]=p
  self.b[ns]=cap
  self.t=8-self.t
 def ev(self):
  s=sum(V[p]*(-1 if p&8 else 1) for sq,p in enumerate(self.b) if not(sq&0x88) and p)
  return s if self.t==0 else -s
 def q(self,a,beta,d):
  self.n+=1
  sp=self.ev()
  if sp>=beta or d<=0:return beta if sp>=beta else a
  if a<sp:a=sp
  for m in self.moves():
   if not self.b[m[1]]:continue
   u=self.make(m)
   sc=-self.q(-beta,-a,d-1)
   self.unmake(m,u)
   if sc>=beta:return beta
   if sc>a:a=sc
  return a
 def neg(self,d,a,beta):
  self.n+=1
  if d<=0 or self.n>160000:return self.q(a,beta,9)
  moves=self.moves()
  if not moves:return -30000+d*100
  moves.sort(key=lambda m:self.b[m[1]]&7,reverse=True)
  for m in moves:
   u=self.make(m)
   sc=-self.neg(d-1,-beta,-a)
   self.unmake(m,u)
   if sc>=beta:return beta
   if sc>a:a=sc
  return a
 def best(self):
  self.n=0
  moves=self.moves()
  if not moves:return None
  bm,bv=moves[0],-9e9
  for d in range(1,9):
   if self.n>120000:break
   for m in moves:
    u=self.make(m)
    v=-self.neg(d-1,-1e9,1e9)
    self.unmake(m,u)
    if v>bv:bv,bm=v,m
   if self.n>30000:break
  return s2u(bm[0])+s2u(bm[1])+({Q:'q',R:'r',B:'b',N:'n'}[bm[2]] if bm[2] else '')
def main():
 res=req("/game")
 while True:
  st=res.get("status")
  if st=="done":break
  if st=="your_move":
   e=Engine()
   e.parse(res["fen"])
   m=e.best()
   L=res.get("legal_moves") or []
   if m not in L:m=L[0] if L else m
   res=req("/move",{"game":res["game"],"move":m})
   if res.get("outcome"):print(res["game"],res["outcome"],res.get("reason"))
  else:res=req("/game")
 print(res)
if __name__=="__main__":main()
