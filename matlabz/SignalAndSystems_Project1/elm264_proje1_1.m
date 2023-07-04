n=-45:1:45;
eq=-(0.05 + 0.3j);
y=exp(eq*n);

subplot(2,2,1);
stem(n,real(y))
title('Reel kısım');
xlabel('n');

subplot(2,2,2);
stem(n,imag(y));
title('imajiner kısım');
xlabel('n');

subplot(2,2,3);
stem(n,abs(y));
title('Genlik Grafiği');
xlabel('n');

subplot(2,2,4); 
stem(n,(180/pi)*angle(y)); title('Faz'); xlabel('n')