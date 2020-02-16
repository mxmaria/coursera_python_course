# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой, при условии, что поворачивать коробки можно только на 90 градусов вокруг ребер.

A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
if ((A1 == A2 and B1 == B2 and C1 == C2) or
        (A1 == B2 and B1 == C2 and C1 == A2) or
        (A1 == C2 and B1 == B2 and C1 == A2) or
        (A1 == C2 and B1 == A2 and C1 == B2) or
        (A1 == B2 and B1 == A2 and C1 == C2) or
        (A1 == A2 and B1 == C2 and C1 == B2)):
    print('Boxes are equal')
elif ((A1 <= A2 and B1 <= B2 and C1 <= C2) or
        (A1 <= B2 and B1 <= C2 and C1 <= A2) or
        (A1 <= C2 and B1 <= B2 and C1 <= A2) or
        (A1 <= C2 and B1 <= A2 and C1 <= B2) or
        (A1 <= B2 and B1 <= A2 and C1 <= C2) or
        (A1 <= A2 and B1 <= C2 and C1 <= B2)):
    print('The first box is smaller than the second one')
elif ((A1 >= A2 and B1 >= B2 and C1 >= C2) or
        (A1 >= B2 and B1 >= C2 and C1 >= A2) or
        (A1 >= C2 and B1 >= B2 and C1 >= A2) or
        (A1 >= C2 and B1 >= A2 and C1 >= B2) or
        (A1 >= B2 and B1 >= A2 and C1 >= C2) or
        (A1 >= A2 and B1 >= C2 and C1 >= B2)):
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
