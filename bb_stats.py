# bb_stats.py

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
#print stats_j(2,3,1)
  
