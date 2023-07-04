n = 0:99; % n değerleri ayrık zamanlı tanımlamak için oluşturuldu
x = (0.8).^n .* (n >= 0); % istenilen x[n] sinyali tanımı

N = length(x); % Sinyal uzunluğu range tanımı

FF = fftshift(fft(x)); % Fourier dönüşümü fonksiyonu tanımlandı 

genlik = abs(FF); % Genlik hesabı
faz = (180/pi).*angle(FF); % Faz hesabı

frek = linspace(-pi, pi, N); % Frekans vektörü tanımlama işlemi bu vektör belli bir aralık oluşturmak için tanımlandı

% Genlik grafiği
subplot(2, 1, 1); %aynı sayfada çoklu grafik için tanımlandı
stem(frek, genlik); %ayrık veri çizimi,discreet-plot
xlabel('Frekans (radyan)');%x ekseni adlandırma
ylabel('Genlik');%y ekseni adlandırma
title('x[n] Fourier Dönüşümü Genlik Grafiği');%başlık ekler

% Faz grafiği
subplot(2, 1, 2);%aynı sayfada çoklu grafik için tanımlandı
stem(frek, faz); %ayrık veri çizimi,discreet-plot işlevi için tanımlandı
xlabel('Frekans (radyan)'); % x eksenini isimlendirir.
ylabel('Faz (radyan)');%y eksenini adlandırmak için kullanıldı
title('x[n] Fourier Dönüşümü Faz Grafiği');%başlık eklendi
