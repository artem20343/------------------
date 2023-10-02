var
y,x,g: integer;
begin
writeln('Введите целое число');
readln(x);
if x<=2 then y:=x;
if x>=3 then y:=2 else y:=-x+5;
writeln( 'Ответ:',y);
end.
