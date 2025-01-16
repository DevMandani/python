marks={
    "dev":99,
    "jayshreedidi":100,
    "priyank":99,
}

print(marks.keys())
print(marks.values())

marks.update({"jayshreedidi":99,"priyank":98,"komaldidi":99})
print(marks)

print(marks.get("dev"))

print(marks["dev"])