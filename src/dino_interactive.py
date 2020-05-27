import sys
import dparse
import dlex
import dinterp


# ###Interactive Mode###         ### in development
interp = dinterp.DinoInterp(prog=None)
vars = {'this':'Dino Language'}
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
    interp.setVariables(vars)
    interp.comp(prog)
    vars = interp.getVariables
    interp.run()

    if not prog:
        continue
# #########################
