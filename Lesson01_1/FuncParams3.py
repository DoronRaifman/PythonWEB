def func1(*positional, **keywords):
    print(f"positional={positional}")
    print(f"keywords={keywords}")


func1(x=12, y=4)
func1(12, y=4)  # mix of positional and named arguments

