t = linspace(-1, 2, 1000); %integral ve grafiklerde kullanılmak üzere zaman aralığı parçalama işlemi
x = zeros(size(t)); %atama gerçekleşebilecek ve her bir değer aralığı için 0 matrisi atandı

% Verilen grafik parçalı fonksiyon olarak tanımlandı.
x(t > -4 & t < -2) = -1;
x(t >= -2 & t <= 2) = t(t >= -2 & t <= 2) / 2;
x(t > 2 & t < 4) = 1;

Fex = 1 / (t(2) - t(1));  % Örnekleme frekansı, step-by-step frekans aralığını temsil eder.
N = length(x);  %işaret uzunluğu tanımlandı.
frek = linspace(-Fex/2, Fex/2, N);% Frekans vektörü oluşturuldu burada Fex ve N kullanıldı.
%frek ile tanımlanan bu yapı linspace ile seçilen frekans aralığı küçük parçalara bölünür

FF = fftshift(fft(x));%fourier transform fonksiyonu fft ile yapılır shift ile genliğe şekil verilir.

genlik = abs(FF);% Genlik için fonksiyon.
faz = (180/pi).*angle(FF); % Faz açısı için fonksiyon.

% Zaman ölçeklendirme
zaman_skali = 3; % 3 birim zaman ölçeklendirme (scale) işlemi özellik kullanılarak tasarlandı

t_olcekli = t / zaman_skali; % scale işlemi
x_olcekli = x; % scale edilen yeni sinyal

% Fourier dönüşümü (scale  sonrası)
FF_olcekli = fftshift(fft(x_olcekli));

genlik_olcekli = abs(FF_olcekli); % scale sonrası genlik
faz_olcekli = angle(FF_olcekli); % scale sonrası faz açısı
%karşılaştırma işlemleri için önce-sonra olarak 2 tane yapıldı

% Genlik grafiği
subplot(2, 1, 1);% aynı sayfada çoklu grafik için tanımlandı
plot(frek, genlik);%grafiği bastırır
hold on; %grafik ekler
plot(frek, genlik_olcekli); % scale edilen grafik batırma işlemi
xlabel('Frekans ekseni (Hz)');%x ekseni adlandırır
ylabel('Genlik');%y ekseni adlandırır
title('x(t) Fourier dönüşümü ve Zaman Ölçeklendirme Sonrası Genlik Grafiği');%başlık ekler
legend('x(t)', 'Ölçeklendirme Sonrası');%grafikleri ayrı ayrı  isimlendirir

% Faz grafiği
subplot(2, 1, 2);%aynı sayfada çolu grafik için tanımlandı
plot(frek, faz);%grafiği bastırır
hold on; %grafik ekler
plot(frek, faz_olcekli);%grafiği bastırır
xlabel('Frekans ekseni (Hz)');%x ekseni adlandırır
ylabel('Faz (radyan)');%y ekseni adlandırır
title('x(t) Fourier dönüşümü ve Zaman Ölçeklendirme Sonrası Faz Grafiği');%başlık ekler
legend('x(t)', 'Ölçeklendirme Sonrası');%grafikleri ayrı ayrı isimlendirir
