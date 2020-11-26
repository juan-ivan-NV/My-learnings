Not = lambda X: (X)(false)(true)
And = lambda X: lambda Y: (X)(Y)(X)
Or = lambda X: lambda Y: (X)(X)(Y)
Xor = lambda X: lambda Y: (Y)(Not(X))(X)