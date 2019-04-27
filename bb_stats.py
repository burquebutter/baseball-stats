# bb_stats.py
# Bob Staten
# 4/21/2019

# a python program to calculate a running batting average

base_hits = []
at_bats = []
runs = []

def stats_j(hits,abs,rbis):

#append arguments to lists
  base_hits.append(hits)
  at_bats.append(abs)
  runs.append(rbis)
  
# calculations
  tot_rbis = sum(runs)
  avg = int(round(sum(base_hits) / sum(at_bats), 3) * 1000)
  
  return ('Batting avg: %s' % avg + '\n' + ' ' + 'Runs batted in: %d' % tot_rbis)

# execution
# TODO create a file to store data, and use it to update average.
# here's the problem. I want to store stats in a file instead of keeping them in the code itself as below
stats_j(0,3,1)
stats_j(1,3,2)
print stats_j(2,3,1)
  
