import os
t = os.get_terminal_size()
print(t)
print(t.columns)
print(t.lines)
t = os.terminal_size((80,40))
print(t)
print(t.columns)
print(t.lines)

