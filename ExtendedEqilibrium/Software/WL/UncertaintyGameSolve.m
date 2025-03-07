(* ::Package:: *)

(* :Title: UncertaintyGameSolve.m *)

(* :Author: Jozsef Konczer *)

(* :Summary: Solves Games with Uncertainty *)

(* :Package version: 1.0 *)

(* :Mathematica version: 13.0 *)

(* :History: Last update Marhc 2, 2025 *)


BeginPackage["UncertaintyGames`"];


MinimalUncertaintyGameSolve;


Begin["`Private`"];


(** *** ***** ******* *********** ************* *****************

						MinimalUncertaintyGameSolve

	Comments: Symbolic calculation of probabilities
	ToDo:		

***************** ************* *********** ******* ***** *** **)


ClearAll[MinimalUncertaintyGameSolve, iMinimalUncertaintyGameSolve]


Options[MinimalUncertaintyGameSolve] = {
	"Method" -> "Symbolic"
	};


MinimalUncertaintyGameSolve[arg___, opts : OptionsPattern[MinimalUncertaintyGameSolve]]:=Block[
{res},

res = iMinimalUncertaintyGameSolve[arg, OptionValue["Method"]];
   If[FreeQ[res, $Failed],
    res
    ,  
     Message[MinimalUncertaintyGameSolve::notdef];
    res
     ]
    ]


(* Original FunctionF1 *)
iMinimalUncertaintyGameSolve[\[LeftAngleBracket]U1_List,U2_List\[RightAngleBracket],"Symbolic"]:=Module[
{p,q,P,Q,u1e,u2e,u1m,u2m,R1,R2,r1e,r2e},
u1e=Sum[U1[[ii]][[i,j]]{p,1-p}[[i]]{q,1-q}[[j]]{P,1-P}[[ii]],{i,1,2},{j,1,2},{ii,1,2}];
u2e=Sum[U2[[jj]][[i,j]]{p,1-p}[[i]]{q,1-q}[[j]]{Q,1-Q}[[jj]],{i,1,2},{j,1,2},{jj,1,2}];
u1m=Max[u1e/.{p->{1,0}}];
u2m=Max[u2e/.{q->{1,0}}];
R1=Table[Table[(u1m-u1e),{P,{1,0}}],{p,{1,0}}];
R2=Table[Table[(u2m-u2e),{Q,{1,0}}],{q,{1,0}}];

r1e=Sum[R1[[i,j]]{p,1-p}[[i]]{P,1-P}[[j]],{i,1,2},{j,1,2}];
r2e=Sum[R2[[i,j]]{q,1-q}[[i]]{Q,1-Q}[[j]],{i,1,2},{j,1,2}];


Simplify[Solve[{u1e>=(u1e/.p->1),u1e>=(u1e/.p->0),u2e>=(u2e/.q->1),u2e>=(u2e/.q->0),r1e>=(r1e/.P->1),r1e>=(r1e/.P->0),r2e>=(r2e/.Q->1),r2e>=(r2e/.Q->0),0<=p<=1,0<=q<=1,0<=P<=1,0<=Q<=1},{p,q,P,Q}],{0<=p<=1,0<=q<=1,0<=P<=1,0<=Q<=1}]/.{p->"p",q->"q",P->"P",Q->"Q"}
]/;Dimensions[U1]=={2,2,2}&&Dimensions[U2]=={2,2,2}


iMinimalUncertaintyGameSolve[___] := $Failed


MinimalUncertaintyGameSolve::notdef = "MinimalUncertaintyGameSolve has no value associated with the specified argument(s).";


End[];


EndPackage[];
