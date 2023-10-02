var
  n, i, sum: integer;
begin
  writeln('Введите количество членов ряда: ');
  readln(n);
  sum := 0;
  for i := 1 to n do
  begin
    sum := sum + i;
  end;
  writeln('Сумма первых ', n, ' членов ряда равна ', sum);
  readln;
end.


