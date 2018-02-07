import Queue
from Queue import *

#import sys

l, m, r = [], [], []
a, b, c, d = 0, 0, 0, 0
q = Queue()
reg = ""
qw = ""
t = 0

def printShortestPath(n, i_start, j_start, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    a, b, c, d = i_start, j_start, i_end, j_end
    
    r.append(a)
    r.append(b)
    y = []
    y = r
   
    printx ("", y, c, d, 0, "")
    
t = 0
def printy (reg) :
	print "++++++++++++++++++++++++++"
def printx (qw, y, c ,d, k, reg):
    
    q = Queue()
    print y
    q.put(y)
    y = []
   
    while not q.empty() :
	    x = q.get()
	    if c == x[0] and d == x[1] :
		    if k < len(qw) :
			    reg = qw
			    
			    printy (reg)
			    x[0], x[1] = 0, 0
			    break
			    
		    qw = ""
	    else :
		    if x[0]-2 >= 0 :
			    if x[1] + 1 < n :
				    y.append(x[0]-2)
				    y.append(x[1]+1)
				    qw += "LR"
				    printx (qw, y, c, d,k, reg)
			    if x[1] - 1 >= 0 :
				    y.append(x[0]-2)
				    y.append(x[1]-1)
				    #q.put(y)
				    qw += "LL"
				    printx (qw, y, c, d, k, reg)
				    y = []
		    if x[0]+2 < n :
			    if x[1] + 1 < n :
				    y.append(x[0]+2)
				    y.append(x[1]+1)
				    #q.put(y)
				    qw += "UR"
				    printx (qw, y, c, d, k, reg)
				    y = []
			    if x[1] - 1 >= 0 :
				    y.append(x[0]+2)
				    y.append(x[1]-1)
				    #q.put(y)
				    qw += "UL"
				    printx (qw, y, c, d, k, reg)
				    y = []
		    if x[1] + 2 < n :
			    y.append(x[0])
		            y.append(x[1]+2)
			    #q.put(y)
			    qw += "R"
			    printx(qw, y, c, d, k ,reg)
			    y = []
		    if x[1] - 2 >= 0 :
		            y.append(x[0])
		            y.append(x[1]-2)
			    #q.put(y)
			    qw += "L"
			    printx (qw, y, c, d, k ,reg)
			    y = []
   

    
t = 0
if __name__ == "__main__":
    n = int(raw_input().strip())
    i_start, j_start, i_end, j_end = raw_input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)

