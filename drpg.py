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

def generate_pools():
  pools = []
  for x in range(1,21):
    for y in range(1,21):
      pools.append((x, y))
  return pools

def tabulate(skill, style, focus, difficulty):
  pools = generate_pools()
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
  f_2_comp = 0
  s_comp_1_mo = 0
  
  c_total = 0
  not_c_total = 0
  
  for result in results:
    if result[0]:
      s_total += 1
      if result[1] and result[2]:
        s_comp_1_mo += 1
        c_total += 1
      if result[1] and not result[2]:
        s_comp += 1
        c_total += 1
      if not result[1] and result[2]:
        if result[2] == 1:
          s_1_mo += 1
        elif result[2] == 2:
          s_2_mo += 1
        else:
          s_3_mo += 1
        not_c_total += 1
      if not result[1] and not result[2]:
        not_c_total += 1
    else:
      f_total += 1
      if result[1] == 1:
        f_1_comp += 1
        c_total += 1
      elif result[1] == 2:
        f_2_comp += 1
        c_total += 1
      else:
        not_c_total += 1
  
  s_plain = s_total - (s_3_mo + s_2_mo + s_1_mo + s_comp + s_comp_1_mo)
  f_plain = f_total - (f_1_comp + f_2_comp)
  
  mo_total = (s_3_mo + s_2_mo + s_1_mo + s_comp_1_mo)
  not_mo_total = n - mo_total
  
  print('Dishonored RPG')
  print('-------------------------------------------')
  print(f'For skill={skill}, style={style}, focus={focus}, diff={difficulty}')
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
  print(f'successes, 3 mo        : {s_3_mo} ({s_3_mo/pct}%)')
  print(f'successes, 2 mo        : {s_2_mo} ({s_2_mo/pct}%)')
  print(f'successes, 1 mo        : {s_1_mo} ({s_1_mo/pct}%)')
  print(f'successes, 1 comp      : {s_comp} ({s_comp/pct}%)')
  print(f'successes, 1 comp, 1 mo: {s_comp_1_mo} ({s_comp_1_mo/pct}%)')
  print(f'successes, plain       : {s_plain} ({s_plain/pct}%)')
  print(f'failures,  1 comp      : {f_1_comp} ({f_1_comp/pct}%)')
  print(f'failures,  2 comp      : {f_2_comp} ({f_2_comp/pct}%)')
  print(f'failures,  plain       : {f_plain} ({f_plain/pct}%)')
  print('-------------------------------------------')


def main(skill=None, style=None, focus=None, diff=None):
  if skill is None:
    skill = int(input('Enter skill value: '))
  if style is None:
    style = int(input('Enter style value: '))
  if focus is None:
    focus = int(input('Enter focus value: '))
  if diff is None:
    diff = int(input('Enter difficulty: '))
  tabulate(skill, style, focus, diff)

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1:
    args = tuple(map(int, sys.argv[1:]))
  else:
    args=(None,)*4
  main(*args)

