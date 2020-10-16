#!/usr/bin/python3

def generate_pools():
  pools = []
  for x in range(1,7):
    for y in range(1,7):
      pools.append(x+y)
  return pools

def result_of(pool, attr, skill, diff, circ):
  check = pool + attr + skill + circ
  return check >= diff

def tabulate(attr, skill, diff, circ):
  pools = generate_pools()
  results = []
  for pool in pools:
    results.append(result_of(pool, attr, skill, diff, circ))
  
  n = len(results)
  pct = n / 100
  s_total = 0
  f_total = 0
  
  for result in results:
    if result:
      s_total += 1
    else:
      f_total += 1
  
  print('Stars Without Number')
  print('-------------------------------------------------------')
  print(f'For attr mod={attr}, skill level={skill}, diff={diff}, circ={circ}')
  print(f'Number of possible outcomes: {n}')
  print('-------------------------------------------------------')
  print(f'total successes     : {s_total} ({s_total/pct}%)')
  print(f'total failures      : {f_total} ({f_total/pct}%)')

def main(attribute_mod=None, skill_level=None, difficulty=None, circ=None):
  if attribute_mod is None:
    s = input('Enter attribute modifier (default: 0): ')
    attribute_mod = 0 if s == '' else int(s)
  if skill_level is None:
    s = input('Enter skill level (default: -1): ')
    skill_level = -1 if s == '' else int(s)
  if difficulty is None:
    s = input('Enter difficulty (default: 6): ')
    difficulty = 6 if s == '' else int(s)
  if circ is None:
    s = input('Enter circumstance (default: 0): ')
    circ = 0 if s == '' else int(s)
  tabulate(attribute_mod, skill_level, difficulty, circ)

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    args = tuple(map(int, sys.argv[1:]))
  else:
    args = (None,) * 4
  main(*args)


