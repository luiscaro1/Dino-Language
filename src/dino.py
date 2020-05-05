import sys
import dparse
import dlex

sys.path.insert(0, "Dino>>")

if len(sys.argv) == 2:
    with open(sys.argv[1]) as f:
        data = f.read()
    prog = dparse.parse(data)
    if not prog:
        raise SystemExit
