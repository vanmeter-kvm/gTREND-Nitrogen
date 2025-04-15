path="./Data/POP/interpolated_anaul_pop/"
yearl=1930:1:2010;

for year=yearl
    [A1, R1]= readgeoraster(strcat(path,"pop_",int2str(year),".tif"));
    info=geotiffinfo(strcat(path,"pop_",int2str(year),".tif"));
    A=A1*5/100;
    save_path=strcat("./Data/POP/human_waste_n/pop_N_",int2str(year),".tif");
    geotiffwrite(save_path, A, R1,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);
end