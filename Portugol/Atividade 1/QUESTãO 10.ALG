Algoritmo "Questão 10"
// Disciplina  : FLA
// Professor   : Raphael Muniz
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Heitor Queiroga Duarte
// Data atual  : 19/08/2020
Var
   n: vetor [1..4] de inteiro
   i: inteiro
Inicio
   para i de 1 ate 4 faca
      escreva("Digite um número: ")
      leia(n[i])
   fimpara
   para i de 4 ate 1 passo -1 faca
      escreva(n[i])
   fimpara
Fimalgoritmo