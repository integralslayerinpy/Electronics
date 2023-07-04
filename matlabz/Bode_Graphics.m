% Devre Parametreleri
R = 500;  % Direnç (ohm)

% Frekans aralığı
f = logspace(1, 6, 100);   % 10 ile 10^6 arasında 100 adet logaritmik frekans değeri

% Genlik hesaplama
Vout = @(f) R;  % Sadece dirence bağlı olduğu için Vout değeri R olacaktır

% Genlik ve Frekans Bode Grafiği
figure;
subplot(2, 1, 1);
semilogx(f, 20*log10(Vout(f)));
xlabel('Frekans (Hz)');
ylabel('Genlik (dB)');
title('Genlik Bode Grafiği (Sadece Direnç)');

subplot(2, 1, 2);
semilogx(f, log10(f));
xlabel('Frekans (Hz)');
ylabel('Log(Frekans)');
title('Frekans Bode Grafiği');