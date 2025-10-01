import sys, time, builtins

letters = [
    [chr(i) for i in range(ord('a'), ord('z')+1)],
    [chr(i) for i in range(ord('A'), ord('Z')+1)]
]

def write(arg, delay=0.02):
    result = [" "] * len(arg)
    for idx, ch in enumerate(arg):
        if ch.islower():
            pool = letters[0]
        elif ch.isupper():
            pool = letters[1]
        else:
            result[idx] = ch
            sys.stdout.write("\r" + "".join(result))
            sys.stdout.flush()
            continue

        for letter in pool:
            result[idx] = letter
            sys.stdout.write("\r" + "".join(result))
            sys.stdout.flush()
            time.sleep(delay)
            if letter == ch:
                break
    print()

def fancy_print(*args, **kwargs):
    text = " ".join(str(a) for a in args)
    write(text)

builtins.print = fancy_print