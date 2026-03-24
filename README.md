# cod-battleship
### Juego hundir la flota colaboratibo en clase

#### Version completa:
~~~mermaid
sequenceDiagram
    actor Jugador
    participant J as Juego
    participant T as Tablero
    participant C as Casilla [x][y]
    participant N as Nave

    Jugador->>J: Selecciona opción "2" en menu()
    activate J
    
    J->>J: lanzar_ataque()
    Jugador-->>J: Introduce coordenadas x, y (input)
    
    J-->>Jugador: print("Ataque en (x,y)")
    J->>T: comprobar_impacto(x, y)
    activate T
    
    T-->>Jugador: print("Impacto en (x,y)")
    T->>C: disparar()
    activate C
    
    alt visitada == True
        C-->>Jugador: print("Ya disparaste aquí")
        C-->>T: return None
    else visitada == False
        C->>C: visitada = True
        
        alt nave is None
            C-->>Jugador: print("Agua")
            C-->>T: return 0
        else nave asignada
            C->>N: recibir_disparo()
            activate N
            
            alt hundido == True
                N-->>C: return 2 (HUNDIDO)
            else hundido == False
                N->>N: vida -= 1
                
                alt vida <= 0
                    N->>N: vida = 0
                    N->>N: hundido = True
                    N-->>Jugador: print("{nombre} hundido")
                    N-->>C: return 2 (HUNDIDO)
                else vida > 0
                    N-->>Jugador: print("{nombre} tocado. Vida restante: {vida}")
                    N-->>C: return 1 (TOCADO)
                end
            end
            deactivate N
            
            C-->>T: return resultado
        end
    end
    deactivate C
    
    T-->>J: return resultado
    deactivate T
    
    J->>J: mostrar_resultado(resultado)
    J-->>Jugador: print("Agua / Tocado / Hundido / Ya disparaste aquí")
    deactivate J
~~~

#### Version simple:
~~~mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Juego as :Juego
    participant Tablero as :Tablero
    participant Casilla as :Casilla
    participant Nave as :Nave

    Usuario->>Juego: lanzar_ataque(x, y)
    activate Juego

    Juego->>Tablero: comprobar_impacto(x, y)
    activate Tablero

    Tablero->>Casilla: disparar()
    activate Casilla

    alt visitada == True
        Casilla-->>Tablero: return None
    else visitada == False
        Casilla->>Nave: recibir_disparo()
        activate Nave
        Nave-->>Casilla: return TOCADO / HUNDIDO
        deactivate Nave
        Casilla-->>Tablero: return resultado
    end

    deactivate Casilla

    Tablero-->>Juego: return resultado
    deactivate Tablero

    Juego->>Juego: mostrar_resultado(resultado)
    Juego-->>Usuario: imprime resultado
    deactivate Juego
~~~