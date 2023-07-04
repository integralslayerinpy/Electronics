t1 = linspace(-2, 2, 1000);
t2= linspace(-1, 2, 1000);
t3= linspace(-2, 1, 1000);

xfirst = (t2>=-1 & t2<0).*(t2+1) + (t2>=0 & t2<2)*1 + (t2==2)*0;
xsecond = (t3>-2 & t3<0).*(1) + (t3>=0 & t3<=1).*(-t3+1) + (t3==-2)*0;
x_1 = (t1>=-1 & t1<0).*(t1+1) + (t1>=0 & t1<2)*1 + (t1==2)*0;
x_2 = (t1>-2 & t1<0).*(1) + (t1>=0 & t1<=1).*(-t1+1) + (t1==-2)*0;

subplot(2,2,1);
plot(t1, xfirst,'LineWidth',2);
title('x(t) grafiği');
xlabel('t'); ylabel('x(t)');
grid on;

subplot(2,2,2);
plot(t1, xsecond, 'LineWidth',2);
title('x(-t) grafiği') 
xlabel('t'); ylabel('x(-t)');
grid on;

subplot(2,2,3);
plot(t1, (x_1+x_2)/2,'LineWidth',2);
title('çift denklem grafiği') 
xlabel('t');
grid on;

subplot(2,2,4);
plot(t1,(x_1-x_2)/2,'LineWidth',2);
title('tek denklem grafiği');xlabel('t');
grid on;