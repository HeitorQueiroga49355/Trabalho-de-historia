Algoritmo "Quest�o 13"
// Disciplina  : FLA
// Professor   : Raphael Muniz
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Heitor Queiroga Duarte
// Data atual  : 19/08/2020
Var
   n: vetor [1..3] de inteiro
   i: inteiro
Inicio
   para i de 1 ate 2 faca
      escreva("Digite o ", i, "� n�mero: ")
      leia(n[i])
   fimpara
   n[3] <- n[1]
   n[1] <- n[2]
   n[2] <- n[3]
   escreval("1� n�mero: ", n[1])
   escreval("2� n�mero: ", n[2])
Fimalgoritmo