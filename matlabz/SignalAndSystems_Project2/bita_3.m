t = linspace(-1, 2, 1000); %t zaman aralığı parçalama işlemi
x = zeros(size(t)); %atama gerçekleşebilecek 0'lar matrisi

% Verilen grafik parçalı fonksiyon olarak tanımlandı.
x(t > -4 & t < -2) = -1;
x(t >= -2 & t <= 2) = t(t >= -2 & t <= 2) / 2;
x(t > 2 & t < 4) = 1;

Fex = 1 / (t(2) - t(1));  % Örnekleme frekansı tanımı, sinyal hızı
N = length(x);  % Sinyal uzunluğu gönderilecek parçayı temsil eder
frek = linspace(-Fex/2, Fex/2, N);  % Frekans vektörü, iki frekans arası nokta sayısı için tanımlandı

FF = fftshift(fft(x)); % Fourier dönüşümü fonksiyonu

genlik = abs(FF); % Genlik için fonksiyon.
faz = angle(FF); % Faz açısı için fonksiyon.

% Frekans öteleme
zamandaOteleme = 5; % 5 birim frekans öteleme

% Öteleme işlemi
frek_oteleme = frek + zamandaOteleme; % Öteleme sonrası frekans vektörü

% Öteleme sonrası Fourier dönüşümü
FF_oteleme = interp1(frek, FF, frek_oteleme, 'linear', 0); % Lineer interpolasyon

genlik_oteleme = abs(FF_oteleme); % Öteleme sonrası genlik
faz_oteleme = angle(FF_oteleme); % Öteleme sonrası faz açısı

% Genlik grafiği
subplot(2, 1, 1);
plot(frek_oteleme, genlik_oteleme);
xlabel('Frekans ekseni (Hz)');
ylabel('Genlik');
title('x(t) Fourier dönüşümü ve Frekans Öteleme Sonrası Genlik Grafiği');

% Faz grafiği
subplot(2, 1, 2);
plot(frek_oteleme, faz_oteleme);
xlabel('Frekans ekseni (Hz)');
ylabel('Faz (radyan)');
title('x(t) Fourier dönüşümü ve Frekans Öteleme Sonrası Faz Grafiği');
