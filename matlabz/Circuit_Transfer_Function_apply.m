R = 500;
L = 33*10^-3;
C = 47*10^-9;

f = logspace(1, 6, 1000);
w = 2*pi*f; 

s = 1i*w;

H = 1 ./ (1 + s*R*C + (s.^2)*(L*C));

subplot(2, 1, 1);
semilogx(f, 20*log10(abs(H)));
xlabel('Frekans (Hz)');
ylabel('Genlik (dB)');
title('Hacı Eren Karataş ');

subplot(2, 1, 2);
semilogx(f, angle(H)*180/pi);
xlabel('Frekans (Hz)');
ylabel('Faz (derece)');
title('Hacı Eren Karataş');