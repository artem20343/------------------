var
  i, num: integer;
  root: real;
begin
  i := 1;
  while i <= 10 do
  begin
    write('Введите число: ');
    readln(num);
    if num < 0 then
    begin
      writeln('Число отрицательное. Продолжаем дальше.');
      continue; 
    end;
    if num = 0 then
    begin
      writeln('Вы ввели ноль. Программа завершена.');
      break;
    end;
    root := sqrt(num);
    writeln('Квадратный корень числа ', num, ' = ', root:0:2);
    i := i + 1;
  end;
  readln;
end.