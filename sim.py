#!/usr/bin/python
#my first ever kinda long python code
#by abdullah samarkandi 
# 
# 
import sys, getopt
import random

from itertools import izip, chain

def main():
	print("fifo or sjf or rr?")
	ty = raw_input()
	 
	bt=[]
	print("Enter the number of process: ")
        n=int(input())
	
	print("Enter the burst time of the processes: ")
        bt=list(map(int, raw_input().split()))


	if   ty == "fifo":fifo(n, bt)
	elif ty == "sjf": sjf (n, bt)
	elif ty == "rr":
		print("quantum?")
		quantum = int(input()) 
		rr(n, bt, quantum)
	else:	
		print("error")
		sys.exit() 

def rr(n, bt, quantum):
	wt=[]
	avgwt=0
	tat=[]
	avgtat=[]
	avgtat=0	

	rem_bt=[]
	t=0
	rem_bt =list(bt)   	#Make a copy of burst times bt[] to store remaining burst times.
	
	tat.insert(0,0)
	while True: 
		done = 1 
		for i in range(0,n):
			if rem_bt[i] > 0:
				done = 0 
				if rem_bt[i] > quantum:
					t = t+ quantum
					rem_bt[i] -= quantum
				else:
					t = t + rem_bt[i]
					
       					wt.append(t -bt[i])
       					rem_bt[i] = 0; 		# This process is over
		if done == 1: 
			break
	total_wt =0
	for i in range(1,len(bt)):
		tat.insert(i,wt[i]+bt[i])
		avgwt+=wt[i]
		avgtat+=tat[i]

	avgtat=float(avgtat)/n
	avgwt=float(avgwt)/n

  	print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
	
	for i in range(0,n):
		print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
		print("\n")




	status(avgwt, avgtat)

def fifo(n, bt):
	 
	wt=[] 					#waiting time 
	avgwt=0
	tat=[]
	avgtat=0

	wt.insert(0,0)
	tat.insert(0,bt[0])
	for i in range(1,len(bt)):
		wt.insert(i,wt[i-1]+bt[i-1])
		tat.insert(i,wt[i]+bt[i])
 		avgwt+=wt[i]
 		avgtat+=tat[i]

	avgwt=float(avgwt)/n
	avgtat=float(avgtat)/n
	
	print("\n")
	print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")

	for i in range(0,n):
		print(str(i)+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
		print("\n")
	status(avgwt, avgtat)


def sjf(n, bt):
	
	processes=[]
	for i in range(0,n):
		processes.insert(i,i+1)
	
	for i in range(0,len(bt)-1):  #applying bubble sort to sort process according to their burst time
 		for j in range(0,len(bt)-i-1):
  			if(bt[j]>bt[j+1]):
   				temp=bt[j]
   				bt[j]=bt[j+1]
   				bt[j+1]=temp
   				temp=processes[j]
   				processes[j]=processes[j+1]
				processes[j+1]=temp
	wt=[]    #wt stands for waiting time
	avgwt=0  #average of waiting time
	tat=[]    #tat stands for turnaround time
	avgtat=0   #average of total turnaround time
	wt.insert(0,0)
	tat.insert(0,bt[0])
	for i in range(1,len(bt)):  
		wt.insert(i,wt[i-1]+bt[i-1])
		tat.insert(i,wt[i]+bt[i])
		avgwt+=wt[i]
 		avgtat+=tat[i]
	avgwt=float(avgwt)/n
	avgtat=float(avgtat)/n
	
	print("\n")
	print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
	for i in range(0,n):
		print(str(processes[i])+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
		print("\n")
	status(avgwt, avgtat)


def status(avgwt, avgtat): 
        print("Average Waiting time is: "+str(avgwt))
        print("Average Turn Around Time is: "+str(avgtat))



main()

