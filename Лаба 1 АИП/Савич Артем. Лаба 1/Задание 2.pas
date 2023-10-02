Program example1;
var
  a, b, c, d, sum: real;
  ln, fn, mn, gn: string;
begin
  writeln('Введите вашу фамилию:');
  readln(ln);

  writeln('Введите ваше имя:');
  readln(fn);

  writeln('Введите ваше отчество:');
  readln(mn);

  writeln('Введите номер вашей группы:');
  readln(gn);

  writeln('Введите четыре числа через пробел:');
  readln(a, b, c, d);

  sum := a + b + c + d;

  writeln('Фамилия: ', ln);
  writeln('Имя: ', fn);
  writeln('Отчество: ', mn);
  writeln('Номер группы: ', gn);
  writeln('Сумма четырех чисел равна: ', sum);

  writeln('Нажмите Enter');
  readln;
end.

