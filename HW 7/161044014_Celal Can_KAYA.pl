male(celalcan).
male(kadir).
male(emre).
male(necati).
male(celal).
male(oktay).
male(kenan).
female(aynur).
female(tuğba).
female(sevgi).
female(emine).
female(müşerref).
female(hanife).
female(latife).
female(bakiye).

parent(müşerref,kadir).
parent(müşerref,kenan).
parent(müşerref,latife).
parent(müşerref,bakiye).
parent(celal,kadir).
parent(celal,kenan).
parent(celal,latife).
parent(celal,bakiye).
parent(hanife,aynur).
parent(hanife,sevgi).
parent(hanife,emine).
parent(hanife,oktay).
parent(necati,aynur).
parent(necati,sevgi).
parent(necati,emine).
parent(necati,oktay).
parent(aynur,celalcan).
parent(aynur,emre).
parent(aynur,tuğba).
parent(kadir,celalcan).
parent(kadir,emre).
parent(kadir,tuğba).

child(kadir,müşerref).
child(kadir,celal).
child(kenan,müşerref).
child(kenan,celal).
child(latife,müşerref).
child(latife,celal).
child(bakiye,müşerref).
child(bakiye,celal).
child(aynur,hanife).
child(aynur,necati).
child(sevgi,hanife).
child(sevgi,necati).
child(emine,hanife).
child(emine,necati).
child(oktay,hanife).
child(oktay,necati).
child(celalcan,aynur).
child(celalcan,kadir).
child(emre,aynur).
child(emre,kadir).
child(tuğba,aynur).
child(tuğba,kadir).

sibling(kadir,kenan).
sibling(kenan,kadir).
sibling(kadir,latife).
sibling(latife,kadir).
sibling(kadir,bakiye).
sibling(bakiye,kadir).
sibling(kenan,latife).
sibling(latife,kenan).
sibling(kenan,bakiye).
sibling(bakiye,kenan).
sibling(latife,bakiye).
sibling(bakiye,latife).
sibling(aynur,sevgi).
sibling(sevgi,aynur).
sibling(aynur,emine).
sibling(emine,aynur).
sibling(aynur,oktay).
sibling(oktay,aynur).
sibling(sevgi,emine).
sibling(emine,sevgi).
sibling(sevgi,oktay).
sibling(oktay,sevgi).
sibling(emine,oktay).
sibling(oktay,emine).
sibling(celalcan,tuğba).
sibling(tuğba,celalcan).
sibling(celalcan,emre).
sibling(emre,celalcan).
sibling(emre,tuğba).
sibling(tuğba,emre).

mother(X,Y) :- female(X),parent(X,Y).
father(X,Y) :- male(X),parent(X,Y).
brother(X,Y) :- male(X),sibling(X,Y).
sister(X,Y) :- female(X),sibling(X,Y).
daughter(X,Y) :- female(X),child(X,Y).
son(X,Y) :- male(X),child(X,Y).
grandmother(X,Y) :- child(Y,Z), child(Z,X).
aunt(X,Y) :- female(X),sibling(X,Z),parent(Z,Y).