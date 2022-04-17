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
    for i in range(9):
        row.append(su_table[r_num * 9 + i])
    return row


def column(su_table, col_num):  # sakhte sotun
    # returns column
    column = []
    for j in range(9):
        column.append(su_table[j * 9 + col_num])  # mesle row jaye im j avaz she
    return column


def block(su_table, blk_num):  # moraba 3*3
    block = []
    first = int(blk_num / 3) * 9 * 3 + (blk_num - int(blk_num / 3) * 3) * 3  # avline khune moraba
    for x in range(3):
        for y in range(3):
            block.append(su_table[first + x * 9 + y])
    return block


def fitness_func(su):  # tedad error kamtr bhtr ast
    err = 0  # khata
    for i in range(9):
        for element in [row(su, i), column(su, i), block(su, i)]:  # tedad error dar har satr,sotun,blok
            for g in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # chek krdn adade tekrari
                if (element.count(g)) > 1:
                    err += element.count(g) - 1  # tedad tekrar ra be kolle khata ha eafe mikone

    for i, g in enumerate(su):  # adad haii ke ba adad avl frgh darnd ra chek mikone,genetic taghir dade
        if g != table[i] and table[i] != 0:  # taghir krde va 0 nbaude
            err += 4  # gene khub nabud va bayd crom hazf shavad
    return err


crom = G1DList.G1DList(81)  # crom 81 khane i
crom.setParams(rangemin=1, rangemax=9)  # adad har khane 1 ta 9
crom.evaluator.set(fitness_func)  # har crom ra b tabe error mide fitness hsab mishe
crom.setParams(bestrawscore=0.00, rounddecimal=2)  # behtrin halat khata=0
gen = GSimpleGA.GSimpleGA(crom)  # tabe az ghabl tarif shode genetic
gen.setMinimax(Consts.minimaxType["minimize"])  # dar fitness kmtrin error khub ast
gen.setMutationRate(0.04)  # darsad mutation
gen.setGenerations(200)  # tedad nasl,tedad tekrar
gen.setPopulationSize(100)  # jamiat avvlie
gen.setElitismReplacement(3)  # gene nokhbe ke bedune taghir be nasle bad mire
gen.terminationCriteria.set(GSimpleGA.RawScoreCriteria)  # sharte khateme agar 0 bshe motvgh mishe
gen.evolve(freq_stats=8)        #shru e algorithm va har 10 ta ra nshan midahad
print (gen.bestIndividual())     #behtrin crom