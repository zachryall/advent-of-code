file = open('input.txt', 'r')
lines = file.readlines()
file.close()

workflows = []
parts = []

total_rating = 0


for line in lines:
    if line.startswith('{'):
        parts.append(line.rstrip())
    elif line.startswith('\n'):
        print('')
    else:
        workflows.append(line.rstrip())


def process_part(part_info):
    next_flow = 'in'
    ldict = {}

    print('------')

    ratings = part_info[1:-1].split(',')

    exec(ratings[0], globals(), ldict)
    exec(ratings[1], globals(), ldict)
    exec(ratings[2], globals(), ldict)
    exec(ratings[3], globals(), ldict)
    x = ldict['x']
    m = ldict['m']
    a = ldict['a']
    s = ldict['s']

    while next_flow not in ['A', 'R']:
        flow_line = next(flow for flow in workflows if flow.startswith(next_flow + '{'))[:-1]
        print(flow_line)
        flow_list = flow_line.split('{')
        flow_rules_list = flow_list[1].split(',')

        for flow_rule in flow_rules_list:
            flow_rule_list = flow_rule.split(':')
            if any(rule in flow_rule_list[0] for rule in [">", "<"]):
                if eval(flow_rule_list[0]):
                    next_flow = flow_rule_list[1]
                    break
            else:
                next_flow = flow_rule_list[0]
                print(next_flow)

    if next_flow == 'A':
        return x + m + a + s
    elif next_flow == 'R':
        return 0


for part in parts:
    total_rating += process_part(part)

print(total_rating)
