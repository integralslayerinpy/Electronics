n = 0:99; % ayrık n değerleri
x = (0.8).^n .* (n >= 0); % istenilen x[n] sinyali tanımı
x_ters = fliplr(x); % x[-n] sinyali için ters çevirme işlemi fonksiyon  ile tanımı bu işlem zamanda katlama ile yapıldı.

N = length(x_ters); % Sinyal uzunluğu tanımlama işlemi

FF = fftshift(fft(x_ters)); % Fourier dönüşümü fonksiyon ile tanımlandı

genlik = abs(FF); % Genlik hesabı
faz = (180/pi).*angle(FF); % Faz hesabı

frek = linspace(-pi, pi, N); % Frekans vektörü tanımlama işlemi bununla belirli bir aralık elde edildi.

% Genlik grafiği
subplot(2, 1, 1);%aynı sayfada çoklu grafik için tanımlandı
stem(frek, genlik);%ayrık veri çizimi,discreet-plot işelvi için tanımlandı
xlabel('Frekans (radyan)');%x ekseni adlandırma
ylabel('Genlik');%y ekseni adlandırma
title('x[-n] Fourier Dönüşümü Genlik Grafiği'); %başlık ekleme işlemi

% Faz grafiği
subplot(2, 1, 2);%aynı sayfada çoklu grafik için tanımlandı
stem(frek, faz);%ayrık veri çizimi,discreet-plot işelvi görür.
xlabel('Frekans (radyan)');%x ekseni adlandırma
ylabel('Faz (radyan)');%y ekseni adlandırma
title('x[-n] Fourier Dönüşümü Faz Grafiği'); %başlık eklendi
