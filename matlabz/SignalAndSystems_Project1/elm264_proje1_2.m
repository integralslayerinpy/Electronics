t=linspace(-45,45,1000);
eq=-(0.05 + 0.3j);
y=exp(eq*t);

subplot(2,2,1);
plot(t,real(y))
title('Reel kısım');
xlabel('t');

subplot(2,2,2);
plot(t,imag(y));
title('imajiner kısım');
xlabel('t');

subplot(2,2,3);
plot(t,abs(y));
title('Genlik Grafiği');
xlabel('t');

subplot(2,2,4); 
plot(t,(180/pi)*angle(y)); title('Faz'); xlabel('t')