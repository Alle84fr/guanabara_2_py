# if - condição verdadeira                se
# sempre inicia com if, uma condição verdadeira
# elif - condições alinhada verdadeiras   se não
# else + if = elif
# else - se falsa                         do contrário

# aninha = ninho uma coisa dentro da outra



#|__________________________! ATENÇÃO !______________________________|
#|                                                                   |
#| TERMINAR COM ELSE NÃO É OBRIGATÓRIO, podendo ter apenas if e elif |
#|                                                                   |
#____________________________________________________________________|




# CONDIÇÕES ALINHADAS - CONDIÇÃO DENTRO DE CONDIÇÃO

nome= input("Digite seu nome: ")

#|___________________ CONDIÇÃO SIMPLES________________________|
#|                                                            |
#|Possui apenas o bloco da condição if, verdadeira            |

#OBS - FIZ SOZINHA ESTA PARTE, IREI REFAZER SEGUINDO O IN DADO PELO PROFESSOR
# if nome == "Andréia"or nome == "andréia": print("\n\033[92m Favor entrera em contato \033[m\n")

# SE ESTÁ  NESTA LISTA - IN
if nome in {"Andréia", "andréia"}: print("\n\033[92m Favor entrera em contato \033[m\n")

# aqui há apenas um bloco, se for verdade acontece um mensagem extra, caso contrário, o cód segue normal

#|=============================================================|



#|___________________ CONDIÇÃO COMPOSTA________________________|
#|                                                             |
#|Possui bloco da condição if, verdadeira                      |
#|                                                             |
#|Possui bloco da condição else, falsa                         |


if nome in {"Andréia", "andréia"}: print("\033[92m Somos xarás \033[m\n")
else:print("\n\033[95m Não somos xarás \033[m\n")


#|=============================================================|


#|___________________ CONDIÇÃO ANINHADA________________________|
#|                                                             |
#|Possui bloco da condição if, verdadeira                      |
#|                                                             |
#|Possui bloco da condição elif, verdadeira                      |
#|                                                             |
#|Possui bloco da condição else, falsa                         |


if nome in {"Andréia", "andréia"}: print("\033[92m Nome lindo né! \033[m")
elif nome in {"Andréias", "andréias"}: print("\033[96m Por causa de um s  \033[m")
elif nome in {"André", "andré"}: print("\033[96m Você é meu xará versão masculica \033[m")
else:print("\033[95m Seu nome é diferente do meu \033[m\n")


# Se tivermos o mesmo nome = print que somo xarás
# Se tivermos nome parecido, feminino, somos quase xarás
# Se tiver o equivalente masculino, somos xarás "invertido"
# Se for diferente não somos xarás

#|=============================================================|



#|           CONTINUAÇÃO DO CÓD FORA DO BLOCO                  |

print(f"\n\033[107m Bom dia, {nome}! \033[m\n")

