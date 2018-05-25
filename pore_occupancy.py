import pandas as pd
import matplotlib
import numpy as np
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys

dat = pd.read_csv(sys.argv[1], delimiter='\t')
files = len(sys.argv) 
dat_list = []
dat1_list = [dat]
run_id = dat['run_id'].iloc[0]
print(run_id)

if (files > 2):

    for i in range(2, files):
        print(sys.argv[i])
        try:
            temp = pd.read_csv(sys.argv[i], delimiter='\t')
            run_id_new = temp['run_id'].iloc[0]
            filename = temp['filename'].iloc[0]
            if (run_id_new != run_id and (not ("mux_scan" in filename))):
                run_id = run_id_new
                print(run_id)
                dat = pd.concat(dat1_list, axis = 0)
                dat_list.append(dat)
                dat1_list = []
            else: 
                dat1_list.append(temp)
        except:
            print("boogledy boo")
    dat = pd.concat(dat1_list, axis = 0)
    dat_list.append(dat)

mlen = 0
in_use = np.zeros(0)
i = 1
for dt in dat_list:
    print(i)
    starts = dt['start_time'].as_matrix()
    durs = dt['duration'].as_matrix()

    olen = mlen
    mlen = mlen + np.max(starts + durs)
    in_use = np.pad(in_use, [(0, int(np.ceil(mlen - olen)))], "constant")
    increment = np.bincount((np.ceil(starts) + olen).astype(np.int32), durs, len(in_use))
    in_use += increment
    i += 1
        
def moving_average(a, n):
    ret = np.cumsum(a, dtype=np.float32)
    return (ret[n:] - ret[:-n])/n

plt.figure(figsize=[15, 6])
p = plt.plot(np.arange(len(in_use) - 500)/3600.0, moving_average(in_use, 500)/512)

plt.title("Active pores over time")
plt.xlabel("Time (hr)")
plt.ylabel("Fraction of pores active")
plt.savefig("fraction_active_pores.png")


                                                    
