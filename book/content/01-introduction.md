# Introduction

You already think in types, APIs, and collections. You know `ArrayList`, `HashMap`, and `HashSet`. You have muscle memory for `indexOf`, `put`, and `getOrDefault`.

This book does not talk down to you. It maps what you know to what Python does differently — and shows you the idioms experienced Python developers actually write.

## Who this book is for

Expert Java developers learning Python for real work: scripts, services, data plumbing, and eventually agents and cloud code in this curriculum.

## How Python will feel at first

Three shifts hit Java developers early:

1. **Indentation is syntax.** Blocks are not wrapped in braces.
2. **Types are optional at runtime.** Hints help tools; the interpreter does not enforce them.
3. **The standard library is the playground.** Lists, dicts, and sets are built in — no `java.util` imports for the basics.

## What makes Python collections different

| Java habit | Python reality |
|------------|----------------|
| `ArrayList`, `HashMap` | `list`, `dict` — literals with `[]` and `{}` |
| `LinkedHashMap` for order | `dict` keeps insertion order (since 3.7) |
| `Pair`, `Map.entry` | `tuple` — and unpacking: `x, y = point` |
| `HashSet` utilities | `set` with operators `\|`, `&`, `-`, `^` |
| `list.indexOf` returns -1 | `list.index` raises `ValueError` — check with `in` first |

## Preview edition

This PDF is an early **preview**. Chapters 1–2 are written as teaching prose. Later lessons appear as a roadmap. The runnable source of truth remains the `lesson_NN/` files in the repository — run them, change them, break them, fix them.

> **Java:** Think of each lesson file as a executable tutorial — like a JShell script you run from the terminal, not a slide deck.
