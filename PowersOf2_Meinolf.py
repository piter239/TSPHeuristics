# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random as rd
import math
import time
import numpy as np

def power_of_two(n):
    return n & (n - 1) == 0

def next_power_of_2(n):
    if n == 0:
        return 1
    if power_of_two(n):
        return n
    while n & (n - 1) > 0:
        n &= (n - 1)
    return n << 1

class FingerTree:
    def __init__(self,lst):
        self.npot=next_power_of_2(len(lst))
        self.n=2*self.npot
        self.max=lst[-1]
        self.tree=[self.max+1]*self.n
        k=self.npot
        for i in range(0,len(lst)):
            self.tree[k]=lst[i]
            k=k+1
        #print(self.tree)
        h=self.npot//2
        while (h>0):
            k=h
            for i in range(0,h):
                self.tree[k]=self.tree[2*k]
                k=k+1
            h=h//2
        #print(self.tree)
        self.cur=1

    def dive(self,x):
        #print("diving")
        if self.cur>=self.npot:
            #print("starting at bottom")
            #print("error")
            return 0
        if x>=self.max+1:
            #print("input number exceeds max in list")
            return False,self.max+1
        while(self.cur<self.npot):
            l=2*self.cur
            r=l+1
            #print("trying",l,"and",r)
            if self.tree[r]<=x:
                #print("going right")
                self.cur=r
            else:
                #print("going left")
                self.cur=l
        #print("at bottom")
        if self.tree[self.cur]>=x:
            return True,self.tree[self.cur]
        else:
            #print("going one more right at bottom")
            self.cur=self.cur+1
            return True,self.tree[self.cur]

    def from_current(self,x):
        if (self.tree[self.cur]>=x) or (x>self.max):
            return False,self.max+1
        while (self.cur>1):
            self.cur=self.cur//2
            if (power_of_two(self.cur+1)):
                self.cur=1
                break
            if (self.tree[self.cur+1]>=x):
                break
        if(self.cur>=self.npot):
            return True,self.tree[self.cur]
        return self.dive(x)



    def get_next(self,x):
        if self.cur<self.npot:
            return self.dive(x)
        else:
            return self.from_current(x)

    def reset(self):
        self.cur=1

def compute_number(lst):
    # compute number of sums list_i+list_j=s*s for some integer s
    lst.sort()
    a=lst[0]
    n=len(lst)
    b=lst[n-1]
    #print(a,b,n)
    r=b+1-a
    squares=[]
    h=0
    inc=1
    for i in range(0,10**5):
        squares.append(h)
        if i==h:
            h+=inc
            inc+=2
    ft = FingerTree(lst)
    numberOfMatches=0
    for i in range(0, len(lst)):
        x=lst[i]
        #print("new iteration with x=",x)
        h=-x
        if (h < x): h = x
        while True:
            stat,y=ft.get_next(h)
            if (stat==False):
                break
            #print("trying",x,y)
            sum=x+y
            #print(sum)
            if (squares[sum]==sum):
                #print("match",x,"+",y,"=",sum)
                numberOfMatches=numberOfMatches+1
                h=squares[sum+1]-x
                continue
            h=squares[sum]-x
        ft.reset()
    print(numberOfMatches)


def compute_number_np(lst):
    # compute number of sums list_i+list_j=s*s for some integer s
    lst.sort()
    a=lst[0]
    n=len(lst)
    b=lst[n-1]
    #print(a,b,n)
    r=b+1-a
    squares=[]
    h=0
    inc=1
    for i in range(0,r):
        squares.append(h)
        if i==h:
            h+=inc
            inc+=2
    nplst=np.array(lst)
    numberOfMatches=0
    for i in range(0, len(lst)):
        x=lst[i]
        #print("new iteration with x=",x)
        h=-x
        if (h < x): h = x
        while True:
            ind=np.searchsorted(nplst,h)
            if (ind>=len(lst) or ind==0):
                break
            y=nplst[ind]
            #print("trying",x,y)
            sum=x+y
            #print(sum)
            if (squares[sum]==sum):
                #print("match",x,"+",y,"=",sum)
                numberOfMatches=numberOfMatches+1
                h=squares[sum+1]-x
                continue
            h=squares[sum]-x
    print(numberOfMatches)


def solution(numbers):
    ''' Using two pointers technique'''
    m2 = int(math.sqrt(4*10**4))
    lu = [i ** 2 for i in range(m2)]

    num = sorted(numbers)
    #print(len(numbers), len(lu))

    result = 0
    for r in lu:
        left, right = 0, len(num)-1
        while left <= right:
            if num[left] + num[right] == r:
                result += 1
                left += 1
            elif num[left] + num[right] < r:
                left += 1
            else:
                right -= 1

    print(result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hlst=list(range(-2*10**4, 2*10**4))
    lst=rd.sample(hlst,4*10**4)
    #print(lst)
    print("List lenght: ", len(lst))
    t0 = time.time()

    #compute_number(lst)

    t1 = time.time()
    print("FingerTree: ", t1 - t0)
    #compute_number_np(lst)

    t2 = time.time()
    print("Numpy: ", t2 - t1)

    solution(lst)
    t3 = time.time()
    print("TwoPTR: ", t3 - t2)



    #print(lst)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
