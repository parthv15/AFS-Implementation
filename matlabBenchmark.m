syms x a b c y; 
clc;

T = readtable('Book1.xlsx'); 
expr = table2array(T); 

len_expr = 1:length(expr);
expr_runTime = 1:length(expr); 

for i = 1 : length(expr)
   strExpr = string(expr(i)); 
   len_expr(i) = strExpr.strlength();    
   tic; 
   k = simplify(str2sym(strExpr));
   t = toc;
   expr_runTime(i) = 1000*t; 
end 

scatter(len_expr,expr_runTime,"blue","filled"); 
title("MATLAB Runtime Benchmark");
xlabel("Expression Length");
ylabel("Run Time");
ylim([10,100]);



