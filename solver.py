import pyomo.environ as pyEnv

def obj_func(model):
    return sum(model.x[i,j] * model.c[i,j] for i in model.N for j in model.M)

def rule_const1(model, M):
    return sum(model.x[i, M] for i in model.N if i != M) == 1

def rule_const2(model, N):
    return sum(model.x[N, j] for j in model.M if j != N) == 1

def rule_const3(model, i, j):
    n = len(model.N)  # Tamanho do conjunto de nós (número de cidades)
    if i != j:
        return model.u[i] - model.u[j] + model.x[i,j] * n <= n-1
    else:
        return model.u[i] - model.u[i] == 0

def create_model(n, dist_matrix):
    #Model
    model = pyEnv.ConcreteModel()

    #Indexes for the cities
    model.M = pyEnv.RangeSet(n)                
    model.N = pyEnv.RangeSet(n)

    #Index for the dummy variable u
    model.U = pyEnv.RangeSet(2,n)
    
    #Decision variables xij
    model.x = pyEnv.Var(model.N,model.M, within=pyEnv.Binary)

    #Dummy variable ui
    model.u = pyEnv.Var(model.N, within=pyEnv.NonNegativeIntegers,bounds=(0,n-1))
    
    #Distance Matrix cij
    model.c = pyEnv.Param(model.N, model.M, initialize=lambda model, i, j: dist_matrix[i-1][j-1])
    
    model.objective = pyEnv.Objective(rule=obj_func,sense=pyEnv.minimize)

    model.const1 = pyEnv.Constraint(model.M,rule=rule_const1)
    
    model.rest2 = pyEnv.Constraint(model.N,rule=rule_const2)

    # Define the rest3 constraint correctly
    model.rest3 = pyEnv.Constraint(model.N, model.N, rule=rule_const3)
    
    model.pprint()
    
    #Solves
    solver = pyEnv.SolverFactory('glpk')
    result = solver.solve(model,tee = False)

    #Prints the results
    print(result)
    
    l = list(model.x.keys())
    for i in l:
        if model.x[i]() != 0:
            print(i,'--', model.x[i]())
