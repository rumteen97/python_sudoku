from pyevolve import *

table = []  # sudoku khali

for i in range(0, 81):
    table.append(0)  # jadval ba 0 por

# meghdar dehi avvlie
table[1] = 2
table[3] = 5
table[5] = 1
table[7] = 9
table[9] = 8
table[12] = 2
table[14] = 3
table[17] = 6
table[19] = 3
table[22] = 6
table[25] = 7
table[29] = 1
table[33] = 6
table[36] = 5
table[37] = 4
table[43] = 1
table[44] = 9
table[47] = 2
table[51] = 7
table[55] = 9
table[58] = 3
table[61] = 8
table[63] = 2
table[66] = 8
table[68] = 4
table[71] = 7
table[73] = 1
table[75] = 9
table[77] = 7
table[79] = 6
print("initial table: ")
print(table)


def row(su_table, r_num):  # sakhte satr ha

    row = []
    for index in range(9):
        row.append(su_table[r_num * 9 + index])
    return row


def column(su_table, col_num):  # sakhte sotun
    # returns column
    column = []
    for index in range(9):
        column.append(su_table[index * 9 + col_num])  # mesle row jaye im j avaz she
    return column


def block(su_table, blk_num):  # moraba 3*3
    block = []
    first = int(blk_num / 3) * 9 * 3 + (blk_num - int(blk_num / 3) * 3) * 3  # avline khune moraba
    for x in range(3):
        for y in range(3):
            block.append(su_table[first + x * 9 + y])
    return block


def fitness_func(su):  # tedad error kamtr bhtr ast
    # this is the fitness function. No errors means the solution
    err = 0  # khata
    for i in range(9):
        for element in [row(su, i), column(su, i), block(su, i)]:  # tedad error dar har satr,sotun,blok
            for g in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # chek krdn adade tekrari
                if (element.count(g)) > 1:
                    err += element.count(g) - 1  # tedad tekrar ra be kolle khata ha eafe mikone

    for i, g in enumerate(su):  # adad haii ke ba adad avl frgh darnd ra chek mikone,genetic taghir dade
        if g != table[i] and table[i] != 0:  # taghir krde va 0 nbaude
            err += 2  # gene khub nabud va bayd crom hazf shavad
    return err


genome = G1DList.G1DList(81)  # crom 81 khane i
genome.setParams(rangemin=1, rangemax=9)  # adad har khane 1 ta 9
genome.evaluator.set(fitness_func)  # har crom ra b tabe error mide fitness hsab mishe
genome.setParams(bestrawscore=0.00, rounddecimal=2)  # behtrin halat khata=0
ga = GSimpleGA.GSimpleGA(genome)  # tabe az ghabl tarif shode genetic
ga.setMinimax(Consts.minimaxType["minimize"])  # dar fitness kmtrin error khub ast
ga.setMutationRate(0.04)  # darsad mutation
ga.setGenerations(100)  # tedad nasl
ga.setPopulationSize(200)  # jamiat avvlie
ga.setCrossoverRate(1)
ga.setElitismReplacement(5)  # bedune taghir be nasle bad mire
ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)  # sharte khateme agar 0 bshe motvgh mishe
ga.evolve(freq_stats=10)

print (ga.bestIndividual())