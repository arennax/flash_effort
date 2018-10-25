all([
	[cart/de8, cart/flash, cart/de2],
	[cart/flash, abe0, cart/de8],
	[cart/de8, cart/de2, cart/flash],
	[cart/nsga2, cart/flash],
	[cart/nsga2],
	[cart/de8, cart/de2, cart/flash],
	[cart/flash],
	[cart/de2, cart/de8, abe0, cart0],
	[atlm, cart/de2, cart/de8, cart/flash, cart0],
	[cart/de8, cart/de2],
	[cart/moead, abe0, cart/flash],
	[cart/flash, cart/denew, atlm, cart/de8, cart/de2, lp4ee],
	[cart/flash, cart/denew],
	[cart/moead, cart/flash, abe0],
	[cart/flash, cart/denew, lp4ee, cart/de2, cart/de8],
	[cart/flash, cart/moead, cart/denew],
	[cart/moead, atlm, abe0],
	[lp4ee, atlm, cart/denew, cart/de2, cart/de8] ]).

count(L0,G) :- flatten(L0,L1), sort(L1,L2), group(L2,1,G).

group([H],    N, [N/H]  ) :- !.
group([H,H|T],M, Out      ) :- !, N is M+1, group([H|T],N,Out).
group([H|T],  M, [M/H|Out]) :-              group(T,1,Out).

unique(X,Y) :- unique(X,Y,[]).

unique([],[],_).
unique([H|T],[H|Out], Seen) :- \+ member(H,Seen), !, unique(T,Out,[H|Seen]).
unique([_|T],X,Seen) :- unique(T,X,Seen).


x(X) :- all(L), member(Y,L), member(X,Y). % atomic(X).

xs(Xs) :- setof(X,x(X),Xs).

ones(L) :- setof([X],ones1(X),L).
twos(L) :- setof(Z,X^Y^(twos1(X,Y),sort([X,Y],Z)),L).
threes(L) :- setof(Z,W^X^Y^(threes1(W,X,Y),sort([W,X,Y],Z)), L).

ones1(X)       :- xs(L), member(X,L).
twos1(X,Y)     :- xs(L),  member(X,L), member(Y,L), X \= Y.
threes1(X,Y,Z) :- twos1(X,Y), ones1(Z), Z \= X, Z\=Y.

finds3(L) :- setof(N/X, L^(threes(L), member(X,L), works(X,N)), L).
finds2(L) :- setof(N/X, L^(twos(L),   member(X,L), works(X,N)), L).
finds1(L) :- setof(N/X, L^(ones(L),   member(X,L), works(X,N)), L).

works(X,N) :- all(All),  works(All,X,0,N0), N is N0.

works([],    _,  N, N).
works([One|All], X, N0, N) :-
  member(Y,X),
  member(Y,One)
  ->  works(All,X,1+N0,N) | works(All,X,N0,N).


printl(X) :- nl,forall(member(Y,X),(print(Y),nl)).
:- finds1(L),printl(L).
:- finds2(L),printl(L).
:- finds3(L),printl(L).
