#!/usr/bin/env python
# coding: utf-8

# In[2]:


processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 4, 5, 6]
burst_time = [24, 3, 3, 12]
priority = [3, 1, 4, 2]
n = len(processes)

def waiting_time(bt, wt, tat):
    wt[0] = 0
    for i in range(1, n):
        wt[i] = tat[i-1] - bt[i-1]

def turnaround_time(bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]


def fcfs():
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0

  
    for i in range(1, n):
        wt[i] = burst_time[i-1] + wt[i-1]

   
    turnaround_time(burst_time, wt, tat)

    return wt, tat


def sjf():
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0


    for i in range(n):
        wt[i] = 0
        for j in range(i):
            wt[i] += burst_time[j]

  
    turnaround_time(burst_time, wt, tat)

    return wt, tat


def ps():
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0
    for i in range(1, n):
        wt[i] = burst_time[i-1] + wt[i-1]
    turnaround_time(burst_time, wt, tat)
    return wt, tat



def rr(quantum):
    wt, tat = [0] * n, [0] * n
    total_wt, total_tat = 0, 0
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = burst_time[i]

    t = 0
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t = t + rem_bt[i]
                    wt[i] = t - burst_time[i]
                    rem_bt[i] = 0

        if done:
            break

  
    turnaround_time(burst_time, wt, tat)

    return wt, tat

fcfs_wt, fcfs_tat = fcfs()
sjf_wt, sjf_tat = sjf()
ps_wt, ps_tat = ps()
rr_wt, rr_tat = rr(4)


avg_wt = {
    "FCFS": sum(fcfs_wt) / n,
    "SJF": sum(sjf_wt) / n,
    "PS": sum(ps_wt) / n,
    "RR": sum(rr_wt) / n
}

avg_tat = {
    "FCFS": sum(fcfs_tat) / n,
    "SJF": sum(sjf_tat) / n,
    "PS": sum(ps_tat) / n,
    "RR": sum(rr_tat) / n
}


def display_results(algorithm_name, wt, tat):
    print(f"\n{algorithm_name} Scheduling:")
    print("Process\t\tWT\t\tTAT")
    for i in range(n):
        print(f"{processes[i]}\t\t{wt[i]}\t\t{tat[i]}")
    print(f"Average WT: {sum(wt)/n}")
    print(f"Average TAT: {sum(tat)/n}")

fcfs_wt, fcfs_tat = fcfs()
display_results("FCFS", fcfs_wt, fcfs_tat)

sjf_wt, sjf_tat = sjf()
display_results("SJF", sjf_wt, sjf_tat)

ps_wt, ps_tat = ps()
display_results("PS", ps_wt, ps_tat)

rr_wt, rr_tat = rr(4)
display_results("RR", rr_wt, rr_tat)

avg_wt = {
    "FCFS": sum(fcfs_wt) / n,
    "SJF": sum(sjf_wt) / n,
    "PS": sum(ps_wt) / n,
    "RR": sum(rr_wt) / n
}

avg_tat = {
    "FCFS": sum(fcfs_tat) / n,
    "SJF": sum(sjf_tat) / n,
    "PS": sum(ps_tat) / n,
    "RR": sum(rr_tat) / n
}


most_suitable = min(avg_wt, key=avg_wt.get)

print(f"\nMost suitable scheduling algorithm is {most_suitable} with average waiting time of {avg_wt[most_suitable]} and average turnaround time of {avg_tat[most_suitable]}")


# In[ ]:




