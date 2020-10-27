# https://www.vivaxsolutions.com/web/lmc.aspx
# Fibonacci sequence
INP
STA x
INP
STA y
INP
STA   lmt
LDA x
OUT
LDA y
OUT
loop    LDA lmt
BRZ end
SUB one
STA lmt
LDA x
ADD y
STA z
OUT
LDA y
STA x
LDA z
STA y
BRA loop
end   LDA z
SUB z
HLT
x    DAT
y    DAT
z    DAT
lmt   DAT
one   DAT 1 