import sys
import dparse
import dlex

# sys.path.insert(0, "Dino>>")
#
# if len(sys.argv) == 2:
#     with open(sys.argv[1]) as f:
#         data = "1 plus 1"
#     prog = dparse.parse(data)
#     if not prog:
#         raise SystemExit

# prog = dparse.parse("1 divided by 0")

#
while True:
    try:
        line = input("[Dino] ")
        if line == "<end>":
            break
    except EOFError:
        raise SystemExit
    if not line:
        continue
    line += "\n"
    prog = dparse.parse(line)
    print(prog)
    if not prog:
        continue

    # keys = list(prog)
    # if keys[0] > 0:
    #     b.add_statements(prog)
    # else:
    #     stat = prog[keys[0]]
    #     if stat[0] == 'RUN':
    #         try:
    #             b.run()
    #         except RuntimeError:
    #             pass
    #     elif stat[0] == 'LIST':
    #         b.list()
    #     elif stat[0] == 'BLANK':
    #         b.del_line(stat[1])
    #     elif stat[0] == 'NEW':
    #         b.new()