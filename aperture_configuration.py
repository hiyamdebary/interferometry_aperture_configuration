"""
Author: Hiyam Debary
Script allowing to produce pupil configurations given the amount of baselines (n_pup/2) and
the first measured baseline of the compact frequency coverage (m).

The tables correspond to the ones found in the papers by Skolem 1958 (for baselines starting at 1),
Simpson 1983 and Bermond 1976 (baselines starting at at least 3)
.
A function is written for the Davies 1959 solutions for baselines starting from 2.
More details are written below.

The tables are filled to be under the form:
(a_i) d*t + e*s + c + f*j, (b_i) dp*t + ep*s + cp + fp*j, (j) aj*t + bj*s + cj
"""
## First table in Skolem 1958
table_skolem_1 = [
           (4,  0,  0,  1,  8,  0,  0, -1,  2,  0, -1),
           (2,  0,  1,  0,  6,  0,  0,  0,  0,  0,  0),
           (2,  0,  0,  0,  4,  0, -1,  0,  0,  0,  0),
           (0,  0,  1,  1,  4,  0, -2, -1,  1,  0, -2),
           (1,  0,  0,  0,  1,  0,  1,  0,  0,  0,  0),
           (1,  0,  2,  1,  3,  0, -1, -1,  1,  0, -3)
           ]

## Second table in Skolem 1958
table_skolem_2 = [
           (4,  0,  2,  1,  8,  0,  2, -1,  2,  0, -1),
           (2,  0,  1,  0,  6,  0,  2,  0,  0,  0,  0),
           (2,  0,  2,  0,  4,  0,  1,  0,  0,  0,  0),
           (0,  0,  1,  1,  4,  0,  0, -1,  1,  0, -1),
           (1,  0,  1,  0,  1,  0,  2,  0,  0,  0,  0),
           (1,  0,  3,  1,  3,  0,  0, -1,  1,  0, -3)
           ]

## First table in Simpson 1983
table_1 = [(2, -3,  1, -1,  2,  1,  2,  1,  1, -2, -1),
           (1, -2,  1, -1,  3,  1,  1,  1,  1, -2,  0),
           (6, -1,  1, -1,  6,  3,  1,  1,  1, -2, -1),
           (5, -1,  1, -1,  7,  2,  0,  1,  1, -2,  0),
           (3, -1,  2,  0,  5, -1,  2,  0,  0,  0,  0),
           (2,  0,  0, -1,  4,  0,  1,  1,  0,  1, -1),
           (4, -1,  2,  1,  6,  1,  2,  2,  0,  1, -2),
           (3,  0,  1, -1,  5,  0,  3,  1,  0,  1, -2),
           (3,  1,  0, -1,  7,  1,  1,  1,  0,  1, -2),
           (1, -1,  1, -1,  5, -1,  3,  1,  0,  1, -1),
           (2, -3,  2,  1,  6, -1,  3,  2,  0,  2, -2),
           (2,  0,  1,  1,  6, -1,  2,  2,  0,  1, -1),
           (2,  1,  1,  0,  6,  3,  0,  0,  0,  0,  0)
           ]

## Second table in Simpson 1983
table_2 = [(2, -3, -1, -1,  2,  1,  2,  1,  1, -2, -2),
           (1, -2,  0, -1,  3,  1,  1,  1,  1, -2, -1),
           (6, -1,  0, -1,  6,  3,  2,  1,  1, -2, -2),
           (5, -1, -1, -1,  7,  2,  1,  1,  1, -2, -2),
           (5, -1,  0,  0,  7,  1,  1,  0,  0,  0,  0),
           (2,  0,  0, -1,  4,  0,  1,  1,  0,  1, -1),
           (4, -1,  1,  1,  6,  1,  3,  2,  0,  1, -2),
           (3,  0,  1, -1,  5,  0,  1,  1,  0,  1,  0),
           (3,  1,  0, -1,  7,  1,  2,  1,  0,  1, -2),
           (1, -1,  0, -1,  5, -1,  1,  1,  0,  1, -1),
           (2, -3,  0,  1,  6, -1,  2,  2,  0,  2, -1),
           (2,  0,  1,  1,  6, -1,  1,  2,  0,  1, -1),
           (2,  1,  1,  0,  6,  3,  1,  0,  0,  0,  0),
           (2, -1,  0,  0,  6,  1,  1,  0,  0,  0,  0),
           (4,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0)
           ]

## Third table in Simpson 1983
table_3 = [(2, -3,  1, -1,  2,  1,  1,  1,  1, -2, -1),
           (1, -2,  2, -1,  3,  1,  0,  1,  1, -2,  1),
           (6, -1,  0, -1,  6,  3, -1,  1,  1, -2,  0),
           (5, -1,  1, -1,  7,  2,  0,  1,  1, -2,  0),
           (3, -1,  1,  0,  5, -1,  2,  0,  0,  0,  0),
           (2,  0,  1, -1,  4,  0,  1,  1,  0,  1, -1),
           (4, -1,  2,  1,  6,  1,  1,  2,  0,  1, -2),
           (3,  0, -1, -1,  5,  0,  2,  1,  0,  1, -3),
           (3,  1, -1, -1,  7,  1,  0,  1,  0,  1, -1),
           (1, -1,  1, -1,  5, -1,  3,  1,  0,  1, -2),
           (2, -3,  2,  1,  6, -1,  2,  2,  0,  2, -2),
           (2,  0,  2,  1,  6, -1,  3,  2,  0,  1, -2),
           (2, -1,  1,  0,  6, -1,  1,  0,  0,  0,  0)
           ]

## Fourth table in Simpson 1983
table_4 = [(2, -3, -1, -1,  2,  1,  1,  1,  1, -2, -2),
           (1, -2,  0, -1,  3,  1,  1,  1,  1, -2, -1),
           (6, -1, -1, -1,  6,  3,  0,  1,  1, -2, -1),
           (5, -1,  0, -1,  7,  2,  0,  1,  1, -2, -1),
           (1, -1,  0,  0,  3,  1,  0,  0,  0,  0,  0),
           (2,  0,  1, -1,  4,  0,  1,  1,  0,  1, -1),
           (4, -1,  1,  1,  6,  1,  2,  2,  0,  1, -2),
           (3,  0, -1, -1,  5,  0,  0,  1,  0,  1, -1),
           (3,  1, -1, -1,  7,  1,  0,  1,  0,  1, -1),
           (1, -1, -1, -1,  5, -1,  1,  1,  0,  1, -2),
           (2, -3,  0,  1,  6, -1,  1,  2,  0,  2, -1),
           (2,  0,  2,  1,  6, -1,  2,  2,  0,  1, -2),
           (2, -1,  1,  0,  6, -1,  0,  0,  0,  0,  0),
           (2, -1,  0,  0,  6,  1,  0,  0,  0,  0,  0),
           (4,  0,  0,  0,  8,  0,  0,  0,  0,  0,  0)
           ]

## First table under Theorem 2 in Bermond 1976
table_5 = [(2,  0,  1, -1,  2,  2,  2,  1,  1, -1,  0),
           (1,  1, -1, -1,  3,  1,  3,  1,  1, -1,  0),
           (0,  2, -2, -1,  4,  0,  4,  1,  0,  1, -2),
           (2,  1,  1,  0,  4,  1,  3,  0,  0,  0,  0),
           (0,  1, -1, -1,  4,  1,  4,  1,  0,  1, -2),
           (1,  1,  0,  0,  5,  1,  4,  0,  0,  0,  0),
           (2,  2,  1, -1,  6,  0,  6,  1,  0,  1, -1),
           (2,  1,  0, -1,  6,  1,  6,  1,  0,  1, -2),
           (6,  0,  5, -1,  6,  2,  5,  1,  1, -1,  0),
           (5,  1,  3, -1,  7,  1,  6,  1,  1, -1,  0)
           ]

## Second table under Theorem 2 in Bermond 1976
table_6 = [(2,  0,  0, -1,  2,  2,  0,  1,  1, -1,  0),
           (1,  1, -2, -1,  3,  1,  1,  1,  1, -1,  0),
           (0,  2, -3, -1,  4,  0,  2,  1,  0,  1, -2),
           (2,  1,  0,  0,  4,  1,  1,  0,  0,  0,  0),
           (0,  1, -2, -1,  4,  1,  2,  1,  0,  1, -3),
           (1,  1, -1,  0,  5,  1,  1,  0,  0,  0,  0),
           (2,  2, -1, -1,  6,  0,  3,  1,  0,  1, -2),
           (2,  1, -1, -1,  6,  1,  2,  1,  0,  1, -2),
           (6,  0,  2, -1,  6,  2,  1,  1,  1, -1,  0),
           (5,  1,  0, -1,  7,  1,  2,  1,  1, -1,  0),
           ]

def davies_configuration_1(m):
    lenslet_configurations = []
    offset_start = 1
    offset_convention = +1
    def add_line(davies_baseline, offset_start):
        A = offset_start
        B = offset_start + davies_baseline + offset_convention
        lenslet_configurations.append((A, B))
        offset_start += 1
        return offset_start
    for j in range(m-1):
        offset_start = add_line(4*m-4 - 2*j, offset_start)
    offset_start = add_line(4*m-2, offset_start)
    for j in range(m-1):
        offset_start = add_line(2*m-3 - 2*j, offset_start)
    offset_start = add_line(4*m-1, offset_start)
    offset_start += m-1
    offset_start += m-1
    offset_start = add_line(4*m, offset_start)
    for j in range(m-1):
        offset_start = add_line(4*m-3 - 2*j, offset_start)
    offset_start += 1
    for j in range(m-1):
        offset_start = add_line(2*m-2 - 2*j, offset_start)
    offset_start = add_line(2*m-1, offset_start)
    offset_start += m-1
    offset_start += m-1
    offset_start += 1
    offset_start += 1
    return lenslet_configurations

def davies_configuration_2(m):
    lenslet_configurations = []
    offset_start = 1
    offset_convention = +1
    def add_line(davies_baseline, offset_start):
        A = offset_start
        B = offset_start + davies_baseline + offset_convention
        lenslet_configurations.append((A, B))
        offset_start += 1
        return offset_start
    for j in range(m-1):
        offset_start = add_line(4*m-4 - 2*j, offset_start)
    offset_start = add_line(4*m-2, offset_start)
    for j in range(m-1):
        offset_start = add_line(2*m-3 - 2*j, offset_start)
    offset_start = add_line(4*m-1, offset_start)
    offset_start += m-1
    offset_start += m-1
    offset_start = add_line(2*m-1, offset_start)
    for j in range(m-1):
        offset_start = add_line(4*m-3 - 2*j, offset_start)
    offset_start += 1
    for j in range(m-1):
        offset_start = add_line(2*m-2 - 2*j, offset_start)
    offset_start += m-1
    offset_start += m-1
    offset_start += 1
    offset_start += 1
    return lenslet_configurations

def output_configuration(table, t, s):
    lenslet_configurations = []
    for line in table:
        a, b, c, d, e, f, g, h, i, k, l = line
        j_max = i*t + k*s + l
        if j_max >= 0:
            for j in range(int(j_max)+1):
                A = a*t + b*s + c + d*j
                B = e*t + f*s + g + h*j
                lenslet_configurations.append((A, B))
    return lenslet_configurations

def lenslet_configuration(d, m):
    # d: first measured baseline
    # m: number of baselines/frequencies measured
    if m >= 2*d-1: # if first condition is verified, then continue
        mod_m = m % 4
        mod_d = d % 4
        if d == 1:
            if mod_m == 0:
                t = m//4
                return output_configuration(table_skolem_1, t, 0)
            if mod_m == 1:
                t = m//4
                return output_configuration(table_skolem_2, t, 0)
            else:
                print(f"There is no Skolem solution for m={m}.")
        if d == 2:
            if mod_m == 0:
                t = m//4
                return davies_configuration_1(t)
            elif mod_m == 3:
                t = (m+1)//4
                return davies_configuration_2(t)
            else:
                print("Condition 2 not satisfied.")
        if d > 2:
            if d % 2 == 0:
                if mod_m == 0:
                    if mod_d == 0:
                        # Tableau 1
                        # print("Tableau 1")
                        t = m//4
                        s = d//4
                        return output_configuration(table_1, t, s)
                    elif mod_d == 2:
                        # Tableau 2
                        # print("Tableau 2")
                        t = m//4
                        s = (d-2)//4
                        return output_configuration(table_2, t, s)
                elif mod_m == 3:
                    # Tableau 5
                    #print("Tableau 5")
                    t = (m-3)//4
                    s = d//2
                    return output_configuration(table_5, t, s)
                else:
                    print("Condition 2 not satisfied.")
                    raise
            else:
                if mod_m == 0:
                    if mod_d == 1:
                        # Tableau 4
                        # print("Tableau 4")
                        t = m//4
                        s = (d-1)//4
                        return output_configuration(table_4, t, s)
                    if mod_d == 3:
                        # Tableau 3
                        # print("Tableau 3")
                        t = m//4
                        s = (d+1)//4
                        return output_configuration(table_3, t, s)
                elif mod_m == 1:
                    # Tableau 6
                    # print("Tableau 6")
                    t = (m-1)//4
                    s = (d+1)//2
                    return output_configuration(table_6, t, s)
                else:
                    print("Condition 2 not satisfied.")
                    raise
    else:
        print("Condition 1 not satisfied.")
        raise

def verification(d, m):
    supposed_baselines = [i for i in range(d, d + m)]
    supposed_pupils = [i for i in range(1, 2*m+1)]
    constructed_lenslet_pairs = lenslet_configuration(d, m)
    constructed_baselines = [abs(b-a) for a, b in constructed_lenslet_pairs]
    constructed_baselines.sort()
    pupil_list = []
    for a, b in constructed_lenslet_pairs:
        pupil_list.append(a)
        pupil_list.append(b)
    pupil_list.sort()
    print(constructed_baselines)
    return (pupil_list == supposed_pupils) and (constructed_baselines == supposed_baselines)

if __name__ == "__main__":
    ## Test for a Skolem set with first baseline at d=1 and m=8 frequencies
    ## For m = 4k
    d = 1
    m = 8
    print(lenslet_configuration(d=d, m=m), verification(d=d, m=m))


    ## Test for a Skolem set with first baseline at d=1 and m=9 frequencies
    ## For m = 4k+1
    d = 1
    m = 9
    print(lenslet_configuration(d=d, m=m), verification(d=d, m=m))


    ## Test for a Langford set with first baseline at d=2 and m=8 frequencies
    ## For m = 4k
    d = 2
    m = 8
    print(lenslet_configuration(d=d, m=m), verification(d=d, m=m))


    ## Test for a Langford set with first baseline at d=2 and m=7 frequencies
    ## For m = 4k+3
    d = 2
    m = 7
    print(lenslet_configuration(d=d, m=m), verification(d=d, m=m))




