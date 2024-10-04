import pyomo.environ as pyEnv

def obj_func(model):
    return sum(model.x[i, j] * model.c[i, j] for i in model.N for j in model.N)

def rule_const1(model, j):
    return sum(model.x[i, j] for i in model.N if i != j) == 1

def rule_const2(model, i):
    return sum(model.x[i, j] for j in model.N if i != j) == 1

def rule_const3(model, i, j):
    n = len(model.N)  # Tamanho do conjunto de nós (número de cidades)
    if i != j and i > 1 and j > 1:
        return model.u[i] - model.u[j] + model.x[i, j] * n <= n - 1
    else:
        return pyEnv.Constraint.Skip
    
# Restrição de volume de carga
def rule_volume(model):
    return sum(model.volume[i] * sum(model.x[i, j] for j in model.N) for i in model.N) <= 15

def create_model(n, dist_matrix, total_volume):
    # Model
    model = pyEnv.ConcreteModel()

    # Indexes for the cities
    model.N = pyEnv.RangeSet(n)

    # Dummy variable u for subtour elimination (starts from city 2)
    model.u = pyEnv.Var(model.N, within=pyEnv.NonNegativeIntegers, bounds=(0, n - 1))

    # Decision variables xij
    model.x = pyEnv.Var(model.N, model.N, within=pyEnv.Binary)

    # Distance Matrix cij
    model.c = pyEnv.Param(model.N, model.N, initialize=lambda model, i, j: dist_matrix[i - 1][j - 1])

    # Volume
    model.volume = pyEnv.Param(model.N, initialize=lambda model, i: total_volume[i - 1])
    
    # Objective Function
    model.objective = pyEnv.Objective(rule=obj_func, sense=pyEnv.minimize)

    # Constraints
    model.const1 = pyEnv.Constraint(model.N, rule=rule_const1)
    model.const2 = pyEnv.Constraint(model.N, rule=rule_const2)
    model.rest3 = pyEnv.Constraint(model.N, model.N, rule=rule_const3)
    model.volume_constraint = pyEnv.Constraint(rule=rule_volume)

    # Solver
    solver = pyEnv.SolverFactory('glpk')
    result = solver.solve(model, tee=False)

    # Output results
    print(result)

    l = list(model.x.keys())
    for i in l:
        if model.x[i]() != 0:
            print(i, '--', model.x[i]())

