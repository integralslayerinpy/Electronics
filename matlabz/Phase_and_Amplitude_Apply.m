f = -1000:1:1000;
xsurekli = ((1j*cos(8*pi*f))./(pi*f))+((1j*sin(4*pi*f)) ./ ((2*pi*f).^2));

subplot(2,1,1);
plot(f,abs(xsurekli));
title('Genlik');
xlabel('f');

subplot(2,1,2);
plot(f,(180/pi)*angle(xsurekli));
title('Faz');
xlabel('f');
