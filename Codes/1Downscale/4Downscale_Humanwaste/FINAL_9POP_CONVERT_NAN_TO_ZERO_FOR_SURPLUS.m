path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/250m_human_waste_n/";
% atm_path="G:/My Drive/Downscaled_Trend_N/Atmospheric_Deposition/Atmospheric_Oxidized/"
% agcrop_path="G:/My Drive/Downscaled_Trend_N/CropUptake_Agriculture_Agriculture_LU/"
% agfert_path="G:/My Drive/Downscaled_Trend_N/Fertilizer_Agriculture_Agirculture_LU/"
% defert_path="G:/My Drive/Downscaled_Trend_N/Fertilizer_Domestic_Domestic_LU/"
% agfixa_path="G:/My Drive/Downscaled_Trend_N/Fix_Agriculture_Agirculture_LU/"
% agbeef_path="G:/My Drive/Downscaled_Trend_N/Lvst_BeefCattle_Agriculture_LU/"
% agbroi_path="G:/My Drive/Downscaled_Trend_N/Lvst_Broilers_Agriculture_LU/"
% agdairy_path="G:/My Drive/Downscaled_Trend_N/Lvst_DairyCattle_Agriculture_LU/"
% agequine_path="G:/My Drive/Downscaled_Trend_N/Lvst_Equine_Agriculture_LU/"
% aghogs_path="G:/My Drive/Downscaled_Trend_N/Lvst_Hogs_Agriculture_LU/"
% aglayer_path="G:/My Drive/Downscaled_Trend_N/Lvst_LayersPullets_Agriculture_LU/"
% agotherc_path="G:/My Drive/Downscaled_Trend_N/Lvst_OtherCattle_Agriculture_LU/"
% agequine_path="G:/My Drive/Downscaled_Trend_N/Lvst_Equine_Agriculture_LU/"
% agsheep_path="G:/My Drive/Downscaled_Trend_N/Lvst_SheepGoat_Agriculture_LU/"
% agturkey_path="G:/My Drive/Downscaled_Trend_N/Lvst_SheepGoat_Agriculture_LU/"
% save_path="G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/human_waste_n_zero/";
% Year_l=1930:1:1931;

yearl=[1967,1972,1973]
for j=1:3
    year=yearl(j);
    [A1, R1]= readgeoraster(strcat(path,"pop_N_",int2str(year),"_250m.tif"));
    info=geotiffinfo(strcat(path,"pop_N_",int2str(year),"_250m.tif"));
    dim=size(A1);
    
    
    idx_A1 = isnan(A1);
    A1(idx_A1)=0;
    save_path=strcat("G:/My Drive/schang68@uic.edu 2022-01-16 10 58/Downscale_2021/Population/human_waste_n_zero/pop_fill0_",int2str(year),".tif");
    geotiffwrite(save_path, A1, R1,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
end