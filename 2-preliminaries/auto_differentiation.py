
def square(x):
    return x*x* x

if __name__ == "__main__":
    import torch 
    print("z = x^T w - y") 
    x = torch.arange(4.0, requires_grad=True)
    print("x is {}".format(x))

    w = torch.arange(4.0) + 2
    w.requires_grad_(True)
    print("w is {}".format(w))

    y = torch.rand(1)
    print("y is {}".format(y))

    z = torch.dot(w, x) - y
    print("z is {}".format(z))

    print("now calculate the grad of z")
    print("dz/dw = x^T")

    z.backward()
    print("dz/dx: x.grad: {}".format(x.grad))
    print("dz/dw: w.grad: {}".format(w.grad))

    print("d = f(a)")
    a = torch.randn(1, requires_grad=True)
    print("a={}".format(a))
    d = square(a)
    print("d={}".format(d))
    d.backward()
    print("dd/da={}".format(a.grad))


