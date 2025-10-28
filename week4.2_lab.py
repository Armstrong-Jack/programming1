
my_veriable = "i am globel"

def test_scope():
    my_veriable = "i am local"
    print(my_veriable)


print(test_scope())

print(my_veriable)