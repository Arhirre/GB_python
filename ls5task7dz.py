# _author_ = Nikita_Savchenko

import json
finish_list = []
comp_profit = {}
comp_counter = 0
prof_aver = 0
prof_total = 0

with open('task7text_input.txt', 'r') as my_file:
    for l in my_file:
        name, firm_type, earn, loss = l.split()
        comp_profit[name] = int(earn) - int(loss)
        if comp_profit.setdefault(name) > 0:
            prof_total = prof_total + comp_profit.setdefault(name)
            comp_counter += 1
    if comp_counter != 0:
        prof_aver = prof_total / comp_counter
    pr = {'Average profit= ': prof_aver}
    finish_list.append(comp_profit)
    finish_list.append(pr)
    print(f'Profit by company: {finish_list}')

with open('task7json_out.json', 'w') as write_js:
    json.dump(finish_list, write_js)
    js_str = json.dumps(finish_list)
    print({js_str})
