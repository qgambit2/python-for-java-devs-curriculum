"""Lesson 1g — Java ↔ Python quick reference."""

print("""
Java                    Python
----                    ------
System.out.println(x)   print(x)
null                    None
true / false            True / False
ArrayList<String>       list ([])
HashMap / LinkedHashMap dict ({}) — insertion order since 3.7
.length / .size()       len(x)
new ArrayList<>(list)   list[:]  list.copy()  list(lst)
new HashMap<>(map)      {**d}  d.copy()  dict(d)   (no d[:]!)
@Override                (no keyword; just redefine)
public static void      def name():
""")
