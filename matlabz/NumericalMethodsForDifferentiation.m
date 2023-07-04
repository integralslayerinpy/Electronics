v= linspace(0,2*pi,360);

h= 2*pi/360;

f_main= (((abs(cos(3*v/4))).^8 + (abs(sin(3.*v/4))).^8)).^-0.25;

fileri= (((abs(cos(3*(v+h)/4))).^8 + (abs(sin(3*(v+h)/4))).^8)).^-0.25;

fgeri= (((abs(cos(3*(v-h)/4))).^8 + (abs(sin(3*(v-h)/4))).^8)).^-0.25;

fson= (((abs(cos(3*(v+2*h)/4))).^8 + (abs(sin(3*(v+2*h)/4))).^8)).^-0.25;

fara= (((abs(cos(3*(v-h)/4))).^8 + (abs(sin(3*(v-h)/4))).^8)).^-0.25;

ileri= (fileri-f_main)/h;
geri= (fgeri-f_main)/h;
son= (1/2*h)*((-3*f_main) + (4*fileri) - (fson));
ara= (1/2*h)*(fileri - fara);

x_ara= ara.*cos(v) - f_main.*sin(v);
y_ara= ara.*sin(v) + f_main.*cos(v);

L_ara= (x_ara.^2 + y_ara.^2).^0.5;

l_xara= (x_ara/L_ara);
l_yara= (y_ara/L_ara);

x_son= son.*cos(v) - f_main.*sin(v);
y_son= son.*sin(v) + f_main.*cos(v);

L_son= (x_son.^2 + y_son.^2).^0.5;

l_xson= (x_son/L_son);
l_yson= (y_son/L_son);

x_ileri= ileri.*cos(v) -f_main.*sin(v);
y_ileri= ileri.*sin(v) +f_main.*cos(v);

L_ileri= (x_ileri.^2 + y_ileri.^2).^0.5;

lxileri= (x_ileri/L_ileri);
lyileri= (y_ileri/L_ileri);

x_geri= geri.*cos(v) -f_main.*sin(v);
y_geri= geri.*sin(v) +f_main.*cos(v);

Lgeri= (x_geri.^2 + y_geri.^2).^0.5;

lxgeri= (x_geri/Lgeri);
lygeri= (y_geri/Lgeri);

polarplot(v,ara)
title('3 nokta ara nokta: g(Φ)')