function f(x: real): real;
begin
    f := sin(x - 0.5) - 2*x + 0.5;
end;
function HalfDivisionMethod(a, b, eps: real): real;
var
    x, c: real;
begin
    repeat
        c := (a + b) / 2;
        if f(c) = 0 then
            break;
        if f(a) * f(c) < 0 then
            b := c
        else
            a := c;
    until abs(b - a) < eps;
    x := (a + b) / 2;
    HalfDivisionMethod := x;
end;
var
    a, b, eps, x: real;
begin
    writeln('Введите интервал [a, b]:');
    readln(a, b);
    writeln('Введите допуск:');
    readln(eps);
    
    x := HalfDivisionMethod(a, b, eps);
    
    writeln('Решение:', x:0:6);
end.