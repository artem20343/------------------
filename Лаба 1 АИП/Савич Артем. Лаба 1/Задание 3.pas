var z:integer; r:real;
begin
  writeln('Введите число z ');
  readln(z);
  r:=1+(sqr(z)/3+sqr(z)/5)+arcsin(z/4);
  writeln('Результат вычислений функции при произвольно введенных данных = ',r);
end.