var
  a: integer;
begin
  writeln('Введите число от 0 до 9:');
  readln(a);
  if a = 0 then
    writeln('ноль')
  else if a = 1 then
    writeln('один')
  else if a = 2 then
    writeln('два')
  else if a = 3 then
    writeln('три')
  else if a = 4 then
    writeln('четыре')
  else if a = 5 then
    writeln('пять')
  else if a = 6 then
    writeln('шесть')
  else if a = 7 then
    writeln('семь')
  else if a = 8 then
    writeln('восемь')
  else if a = 9 then
    writeln('девять')
  else
    writeln('Число за пределами диапазона');

  readln;
end.
