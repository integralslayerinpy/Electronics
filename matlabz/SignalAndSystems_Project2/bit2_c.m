n = 0:99;%n değerleri ayrık zamanlı tanımlamak için oluşturuldu
x = (0.8).^n .* (n >= 0); % istenilen x[n] sinyali tanımı

N = length(x);% Sinyal uzunluğu range tanımı

FF = fftshift(fft(x)); %Fourier dönüşümü fonksiyonu tanımlandı 

genlik = abs(FF); % Genlik hesabı
faz = (180/pi).*angle(FF); % Faz hesabı

frek = linspace(-pi, pi, N);% Frekans vektörü tanımlama işlemi bu vektör belli bir aralık oluşturmak için tanımlandı

% Türev işlemi özellik yardımı ile kullanıldı.
frek_turev = linspace(-pi, pi, N-1); %frekansta belirli aralıkta türev
genlik_turev = diff(genlik) ./ diff(frek); % genlik içintürev operatörü ataması
faz_turev = diff(faz) ./ diff(frek); % faz için türev operatörü ataması

% Genlik grafiği
subplot(2, 1, 1);%aynı sayfada çoklu grafik için tanımlandı
stem(frek_turev, genlik_turev);%ayrık veri çizimi,discreet-plot işelvi için tanımlandı
xlabel('Frekans (radyan)');%x ekseni adlandırma
ylabel('Türevli Genlik');%y ekseni adlandırma
title('x[n] Fourier Dönüşümü Türevli Genlik Grafiği');% başlık eklendi

% Faz grafiği
subplot(2, 1, 2);%aynı sayfada çoklu grafik için tanımlandı
stem(frek_turev, faz_turev);%ayrık veri çizimi,discreet-plot işelvi için tanımlandı
xlabel('Frekans (radyan)');%x ekseni adlandırma
ylabel('Türevli Faz (radyan)');%y ekseni adlandırma
title('x[n] Fourier Dönüşümü Türevli Faz Grafiği');%başlık eklendi

