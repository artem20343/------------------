function CalculateSeries(x, e: Real): Real;
var
  n: Integer; // Начальное значение счетчика итераций
  s, t: Real; // Обнуление суммы и значения члена ряда
begin
  n := 0;
  s := 0;
  t := x;
  repeat
    n := n + 1;
    t := (-1)**n * (1 / (2*n + 1)) * x**(2*n-1); // Нахождение члена ряда
    s := s + t;
  until abs(t) <= e;
  
  CalculateSeries := s;
end;

var
  x, e, result: Real;
  num_terms: Integer;
begin
  x := -1.5;
  e := 0.5 * power(10, -4);
  
  result := CalculateSeries(x, e);
  
  writeln('Значение суммы: ', result);
  
  num_terms := Trunc(abs(result) / e) + 1;
  writeln('Число членов ряда: ', num_terms);
end.