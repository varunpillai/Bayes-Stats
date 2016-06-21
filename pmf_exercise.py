import Pmf

def PrintPmf(pmf):
    for value, prob in pmf.Items():
        print value, prob

def ProbBigger(pmf1, pmf2):
    total = 0
    for v1, p1 in pmf1.Items():
        for v2, p2 in pmf2.Items():
            if v1 > v2:
                total += p1*p2
    return total

six_sided_die = Pmf.MakePmfFromList([1, 2, 3, 4, 5, 6])
ten_sided_die = Pmf.MakeHistFromList(range(1, 11))
PrintPmf(six_sided_die)
PrintPmf(ten_sided_die)

print 'Prob ten-side is bigger: ', ProbBigger(ten_sided_die, six_sided_die)




