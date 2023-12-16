import random
 
gene = ['01101','11000','01000','10011']

def selection(gene):
    x = [int(x,2) for x in gene]
    fx = [int(x)*int(x) for x in x]
    fx_sum = sum(fx)
    fx_avg = fx_sum//len(fx)
    excepted_count = [round((i/fx_avg),4) for i in fx]
    actual_count = [round(i) for i in excepted_count]
    mate_pool = []
    for i,j in zip(actual_count,gene):
        if i:
            for c in range(i):
                mate_pool.append(j)
    return x,fx, fx_sum,fx_avg,excepted_count,actual_count,mate_pool

x,fx, fx_sum,fx_avg,excepted_count,actual_count,mate_pool=selection(gene)
#print(mate_pool)

def crossover(mate_pool):
    remaining_pool = mate_pool.copy()
    parent1 = random.choice(remaining_pool)
    remaining_pool.remove(parent1)
    parent2 = random.choice(remaining_pool)
    remaining_pool.remove(parent2)
    parent3 = random.choice(remaining_pool)
    remaining_pool.remove(parent3)
    parent4 = random.choice(remaining_pool)
    
    crossoverpoint1 = random.randint(1, len(parent1)-1)
    crossoverpoint2 = random.randint(1, len(parent1)-1)
    crossover_points=[crossoverpoint1,crossoverpoint1,crossoverpoint2,crossoverpoint2]

    child1 = parent1[:crossoverpoint1] + parent2[crossoverpoint1:]
    child2 = parent2[:crossoverpoint1] + parent1[crossoverpoint1:]
    child3 = parent3[:crossoverpoint2] + parent4[crossoverpoint2:]
    child4 = parent4[:crossoverpoint2] + parent3[crossoverpoint2:]
    new_poplu=[child1,child2,child3,child4]

    x = [int(x,2) for x in new_poplu]
    fx = [int(x)*int(x) for x in x]
    return new_poplu,crossover_points,x,fx,mate_pool

#new_popu=crossover(mate_pool)
#print("New population after crossover:\n", new_popu)

def GA(gene,iter,n):
    if iter == 0:
        return
    
    x,fx, fx_sum,fx_avg,excepted_count,actual_count,mate_pool = selection(gene)
    if sum(actual_count)!=len(gene):
        print("Error dont know what to do at this situation ")
        return 
    print(f"\n------------------------------------------------- GENERATION {n} --------------------------------------------------")
    print("Initial Population\tX Value\t\tFitness Value( f(x) )\tProbability(Expected Count)\tActual Count")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{gene[i]}\t\t\t{x[i]}\t\t{fx[i]}\t\t\t{excepted_count[i]}\t\t\t\t{actual_count[i]}")

    new_poplu,crossover_points,x,fx,mate_pool= crossover(mate_pool)
    

    print(f"\n----------------------------------------------- New Population {n} ------------------------------------------------")
    print("Mate Pool\t\tCrossover Points\tNew Population\t\tx value\t\tf(x)")
    print(f"-----------------------------------------------------------------------------------------------------------------")
    for i in range(len(gene)):
        print(f"{mate_pool[i]}\t\t{crossover_points[i]}\t\t\t{new_poplu[i]}\t\t\t{x[i]}\t\t{fx[i]}")
    GA(new_poplu,iter-1,n+1)
GA(gene,3,0)
