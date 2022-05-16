a = [] ; b = [] ; c = [] ; d = [] ; e = [] ; f = []
for A in range(1,7) :
    for B in range(1,7) :
        for C in range(1,7) :
            for D in range(1,7) :
                for E in range(1,7) :
                    for F in range(1,7) :
                        if A<C and C<D and D<F and F>E and B<E and A<B and F==2*A :
                            a.append(A)
                            b.append(B)
                            c.append(C)
                            d.append(D)
                            e.append(E)
                            f.append(F)
print('A = ',sorted(list(set(a))))
print('B = ',sorted(list(set(b))))
print('C = ',sorted(list(set(c))))
print('D = ',sorted(list(set(d))))
print('E = ',sorted(list(set(e))))
print('F = ',sorted(list(set(f))))