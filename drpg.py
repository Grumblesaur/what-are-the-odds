#!/usr/bin/python3

def result_of(pool, skill, style, focus, difficulty):
  '''Calculates the number of successes and complications from
    pool:  a list of results from d20s
    skill: a number that determine's a character's skill level
    style: a number that determine's a character's style proficiency
    focus: the value under which a roll counts as a double success
    difficulty: the number of successes'''
  comp = 0
  succ = 0
  fail = 0
  
  for die in pool:
    if die <= focus:
      succ += 2
    elif die <= skill + style:
      succ += 1
    elif die < 20:
      fail += 1
    else:
      fail += 1
      comp += 1
  
  passed = False
  if succ >= difficulty:
    passed = True
  
  momentum = 0 if not passed else succ - difficulty
  
  return (passed, comp, momentum)

def generate_pools(mo):
  # The runtime complexity on this is bad and I should feel bad, but it's
  # a very easy way to enumerate permutations.
  pools = []
  if mo == -1:
    for x in range(1, 21):
      pools.append((x,))
  elif mo == 0:
    for x in range(1,21):
      for y in range(1,21):
        pools.append((x, y))
  elif mo == 1:
    for x in range(1, 21):
      for y in range(1, 21):
        for z in range(1, 21):
          pools.append((x, y, z))
  elif mo == 2:
    for x in range(1, 21):
      for y in range(1, 21):
        for z in range(1, 21):
          for w in range(1, 21):
            pools.append((x, y, z, w))
  else:
    for x in range(1, 21):
      for y in range(1, 21):
        for z in range(1, 21):
          for w in range(1, 21):
            for v in range(1, 21):
              pools.append((x, y, z, w, v))
  return pools

def tabulate(skill, style, focus, difficulty, momentum):
  pools = generate_pools(momentum)
  results = []
  for pool in pools:
    results.append(result_of(pool, skill, style, focus, difficulty))
  
  n = len(results)
  pct = n / 100
  s_total = 0
  f_total = 0
  s_1_mo = 0
  s_2_mo = 0
  s_3_mo = 0
  s_comp = 0
  f_1_comp = 0
  f_2p_comp = 0
  s_comp_mo = 0
  
  c_total = 0
  
  for result in results:
    success, comp, mo = result
    if success:
      s_total += 1
      if comp and mo:
        s_comp_mo += 1
        c_total += 1
      if comp and not mo:
        s_comp += 1
        c_total += 1
      if not comp and mo:
        if mo == 1:
          s_1_mo += 1
        elif mo == 2:
          s_2_mo += 1
        else:
          s_3_mo += 1
    else:
      f_total += 1
      if comp == 1:
        f_1_comp += 1
        c_total += 1
      elif comp == 2:
        f_2p_comp += 1
        c_total += 1
  
  s_plain = s_total - (s_3_mo + s_2_mo + s_1_mo + s_comp + s_comp_mo)
  f_plain = f_total - (f_1_comp + f_2p_comp)
  
  mo_total = (s_3_mo + s_2_mo + s_1_mo + s_comp_mo)
  not_mo_total = n - mo_total
  not_c_total = n - c_total 
  header = ', '.join([
    f'For skill={skill}',
    f'style={style}',
    f'focus={focus}',
    f'diff={difficulty}',
    f'mo={momentum}'
  ])
  
  print('Dishonored RPG')
  print('-------------------------------------------')
  print(header)
  print(f'Number of possible outcomes: {n}')
  print('-------------------------------------------')
  print(f'total successes        : {s_total} ({s_total/pct}%)')
  print(f'total failures         : {f_total} ({f_total/pct}%)')
  print('-------------------------------------------')
  print(f'rolls w/  comp         : {c_total} ({c_total/pct}%)')
  print(f'rolls w/o comp         : {not_c_total} ({not_c_total/pct}%)')
  print('-------------------------------------------')
  print(f'rolls w/  mo           : {mo_total} ({mo_total/pct}%)')
  print(f'rolls w/o mo           : {not_mo_total} ({not_mo_total/pct}%)')
  print('-------------------------------------------')
  print(f'successes, 3+ mo       : {s_3_mo} ({s_3_mo/pct}%)')
  print(f'successes, 2 mo        : {s_2_mo} ({s_2_mo/pct}%)')
  print(f'successes, 1 mo        : {s_1_mo} ({s_1_mo/pct}%)')
  print(f'successes, comp        : {s_comp} ({s_comp/pct}%)')
  print(f'successes, comp, mo    : {s_comp_mo} ({s_comp_mo/pct}%)')
  print(f'successes, plain       : {s_plain} ({s_plain/pct}%)')
  print(f'failures,  1 comp      : {f_1_comp} ({f_1_comp/pct}%)')
  print(f'failures,  2+ comp      : {f_2p_comp} ({f_2p_comp/pct}%)')
  print(f'failures,  plain       : {f_plain} ({f_plain/pct}%)')
  print('-------------------------------------------')


def main(skill=None, style=None, focus=None, diff=None, momentum=None):
  if skill is None:
    skill = int(input('Enter skill value: '))
  if style is None:
    style = int(input('Enter style value: '))
  if focus is None:
    focus = int(input('Enter focus value: '))
  if diff is None:
    diff = int(input('Enter difficulty: '))
  if momentum is None:
    s = input('Enter momentum (-1 for a help pool): ')
    momentum = 0 if not s else int(s)
  tabulate(skill, style, focus, diff, momentum)

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    args = tuple(map(int, sys.argv[1:]))
  else:
    args=(None,)*4
  main(*args)

