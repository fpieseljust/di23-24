# Proves unitàries amb `pytest`

## Part 1 - definició de proves

Donat el codi de la classe [cartera.py](code/cartera/cartera.py), defineix unes proves unitàries per provar-la. 

```python
class SaldoInsuficiente(Exception):
    pass

class Cartera(object):

    def __init__(self, saldo_inicial=0):
        self.saldo = 0

    def gastar(self, cantidad):
        if self.saldo < cantidad:
            raise SaldoInsuficiente(
                'No tienes dinero suficiente. Saldo actual: {}'.format(cantidad))
        self.saldo -= cantidad

    def ingresar(self, cantidad):
        self.saldo += cantidad
```

Els test han de cobrir almenys els aspectes següents:

- Comprovar que el saldo inicial per defecte és 0
- Comprovar que el saldo inicial s'assigna correctament en cas de ser un enter positiu
- Comprovar que en ingressar diners, ens torna la suma del saldo anterior més l'ingrés
- Comprovar que en gastar diners, el saldo és la resta del saldo anterior i la quantitat treta
- Comprovar que ens salta una excepció en gastar més del saldo disponible

## Part 2 - refactorització

Refactoritza el codi de `cartera.py` perquè en cas de rebre un saldo negatiu, el saldo s'assigne a 0. Fes el seu test corresponent per comprovar que passa el nou test i la resta continua passant-los (prova de regressió).

- Comprovar que si passem al constructor un saldo negatiu, ens posarà a 0 el saldo
