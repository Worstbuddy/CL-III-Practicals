# -------- Fuzzy Set Operations --------

def fuzzy_union(A, B):
    return {x: max(A[x], B[x]) for x in A}

def fuzzy_intersection(A, B):
    return {x: min(A[x], B[x]) for x in A}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

def fuzzy_difference(A, B):
    return {x: min(A[x], 1 - B[x]) for x in A}

# -------- Fuzzy Relation (Cartesian Product) --------

def fuzzy_cartesian_product(A, B):
    R = {}
    for a in A:
        for b in B:
            R[(a, b)] = min(A[a], B[b])
    return R

# -------- Max–Min Composition --------

def max_min_composition(R, S, A_elements, B_elements, C_elements):
    T = {}
    for a in A_elements:
        for c in C_elements:
            values = []
            for b in B_elements:
                values.append(min(R[(a, b)], S[(b, c)]))
            T[(a, c)] = max(values)
    return T

# -------- Main Program --------

# Fuzzy sets
A = {'x1': 0.2, 'x2': 0.6, 'x3': 0.8}
B = {'x1': 0.5, 'x2': 0.4, 'x3': 0.9}

print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)

print("\nUnion:", fuzzy_union(A, B))
print("Intersection:", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))
print("Difference (A - B):", fuzzy_difference(A, B))

# -------- Relations --------

A_rel = {'a1': 0.6, 'a2': 0.8}
B_rel = {'b1': 0.5, 'b2': 0.7}
C_rel = {'c1': 0.4, 'c2': 0.9}

R = fuzzy_cartesian_product(A_rel, B_rel)
S = fuzzy_cartesian_product(B_rel, C_rel)

print("\nFuzzy Relation R (A × B):")
for k, v in R.items():
    print(k, ":", v)

print("\nFuzzy Relation S (B × C):")
for k, v in S.items():
    print(k, ":", v)

# -------- Max–Min Composition --------

T = max_min_composition(
    R, S,
    A_elements=['a1', 'a2'],
    B_elements=['b1', 'b2'],
    C_elements=['c1', 'c2']
)

print("\nMax–Min Composition (T):")
for k, v in T.items():
    print(k, ":", v)