
R = 500;      
L = 33e-3;    
C = 47e-9;    

f = logspace(1, 6, 100);   

Z = @(f) R + 1i*(2*pi*f*L - 1./(2*pi*f*C));  
Vout = @(f) abs(1 ./ Z(f));                  

Phi = @(f) angle(1 ./ Z(f));                

figure;
subplot(2, 1, 1);
semilogx(f, 20*log10(Vout(f)));
xlabel('Frekans (Hz)');
ylabel('Genlik (dB)');
title('200102002009 Hacı Eren Karataş');

subplot(2, 1, 2);
semilogx(f, rad2deg(Phi(f)));
xlabel('Frekans (Hz)');
ylabel('Faz Açısı (derece)');
title('200102002009 Hacı Eren Karataş');