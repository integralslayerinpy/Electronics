n = 0:99; %n değerleri ayrık zaman için
x = (0.8).^n .* (n >= 0); % istenilen x[n] sinyali

N = length(x); % Sinyal uzunluğu range 

% Öteleme miktarı
otelenme_miktari = 5;

x_otelenmis = zeros(1, N); % Ötelenmiş sinyal

% Öteleme işlemi
x_otelenmis(n - otelenme_miktari + 1) = x;

FF = fftshift(fft(x_otelenmis)); % Fourier dönüşümü

genlik = abs(FF); % Genlik hesabı
faz = angle(FF); % Faz hesabı

frek = linspace(-pi, pi, N); % Frekans vektörü Tanımlama işlemi

% Genlik grafiği
subplot(2, 1, 1);%figure için
stem(frek, genlik);%ayrık veri çizimi,discreet-plot
xlabel('Frekans (radyan)');%eksen adlandırma
ylabel('Genlik'); %eksen adlandırma
title('x[n-5] Fourier Dönüşümü Genlik Grafiği');%başlık

% Faz grafiği
subplot(2, 1, 2); %figure için
stem(frek, faz);%ayrık veri çizimi,discreet-plot
xlabel('Frekans (radyan)');%eksen adlandırma
ylabel('Faz (radyan)');%eksen adlandırma
title('x[n-5] Fourier Dönüşümü Faz Grafiği');%başlık
