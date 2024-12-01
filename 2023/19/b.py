file = open('example.txt', 'r')
lines = file.readlines()
file.close()

workflows = []
parts = []

max_score = 4000

x_options = list(range(1, max_score + 1))
m_options = list(range(1, max_score + 1))
a_options = list(range(1, max_score + 1))
s_options = list(range(1, max_score + 1))

for line in lines:
    if not line.startswith('{') or line.startswith('\n'):
        if line.find(':R') != -1 or line.find(',R}') != -1:
            workflows.append(line.rstrip())

for flow in workflows:
    rules = flow[:-1].split('{')[1]
    rules_list = rules.split(',')
    for rule in rules_list:
        if rule.find(':R') != -1:
            print(rule)
            rules_condition = rules.split(':')
            if rules_condition[0].find('>') != -1:
                segments = rules_condition[0].split('>')
                if segments[0] == 'x':
                    del x_options[int(segments[1]):]
                elif segments[0] == 'm':
                    del m_options[int(segments[1]):]
                elif segments[0] == 'a':
                    del a_options[int(segments[1]):]
                elif segments[0] == 's':
                    del s_options[int(segments[1]):]
            elif rules_condition[0].find('<') != -1:
                segments = rule.split('<')
                if segments[0] == 'x':
                    del x_options[:int(segments[1])]
                elif segments[0] == 'm':
                    del m_options[:int(segments[1])]
                elif segments[0] == 'a':
                    del a_options[:int(segments[1])]
                elif segments[0] == 's':
                    del s_options[:int(segments[1])]

possibilities = len(x_options) * len(m_options) * len(a_options) * len(s_options)

print(possibilities)