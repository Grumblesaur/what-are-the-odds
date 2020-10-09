#!/usr/bin/python3

def generate_pools(boon=0):
  pools = []
  if boon == 0:
    for x in range(1,7):
      for y in range(1,7):
        pools.append(x+y)
  elif boon < 0:
    for x in range(1,7):
      for y in range(1,7):
        for z in range(1,7):
          pools.append(sum(sorted((x,y,z))[:2]))
  else:
    for x in range(1,7):
      for y in range(1,7):
        for z in range(1,7):
          pools.append(sum(sorted((x,y,z))[1:]))
  return pools

def result_of(pool, cm, rank, dm):
  check = pool + cm + rank + dm
  margin = check - 8
  
  success = None
  degree = None
  
  if margin >= 6:
    success = True
    degree = 'exceptional'
  elif margin in range(1,6):
    success = True
    degree = 'average'
  elif margin == 0:
    success = True
    degree = 'marginal'
  elif margin == -1:
    success = False
    degree = 'marginal'
  elif margin in range(-5, 0):
    success = False
    degree = 'average'
  else:
    success = False
    degree = 'exceptional'
  return (success, degree)

def tabulate(boon, cm, rank, dm):
  pools = generate_pools(boon)
  results = []
  for pool in pools:
    results.append(result_of(pool, cm, rank, dm))
  
  n = len(results)
  pct = n / 100
  s_total  = 0
  f_total  = 0
  s_exc    = 0
  s_avg    = 0
  s_mar    = 0
  f_mar    = 0
  f_avg    = 0
  f_exc    = 0
  
  for result in results:
    success, degree = result
    if success:
      s_total += 1
      if degree == 'marginal':
        s_mar += 1
      elif degree == 'average':
        s_avg += 1
      else:
        s_exc += 1
    else:
      f_total += 1
      if degree == 'marginal':
        f_mar += 1
      elif degree == 'average':
        f_avg += 1
      else:
        f_exc += 1
  
  print('Mongoose Traveller, 2nd Edition')
  print('-------------------------------------------------------')
  print(f'For char mod={cm}, skill rank={rank}, dice mod={dm}, boon={boon}')
  print(f'Number of possible outcomes: {n}')
  print('-------------------------------------------------------')
  print(f'total successes     : {s_total} ({s_total/pct}%)')
  print(f'total failures      : {f_total} ({f_total/pct}%)')
  print('-------------------------------------------------------')
  print(f'success, exceptional: {s_exc} ({s_exc/pct}%)')
  print(f'success, average    : {s_avg} ({s_avg/pct}%)')
  print(f'success, marginal   : {s_mar} ({s_mar/pct}%)')
  print(f'failure, marginal   : {f_mar} ({f_mar/pct}%)')
  print(f'failure, average    : {f_avg} ({f_avg/pct}%)')
  print(f'failure, exceptional: {f_exc} ({f_exc/pct}%)')
  print('-------------------------------------------------------')

def main(characteristic_mod=None, skill_rank=None, dice_mod=None, boon=None):
  if characteristic_mod is None:
    characteristic_mod = int(input('Enter modifier from characteristic: '))
  if skill_rank is None:
    s = input('Enter rank for skill (default: -3): ')
    skill_rank = -3 if not s else int(s)
  if dice_mod is None:
    s = input('Enter dice modifier for difficulty (default: 0): ')
    dice_mod = 0 if not s else int(s)
  if boon is None:
    s = input('Enter boon (-1, 0, 1 | default: 0): ')
    boon = 0 if not s else int(s)
  tabulate(boon, characteristic_mod, skill_rank, dice_mod)

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    args = tuple(map(int, sys.argv[1:]))
  else:
    args = (None,) * 4
  main(*args)


