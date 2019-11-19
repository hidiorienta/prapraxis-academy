print(list(map(int, ["1", "2", "3"])))

def hello_world(h):
    def world(w):
        print(h, w)
        return world # returning functions

h = hello_world # assigning
x = h("hello") # assigning

print(x("world"))

function_list = [h, x]
print(function_list)