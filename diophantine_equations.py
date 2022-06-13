
def mcnuggets(x):
    a = 0
    b = 0
    c = 0 
    current_number = 0
    abyx = x//20
    bbyx = x//9
    cbyx = x//6
    current_number1 = 0
    current_sum_of_diophantine = 0
    while current_number1 < x and a <= abyx:
        while a <= abyx and current_sum_of_diophantine < x:
            while b <= bbyx and current_sum_of_diophantine < x:
                while c <= cbyx and current_sum_of_diophantine < x:
                    current_sum_of_diophantine = 20*a + 9*b + 6*c
                    if current_sum_of_diophantine == x:
                        current_number = current_sum_of_diophantine
                        print(x, "= 20*", a, "+ 9*", b,"+ 6*", c)
                    if current_sum_of_diophantine < x:
                        c = c + 1
                    current_number1 = current_sum_of_diophantine
                c = 0
                b = b + 1
                current_sum_of_diophantine = 0
            c = 0
            b = 0
            a = a + 1
    if current_number != x:
        print("Can´t be divided")

        
