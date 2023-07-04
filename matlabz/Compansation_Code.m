gf = 0.70:0.01:1;
aralik= linspace(-Inf, Inf, numel(gf));

P = 35010;
V=230;
Qc = P * (tan(acos(gf)) - tan(acos(1)));
Vforcalc = 230 * 230;
W0 = 2 * pi * 50;
C = Qc / (Vforcalc * W0);
Sold = P ./ gf;

akim = Sold ./ 230;


akim = repmat(akim, numel(aralik), 1);

figure(1);
surf(gf, C, akim);
xlabel('pf');
ylabel('C');
zlabel('akim');
title('Kompanzasyon Çizim')