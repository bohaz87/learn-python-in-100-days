import foo
import bar

foo.foo()
bar.bar()

import foo as f
import bar as b
f.foo();
b.bar()

from foo import foo
foo()

from bar import bar
bar()

from foo import foo as ff
ff()

from bar import bar as bb
bb()