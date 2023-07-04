t = linspace(-1, 2, 1000);
x = (t>=-1 & t<0).*(t+1) + (t>=0 & t<2)*1 + (t==2)*0;

subplot(2,2,1);
plot(t, x, 'LineWidth', 2);
grid on;
title('x(t)');
xlabel('t');
ylabel('x(t)');

subplot(2,2,2);
plot(t/2, x, 'LineWidth', 2);
grid on;
title('x(2t)');
xlabel('t') ; 
ylabel('x(2t)');

subplot(2,2,3);
plot(t+5/2, x, 'LineWidth', 2);
grid on;
title('x(t-5/2)');
xlabel('t') ; 
ylabel('x(t-5/2)');

subplot(2,2,4);
plot((t/-2 -5), x, 'LineWidth', 2);
grid on;
title('x(-2t+5)');
xlabel('t') ; 
ylabel('x(-2t+5)');