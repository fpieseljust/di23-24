# Metodologia TDD a la funció factorial
Desenvolupa la funció factorial mitjançant la metodologia TDD.

Recorda les regles:

- **Regla 1**: Primer el test, després la codificació.
- **Regla 2**: Afegeix el mínim codi per superar el test
- **Regla 3**: No hauríeu de tindre més d'un test no superat a la vegada
- **Regla 4**: Escriu codi que passe el test, després refactoritza el codi.
- **Regla 5**: Un test hauria de fallar la primera vegada que ho escrius, en cas contrari pregunta't per què ho afegeixes.
- **Regla 6**: mai refactoritzar sense tests.

Hauria d'incloure almenys les següents proves:

- El factorial d'1 és 1
- Llança una excepció TypeError en no rebre un enter
- Llança una excepció ValueError en rebre un enter negatiu
- El factorial de 5 és 120