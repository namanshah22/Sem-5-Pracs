DATA SEGMENT
A DB 5
fact DB ?
DATA ENDS
CODE SEGMENT
         ASSUME DS:DATA,CS:CODE
START:
      MOV AX,DATA
      MOV DS,AX
      MOV AH,00
      MOV AL,A
 L1:  DEC A
      MUL A
      MOV CL,A
      CMP CL,01
      JNZ L1
      MOV fact, AL 
CODE ENDS
END START