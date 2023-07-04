t = linspace(-1, 2, 1000); % t zaman aralığı parçalama işlemi
x = zeros(size(t)); % atama gerçekleşebilecek 0'lar matrisi
% Verilen grafik parçalı fonksiyon olarak tanımlandı.
x(t > -4 & t < -2) = -1;
x(t >= -2 & t <= 2) = t(t >= -2 & t <= 2) / 2;
x(t > 2 & t < 4) = 1;

Fex = 1 / (t(2) - t(1)); % Örnekleme frekansı tanımı, sinyal hızı
N = length(x); % Sinyal uzunluğu gönderilecek parçayı temsil eder
frek = linspace(-Fex/2, Fex/2, N); % Frekans vektörü, iki frekans arası nokta sayısı için tanımlandı

FF = ifftshift(fft(x)); % Fourier dönüşümünü kaydırarak yapın

genlik = abs(FF); % Genlik için fonksiyon
faz = angle(FF) * (180/pi); % Faz açısı için fonksiyon, dereceye dönüştürüldü

% Genlik grafiği için
subplot(2, 1, 1);
plot(frek, genlik);
xlabel('Frekans ekseni (Hz)');
ylabel('Genlik ekseni');
title('x(t) Fourier Dönüşümü Genlik Grafiği');
xlim([-10, 10]); % x ekseni sınırları
ylim([0, 1.2]); % y ekseni sınırları

% Faz grafiği için
subplot(2, 1, 2);
plot(frek, faz);
xlabel('Frekans ekseni (Hz)');
ylabel('Faz (derece)');
title('x(t) Fourier Dönüşümü Faz Grafiği');
xlim([-10, 10]); % x ekseni sınırları
ylim([-200, 200]); % y ekseni sınırları

