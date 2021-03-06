 #two.py

import one

print("Top of Two.PY")

one.func()

if __name__ == '__main__':
    print('Two.PY is ran directly')
else:
    print('Two.PY is imported')