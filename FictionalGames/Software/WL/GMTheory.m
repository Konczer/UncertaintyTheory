(* ::Package:: *)

(* :Title: GaussMatrices.m *)

(* :Author: Jozsef Konczer *)

(* :Summary: Numerical Functions to calculate the probability of
			domination of the first two rows in an Nn by Mm
			Random Gaussian matrix *)

(* :Package version: 1.0 *)

(* :Mathematica version: 13.0 *)

(* :History: Last update February 24, 2025 *)


BeginPackage["DominatingProbabilitiesForGaussianMatrices`"];


TwoRowDominatingProbability;
FunctionF1;
Functionf1;
Ipartial;


Begin["`Private`"];


(** *** ***** ******* *********** ************* *****************

						FunctionF1

	Comments: Numerical calculation of probabilities
	ToDo:		

***************** ************* *********** ******* ***** *** **)


ClearAll[FunctionF1, iFunctionF1]


Options[FunctionF1] = {
	"Method" -> "OriginalInfinite",
	"WorkingPrecision" -> 20
	};


FunctionF1[arg___, opts : OptionsPattern[FunctionF1]]:=Block[
{res},

res = iFunctionF1[arg, OptionValue["Method"],OptionValue["WorkingPrecision"]];
   If[FreeQ[res, $Failed],
    res
    ,  
     Message[FunctionF1::notdef];
    res
     ]
    ]


iFunctionF1[Nn_Integer,0,me_,WP_]:=1/(Nn-1)/;Nn>=2


iFunctionF1[Nn_Integer,1,me_,WP_]:=1/(Nn-1)/;Nn>=2


(* Original FunctionF1 *)
iFunctionF1[Nn_Integer,pp_,"OriginalInfinite",WP_]:=Module[
{},
NIntegrate[(2^(3/2 - Nn)*(1 + Erf[z/Sqrt[2]])^(-2 + Nn))/(E^(z^2/(2 + 4*(-1 + pp)*pp))*Sqrt[Pi + 2*Pi*(-1 + pp)*pp]),{z,-Infinity,Infinity},WorkingPrecision->WP]
]/;Nn>=2


(* Original FunctionF1 *)
iFunctionF1[Nn_Integer,pp_,"rTransform",WP_]:=Module[
{},
NIntegrate[(E^((2*(-1 + pp)*pp*InverseErf[-1 + 2*r]^2)/(1 - 2*pp + 2*pp^2))*r^(-2 + Nn))/Sqrt[1 - 2*pp + 2*pp^2],{r,0,1},WorkingPrecision->WP]
]/;Nn>=2


(* Original FunctionF1 *)
iFunctionF1[Nn_Integer,pp_?NumericQ,"PartsrMaxTransform",WP_]:=Module[
{},
1 - NIntegrate[(1 + Erf[InverseErf[-1 + 2*rm^(-2 + Nn)^(-1)]/Sqrt[1 - 2*pp + 2*pp^2]])/2,{rm,0,1},WorkingPrecision->WP]
]/;Nn>=2


iFunctionF1[___] := $Failed


FunctionF1::notdef = "FunctionF1 has no value associated with the specified argument(s).";


(** *** ***** ******* *********** ************* *****************

						Functionf1

	Comments: Numerical calculation of probabilities
	ToDo:		

***************** ************* *********** ******* ***** *** **)


ClearAll[Functionf1, iFunctionf1]


Options[FunctionF1] = {
	"Method" -> "OriginalInfinite",
	"WorkingPrecision" -> 20
	};


Functionf1[arg___, opts : OptionsPattern[FunctionF1]]:=Block[
{res},

res = iFunctionf1[arg, OptionValue["Method"],OptionValue["WorkingPrecision"]];
   If[FreeQ[res, $Failed],
    res
    ,  
     Message[FunctionF1::notdef];
    res
     ]
    ]


(* Original Functionf1 *)
iFunctionf1[Nn_Integer,pp_,"OriginalInfinite",WP_]:=Module[
{},
NIntegrate[
(2^(1 - Nn)*(1 + Erf[z/Sqrt[2]])^(-2 + Nn)*(-(z/(E^((z - 2*pp*z)^2/(2 + 4*(-1 + pp)*pp))*Pi*(1 + 2*(-1 + pp)*pp)^2)) - 
   ((-1 + 2*pp)*(1 + 2*(-1 + pp)*pp - z^2)*Erf[(z - 2*pp*z)/Sqrt[2 + 4*(-1 + pp)*pp]])/(Sqrt[2*Pi]*(1 + 2*(-1 + pp)*pp)^(5/2))))/E^(z^2/(2 + 4*(-1 + pp)*pp)),
   {z,-Infinity,Infinity},
   WorkingPrecision->WP]
]/;Nn>=2


(* Original Functionf1 *)
iFunctionf1[Nn_Integer,pp_,"rTransform",WP_]:=Module[
{},
NIntegrate[(E^((2*(-1 + pp)*pp*InverseErf[-1 + 2*r]^2)/(1 - 2*pp + 2*pp^2))*r^(-2 + Nn))/Sqrt[1 - 2*pp + 2*pp^2],{r,0,1},WorkingPrecision->WP]
]/;Nn>=2


(* Original Functionf1 *)
iFunctionf1[Nn_Integer,pp_?NumericQ,"PartsrTransform",WP_]:=Module[
{},
NIntegrate[(2^(2 - Nn)*(-2 + Nn)*(1 + Erf[Sqrt[1 - 2*pp + 2*pp^2]*InverseErf[-1 + 2*r]])^(-3 + Nn)*
  (-1 + E^((1 - 2*pp)^2*InverseErf[-1 + 2*r]^2)*Sqrt[Pi]*(-1 + 2*pp)*Erf[(1 - 2*pp)*InverseErf[-1 + 2*r]]*InverseErf[-1 + 2*r]))/
 (E^(2*(1 - 3*pp + 3*pp^2)*InverseErf[-1 + 2*r]^2)*Pi*Sqrt[1 - 2*pp + 2*pp^2]),
{r,0,1},WorkingPrecision->WP]
]/;Nn>=2


iFunctionf1[___] := $Failed


Functionf1::notdef = "Functionf1 has no value associated with the specified argument(s).";


(** *** ***** ******* *********** ************* *****************

						Ipartial

	Comments: Numerical calculation of probabilities
	ToDo:		

***************** ************* *********** ******* ***** *** **)


ClearAll[Ipartial, iIpartial]


Options[Ipartial] = {
	"Method" -> "OriginalInfinite",
	"WorkingPrecision" -> 20
	};


Ipartial[arg___, opts : OptionsPattern[Ipartial]]:=Block[
{res},

res = iIpartial[arg, OptionValue["Method"],OptionValue["WorkingPrecision"]];
   If[FreeQ[res, $Failed],
    res
    ,  
     Message[Ipartial::notdef];
    res
     ]
    ]


(* Original FunctionF1 *)
iIpartial[Nn_Integer,Mm_Integer,"OriginalInfinite",WP_]:=Module[
{iiF1,iif1},

iiF1[pp_?NumericQ]:=
1 - NIntegrate[(1 + Erf[InverseErf[-1 + 2*rm^(-2 + Nn)^(-1)]/Sqrt[1 - 2*pp + 2*pp^2]])/2,{rm,0,1},WorkingPrecision->WP];

iif1[pp_?NumericQ]:=
NIntegrate[(2^(2 - Nn)*(-2 + Nn)*(1 + Erf[Sqrt[1 - 2*pp + 2*pp^2]*InverseErf[-1 + 2*r]])^(-3 + Nn)*
  (-1 + E^((1 - 2*pp)^2*InverseErf[-1 + 2*r]^2)*Sqrt[Pi]*(-1 + 2*pp)*Erf[(1 - 2*pp)*InverseErf[-1 + 2*r]]*InverseErf[-1 + 2*r]))/
 (E^(2*(1 - 3*pp + 3*pp^2)*InverseErf[-1 + 2*r]^2)*Pi*Sqrt[1 - 2*pp + 2*pp^2]),
{r,0,1},WorkingPrecision->WP];

Mm NIntegrate[
iiF1[pp]^(Mm - 1)
iif1[pp],
 {pp, 0, 1},
 WorkingPrecision->WP
 ]
]/;Nn>=2&&Mm>=1


iIpartial[___] := $Failed


Ipartial::notdef = "Ipartial has no value associated with the specified argument(s).";


(** *** ***** ******* *********** ************* *****************

						Ipartial

	Comments: Numerical calculation of probabilities
	ToDo:		

***************** ************* *********** ******* ***** *** **)


ClearAll[TwoRowDominatingProbability, iTwoRowDominatingProbability]


Options[TwoRowDominatingProbability] = {
	"Method" -> "OriginalInfinite",
	"WorkingPrecision" -> 20
	};


TwoRowDominatingProbability[arg___, opts : OptionsPattern[TwoRowDominatingProbability]]:=Block[
{res},

res = iTwoRowDominatingProbability[arg, OptionValue["Method"],OptionValue["WorkingPrecision"]];
   If[FreeQ[res, $Failed],
    res
    ,  
     Message[TwoRowDominatingProbability::notdef];
    res
     ]
    ]


(* Original FunctionF1 *)
iTwoRowDominatingProbability[Nn_Integer,Mm_Integer,"OriginalInfinite",WP_]:=Module[
{},
1/(Nn-1)^Mm - Ipartial[Nn,Mm,"WorkingPrecision"->WP]
]/;Nn>=2&&Mm>=1


iTwoRowDominatingProbability[___] := $Failed


TwoRowDominatingProbability::notdef = "Ipartial has no value associated with the specified argument(s).";


End[];


EndPackage[];
