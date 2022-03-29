""" 
Build index from directory listing
make_index.py --dir </path/to/directory> [--header <header text>]
"""

INDEX_TEMPLATE = r"""
<html>
<body>
<h2>${header}</h2>
<p>
% for name in names:
    <li><a href="${name}">${name}</a></li>
% endfor
</p>
</body>
</html>
"""

EXCLUDED = ['index.html', 'make_index.py', 'update.sh']

import os
import argparse

print("You may need to do > pip3 install --user mako")
from mako.template import Template

parser = argparse.ArgumentParser()
parser.add_argument("--dir")
parser.add_argument("--header")
args = parser.parse_args()

if args.dir is None:
    print("usage: python3 make_index.py --dir </path/to/dir> [--header <header_text>]")
    exit(-1)

fnames = [fname for fname in sorted(os.listdir(args.dir))
          if fname not in EXCLUDED]
header = (args.header if args.header else os.path.basename(args.dir))

f= open("index.html","w+")
f.write(Template(INDEX_TEMPLATE).render(names=fnames, header=header))
f.close()

