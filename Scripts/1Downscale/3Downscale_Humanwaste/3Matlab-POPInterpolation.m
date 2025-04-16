path=="./Data/POP/Clip_to_trend_extent/"
year1=2000
year2=2010
year=year1:1:year2
interval=1/(year2-year1)
num=size(1:interval:2)

[A1, R1]= readgeoraster(strcat(path,"pop_m3_",int2str(year1),"_5070_clipped.tif"));
info=geotiffinfo(strcat(path,"pop_m3_",int2str(year1),"_5070_clipped.tif"));
dim=size(A1);

[A2, R2]= readgeoraster(strcat(path,"pop_m3_",int2str(year2),"_5070_clipped.tif"));


A1_re=reshape(A1,[dim(1)*dim(2),1]);
A2_re=reshape(A2,[dim(1)*dim(2),1]);
A_cat=NaN(dim(1)*dim(2),2);

A_cat(:,1)=A1_re;
A_cat(:,2)=A2_re;

[X,Y] = meshgrid(1:2, 1:dim(1)*dim(2));
[Xq,Yq] = meshgrid(1:interval:2, 1:dim(1)*dim(2));
A_cat = interp2(X,Y,A_cat,Xq,Yq);


l_array=ones(num(2),2);
for i=1:num(2)
    disp(year(i));
    v=reshape(A_cat(:,i),dim(1),dim(2));
    v(idxnan_A2) = NaN;
    m=mean(mean(v,'omitnan'),'omitnan');
    l_array(i,2)=m;
    l_array(i,1)=year(i);
    disp(m);
    save_path=strcat("./Data/POP/interpolated_anaul_pop/pop_",int2str(year(i)),".tif");
    geotiffwrite(save_path, v, R1,'GeoKeyDirectoryTag',info.GeoTIFFTags.GeoKeyDirectoryTag);

end
