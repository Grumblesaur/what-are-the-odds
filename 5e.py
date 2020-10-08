#!/usr/bin/python3

def generate_pools(adv=0):
  '''Second die is only for confirmation if first die is a crit.'''
  pools = []
  if adv == 0:
    for x in range(1, 21):
      for y in range(1, 21):
        pools.append((x, y))
  elif adv == 1:
    for x in range(1, 21):
      for y in range(1, 21):
        for z in range(1, 21):
          pools.append((max(x, y), z))
  else:
    for x in range(1, 21):
      for y in range(1, 21):
        for z in range(1, 21):
          pools.append((min(x, y), z))
  return pools

def result_of(pool, prof, mod, dc):
  roll, confirm = pool
  success = None
  critical = None
  if roll == 20 and confirm == 20:
    success = True
    critical = True
  elif roll == 1 and confirm == 1:
    success = False
    critical = True
  else:
    check = roll + prof + mod
    if check >= dc:
      success = True
      critical = False
    else:
      success = False
      critical = False
  return (success, critical)

def tabulate(prof, mod, adv, dc):
  pools = generate_pools(adv)
  results = []
  for pool in pools:
    results.append(result_of(pool, prof, mod, dc))
  
  n = len(results)
  pct = n / 100
  s_total = 0
  f_total = 0
  s_crit  = 0
  f_crit  = 0
  
  for result in results:
    s, c = result
    if s:
      s_total += 1
      if c:
        s_crit += 1
    else:
      f_total += 1
      if c:
        f_crit += 1
  
  s_plain = s_total - s_crit
  f_plain = f_total - f_crit
  
  print('Dungeons & Dragons, 5th Edition')
  print('----------------------------------------------')
  print(f'For prof={prof}, mod={mod}, adv={adv}, dc={dc}')
  print(f'Number of possible outcomes: {n}')
  print('----------------------------------------------')
  print(f'total successes: {s_total} ({s_total/pct}%)')
  print(f'total failures : {f_total} ({f_total/pct}%)')
  print('----------------------------------------------')
  print(f'plain successes: {s_plain} ({s_plain/pct}%)')
  print(f'crit  successes: {s_crit} ({s_crit/pct}%)')
  print(f'plain failures : {f_plain} ({f_plain/pct}%)')
  print(f'crit  failures : {f_crit} ({f_crit/pct}%)')
  print('----------------------------------------------')

def main(prof=None, mod=None, adv=None, dc=None):
  if prof is None:
    prof = int(input('Enter proficiency: '))
  if mod is None:
    mod = int(input('Enter ability modifier: '))
  if adv is None:
    adv = int(input('Enter (dis)advantage (-1, 0, 1): '))
  if dc is None:
    dc = int(input('Enter difficulty class: '))
  tabulate(prof, mod, adv, dc)

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    args = tuple(map(int, sys.argv[1:]))
  else:
    args = (None,) * 4
  main(*args)
  
