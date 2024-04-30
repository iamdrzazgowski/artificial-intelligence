mezczyzna(stanislaw_kowal).
mezczyzna(roman_kowal).
mezczyzna(stanislaw_kowalski).
mezczyzna(jan_kowal).
mezczyzna(wojciech_mokrogorski).
mezczyzna(arkadiusz_tkacz).
mezczyzna(krzysztof_kowal).
mezczyzna(lech_kowalski).
mezczyzna(sebastian_tkacz).
mezczyzna(pawel_kowal).
mezczyzna(grzegorz_kowalski).
mezczyzna(marek_kowalski).
mezczyzna(brajan_tkacz).

rodzic(stanislaw_kowal,roman_kowal).
rodzic(stanislaw_kowal,jan_kowal).
rodzic(zofia_kowal,roman_kowal).
rodzic(genowefa_kowal,jan_kowal).
rodzic(genowefa_kowal,wojciech_mokrogorski).
rodzic(roman_kowal,maria_tkacz).
rodzic(roman_kowal,krzysztof_kowal).
rodzic(bozena_kowal,maria_tkacz).
rodzic(bozena_kowal,krzysztof_kowal).
rodzic(stanislaw_kowalski, dorota_kowal).
rodzic(stanislaw_kowalski, lech_kowalski).
rodzic(zofia_kowalska, dorota_kowal).
rodzic(zofia_kowalska, lech_kowalski).
rodzic(zofia_kowalska, irena_zieba).
rodzic(arkadiusz_tkacz, sebastian_tkacz).
rodzic(maria_tkacz, sebastian_tkacz).
rodzic(krzysztof_kowal, pawel_kowal).
rodzic(dorota_kowal, pawel_kowal).
rodzic(lech_kowalski, grzegorz_kowalski).
rodzic(lech_kowalski, marek_kowalski).
rodzic(danuta_kowalska, grzegorz_kowalski).
rodzic(danuta_kowalska, marek_kowalski).
rodzic(irena_zieba, julia_zieba).
rodzic(dzesika_tkacz, brajan_tkacz).
rodzic(sebastian_tkacz, brajan_tkacz).

malzenstwo(stanislaw_kowal, zofia_kowal).
malzenstwo(stanislaw_kowal, genowefa_kowal).
malzenstwo(roman_kowal, bozena_kowal).
malzenstwo(stanislaw_kowalski, zofia_kowalska).
malzenstwo(arkadiusz_tkacz, maria_tkacz).
malzenstwo(krzysztof_kowal, dorota_kowal).
malzenstwo(lech_kowalski, danuta_kowalska).
malzenstwo(sebastian_tkacz, dzesika_tkacz).

kobieta(X) :-
    not(mezczyzna(X)).

ojciec(X,Y) :-
    mezczyzna(X),
    rodzic(X,Y).

matka(X,Y) :-
    kobieta(X),
    rodzic(X,Y).

corka(X,Y) :-
    kobieta(X),
    rodzic(Y,X).

brat_rodzony(X,Y) :-
    mezczyzna(X),
    rodzic(Z,X),
    rodzic(Z,Y),
    X \= Y.

brat_przyrodni(X,Y) :-
    mezczyzna(X),
    rodzic(A,X),
    rodzic(B,Y),
    malzenstwo(A, B),
    X \= Y.

kuzyn(X, Y) :-
    mezczyzna(X),
    rodzic(A, X),
    rodzic(B, Y),
    rodzic(C, A),
    rodzic(C, B),
    A \= B,
    X \= Y.

kuzynka(X, Y) :-
    kobieta(X),
    rodzic(A, X),
    rodzic(B, Y),
    rodzic(C, A),
    rodzic(C, B),
    A \= B,
    X \= Y.

dziadek_od_strony_ojca(X, Y) :-
    mezczyzna(X),
    rodzic(X,Z),
    mezczyzna(Z),
    rodzic(Z,Y).

dziadek_od_strony_matki(X, Y) :-
    mezczyzna(X),
    rodzic(X,Z),
    kobieta(Z),
    rodzic(Z,Y).

dziadek(X,Y) :-
    mezczyzna(X),
    rodzic(X, Z),
    rodzic(Z, Y).

babcia(X,Y) :-
    kobieta(X),
    rodzic(X, Z),
    rodzic(Z,Y).

babcia_od_strony_ojca(X,Y) :-
    kobieta(X),
    rodzic(X,Z),
    mezczyzna(Z),
    rodzic(Z,Y).

babcia_od_strony_matki(X,Y) :-
    kobieta(X),
    rodzic(X,Z),
    kobieta(Z),
    rodzic(Z,Y).

pradziadek(X,Y) :-
    mezczyzna(X),
    rodzic(X,A),
    rodzic(A,B),
    rodzic(B,Y).

prababka(X,Y) :-
    kobieta(X),
    rodzic(X,A),
    rodzic(A,B),
    rodzic(B,Y).

wnuczek(X,Y) :-
    mezczyzna(X),
    rodzic(Y,Z),
    rodzic(Z,X).

wnuczka(X,Y) :-
    kobieta(X),
    rodzic(Y,Z),
    rodzic(Z,X).

przodek(X, Y) :-
    rodzic(X, Y).
przodek(X, Y) :-
    rodzic(X, Z),
    przodek(Z, Y).

potomek(X, Y) :-
    rodzic(Y, X).
potomek(X, Y) :-
    rodzic(Y, Z),
    potomek(X, Z).

macocha(X,Y) :-
    kobieta(X),
    malzenstwo(Z,X),
    rodzic(Z,Y),
    not(matka(X,Y)).

ojczym(X,Y) :-
    mezczyzna(X),
    malzenstwo(X, Z),
    rodzic(Z,Y),
    not(ojciec(X,Y)).

pasierb(X,Y) :-
    mezczyzna(X),
    rodzic(Z,X),
    (   malzenstwo(Z, Y);
    malzenstwo(Y,Z)),
    (   not(ojciec(Y,X));
    not(matka(Y,X))).

pasierbica(X,Y) :-
    kobieta(X),
    rodzic(Z,X),
    (   malzenstwo(Z, Y);
    malzenstwo(Y,Z)),
    (   not(ojciec(Y,X));
    not(matka(Y,X))).

wujek(X,Y) :-
    mezczyzna(X),
    rodzic(Z,Y),
    rodzic(A,Z),
    rodzic(A,X),
    X \= Z. 

ciocia(X,Y) :-
    kobieta(X),
    rodzic(Z,Y),
    rodzic(A,Z),
    rodzic(A,X),
    X \= Z.

stryj(X,Y) :-
    mezczyzna(X),
    rodzic(Z,Y),
    rodzic(A,Z),
    rodzic(A,X),
    mezczyzna(Z),
    X \= Z,
    not(malzenstwo(X, _)).

stryjenka(X, Y) :-
    kobieta(X),
    rodzic(Z,Y),
    mezczyzna(Z),
    rodzic(A, Z),
    rodzic(A, B),
    mezczyzna(B),
    Z \= B,
    malzenstwo(B, Y).

szwagier(X, Y) :-
    mezczyzna(X),
    rodzic(A, Y),
    rodzic(A, Z),
    Y \= Z,
    kobieta(Z),
    malzenstwo(X,Z).

szwagierka(X, Y) :-
    kobieta(X),
    rodzic(A, Y),
    rodzic(A, Z),
    Y \= Z,
    mezczyzna(Z),
    malzenstwo(Z,X).

bratowa(X,Y) :-
    kobieta(X),
    malzenstwo(Z, X),
    rodzic(A, Z),
    rodzic(A, Y),
    mezczyzna(Z),
    Y \= Z.

ziec(X, Y) :-
    mezczyzna(X),
    malzenstwo(X, Z),
    kobieta(Z),
    rodzic(Y, Z).

synowa(X,Y) :-
    kobieta(X),
    malzenstwo(Z, X),
    mezczyzna(Z),
    rodzic(Y, Z).

krewny(X, Y) :- 
    przodek(X, Y); 
    kuzyn(X, Y);
    kuzynka(X, Y);
    wujek(X, Y);
    ciocia(X, Y);
    stryj(X, Y);
    stryjenka(X, Y);
    pasierb(X, Y);
    pasierbica(X, Y).