Algoritmo "Cronômetro"
Var
   tt, segundo, minuto, hora: inteiro
Inicio
   tt <- 1
   segundo <- 0
   minuto <- 0
   Repita
      escreva(minuto, ": ", segundo)
      segundo <- segundo+1
      timer 1000
      timer 0
      limpatela
      escreva(minuto, ": ", segundo)
      limpatela
      se segundo=60 entao
      minuto <- minuto + 1
      segundo <- 0
      fimse
   ate tt>2
Fimalgoritmo