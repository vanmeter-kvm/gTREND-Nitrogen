path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/250m_human_waste_n/"
yearl=1930:2010;

[A1, R1]= readgeoraster(strcat(path,"pop_N_",int2str(1930),"_250m.tif"));
info=geotiffinfo("G:/My Drive/Downscaled_Trend_N/Lvst_LayersPullets_Agriculture_LU/LayersPullets_1930.tif");
dim=size(A1);

[A2, R2]= readgeoraster("G:/My Drive/Downscaled_Trend_N/Lvst_LayersPullets_Agriculture_LU/LayersPullets_1930.tif");

x = R1.XWorldLimits(1):250:R1.XWorldLimits(2);
y = R1.YWorldLimits(1):250:R1.YWorldLimits(2);
[X1,Y1] = meshgrid(x,y);

x = R2.XWorldLimits(1):250:R2.XWorldLimits(2);
y = R2.YWorldLimits(1):250:R2.YWorldLimits(2);
[X2,Y2] = meshgrid(x,y);

idx_A1 = A1 >=0;
X1_v=X1(idx_A1);
Y1_v=Y1(idx_A1);

% 
% idx_A2 = A2 ==  NaN; 
% idxnan_A2 = A2 ==  NaN;
% 
% 
% %%%%Figure out NAN%%%%
% idxnan_A1 = A1 ==  NaN; 
% disp(sum(sum(idxnan_A1)))
% idx_A1 = A1 <  NaN;
% disp(sum(sum(idx_A1)))
% idxnan_A2 =  A2 ==  NaN; 
% disp(sum(sum(idxnan_A2)))
% idx_A2= A2 <  NaN;
% disp(sum(sum(idx_A2 )))
% 
% idx1= (idxnan_A1 & idx_A2);
% disp(sum(sum(idx1)))
% idx2= (idx_A1 & idxnan_A2) ;
% disp(sum(sum(idx2)))
% idx3=(idx_A1 & idx_A2);
% disp(sum(sum(idx3)))
% idx4=(idxnan_A1& idxnan_A2);
% disp(sum(sum(idx4)))