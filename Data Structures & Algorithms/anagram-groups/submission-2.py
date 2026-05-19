class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        saida = []
        listaTest = []
        #organizar as letras das strings em ordem alfabética
        for i in range(len(strs)):
            letrasOrd = sorted(strs[i])
            listaTest.append([letrasOrd, strs[i]])

        #organizar as strings em ordem alfabética
        listaTest.sort()    

        cont = 0
        for i in range(len(listaTest)):
            if i == 0:
                saida.append([])
                saida[cont].append(listaTest[i][1])
            elif listaTest[i][0] == listaTest[i-1][0]:
                saida[cont].append(listaTest[i][1])
            else:
                cont += 1
                saida.append([])
                saida[cont].append(listaTest[i][1])

        return saida;