t = linspace(-1, 2, 1000); %integral ve grafiklerde kullanılmak üzere zaman aralığı parçalama işlemi
x = zeros(size(t)); %atama gerçekleşebilecek ve her bir değer aralığı için 0 matrisi atandı
% Verilen grafik parçalı fonksiyon olarak tanımlandı.
x(t > -4 & t < -2) = -1;
x(t >= -2 & t <= 2) = t(t >= -2 & t <= 2) / 2;
x(t > 2 & t < 4) = 1;

Fs = 1 / (t(2) - t(1));  % Örnekleme frekansı, step-by-step frekans aralığını temsil eder.
N = length(x);  % işaret uzunluğu tanımlandı.
frek = linspace(-Fs/2, Fs/2, N);  % Frekans vektörü oluşturuldu burada Fex ve N kullanıldı.
%frek ile tanımlanan bu yapı linspace ile seçilen frekans aralığı küçük parçalara bölünür

FF = fftshift(fft(x)); %fourier transform fonksiyonu fft ile yapılır shift ile genliğe şekil verilir.

genlik = abs(FF); % Genlik için fonksiyon.
faz = (180/pi).*angle(FF); % Faz açısı için fonksiyon.

% Zamanda öteleme işlemi özelliğe bağlı kalınarak aşağıdaki gibi tanımlanmıştır.
zamandaOteleme = 5; % 5 saniye zamanda öteleme
yeni_x = x .* exp(1i * 2 * pi * frek * zamandaOteleme); % özellikten gelen üstel aktarım

Y = fftshift(fft(yeni_x)); %5 saniye dönüşüm sonrası öteleme sonrası fourier dönüşümü fftshift genlik scale için.

genlik_yeni = abs(Y); % Genlik için öteleme sonrası fonksiyon
faz_yeni = (180/pi).*angle(Y); % Faz açısı için öteleme sonrası fonksiyon

% Genlik grafiği
subplot(2, 1, 1); %aynı sayfada çok sayıda basım için özellik tanımlaması
plot(frek, genlik); %grafiği bastırır.
hold on; %grafik ekler
plot(frek, genlik_yeni);% öteleme sonrası grafik bastırma
xlabel('Frekans ekseni (Hz)');%x ekseni adlandırma
ylabel('Genlik');%y ekseni adlandırma
title('x(t) ve Öteleme Sonrası Fourier Dönüşümü Genlik Grafiği');% grafik başlığı adlandırma
legend('x(t)', 'Öteleme Sonrası');%hangi çizgi hangi grafiğe ait renk ekleme tanımı fonksiyonu

% Faz grafiği
subplot(2, 1, 2);%aynı sayfada çok sayıda basım için özellik tanımlaması
plot(frek, faz);%grafiği bastırır.
hold on; %grafik ekler
plot(frek, faz_yeni); % öteleme sonrası grafik bastırma
xlabel('Frekans ekseni (Hz)'); %x ekseni adlandırma
ylabel('Faz (radyan)');%y ekseni adlandırma
title('x(t) ve Öteleme Sonrası Fourier Dönüşümü Faz Grafiği'); %grafik başlığı adlandırma işlemi
legend('x(t)', 'Öteleme Sonrası'); %hangi çizgi hangi grafiğe ait adlandırma işlemi