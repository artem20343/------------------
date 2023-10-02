var
  n, i: integer;
  e, s, t, x, fact: real;
begin
  e := 0.00001; // Точность
  x := 23;
  n := 0; // Начальное значение счетчика итераций
  s := 0; // Обнуление суммы
  t := 1; // Значение первого члена ряда
  s := t; // Добавление к сумме первого члена ряда
  while abs(t) > e do
  begin
    n := n + 1;
    fact := 1;
    for i := 1 to 2 * n do
      fact := fact * i;
    t := power(-1, n) * power(x, 2 * n) / fact; // Нахождение члена ряда
    s := s + t;
  end;
  writeln(s);
end.