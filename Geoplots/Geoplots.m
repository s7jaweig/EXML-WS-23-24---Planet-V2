clc, clear, close, dbstop if error;

buff = 0.5;
colors = ["#0072BD","#D95319","#EDB120","#7E2F8E","#77AC30"];

% names of the pictures
fotos = ["See_Sommer.jpg"];

for j = 1:length(fotos)
    %% Load Pictures

    dateiname = ['Geoplot-', char(fotos(j)), '.txt'];
   
    Data = importfile(['Input/',dateiname], [1, Inf]);
    
    KoordinatenX = zeros([5,5]);
    KoordinatenY = zeros([5,5]);
    Prop = zeros([5,1]);
    Celle = zeros([5,1]);
    
    for i = 1:5
        str1 = char(Data(i*4-3));
        doub1 = str2double(strsplit(str1(2:end-1),' '));
        str2 = char(Data(i*4-2));
        doub2 = str2double(strsplit(str2(2:end-1),' '));
        KoordinatenX(i,1:4)=doub1(1:4);
        KoordinatenY(i,1:4)=doub2(1:4);
        Prop(i) = str2double(char(Data(i*4-1)))*100;
        Celle(i) = str2double(char(Data(i*4)));
    end
    
    KoordinatenX(:,5) = KoordinatenX(:,1);
    KoordinatenY(:,5) = KoordinatenY(:,1);

    fprintf('Picture %d loaded \n',j)
    
    %% Plot
    figure('Visible','off');
    set(gcf,'Position',[300,1,2000,1000])
    % Overview
    subplot(2,3,1);
    for i=1:5
        geoplot(mean(KoordinatenX(i,1:4)),mean(KoordinatenY(i,1:4)),'o',LineWidth=3);
        hold on;
    end
    geolimits([-90,90],[-180,180]);
    geobasemap landcover
    legend("rank 1","rank 2","rank 3","rank 4","rank 5","Location","southeast");
    fprintf('- Overview done \n');
    %%{
    for i =1:5
        buffX=(max(KoordinatenX(i,:))-min(KoordinatenX(i,:)))*buff;
        buffY=(max(KoordinatenY(i,:))-min(KoordinatenY(i,:)))*buff;
        
        subplot(2,3,i+1)
        geoplot(KoordinatenX(i,:),KoordinatenY(i,:),LineWidth=2,Color=colors(i))
        geolimits([min(KoordinatenX(i,:))-buffX,max(KoordinatenX(i,:)+buffX)],[min(KoordinatenY(i,:))-buffY,max(KoordinatenY(i,:)+buffY)])
        geobasemap streets
        title(sprintf('Cell %d with %.2f %%', Celle(i),Prop(i)))
        fprintf('- Plot %d from 5 done (%d) \n',i,j)
    end
    %}
    exportgraphics(gcf,['Output/',dateiname(1:end-8),'.jpg'],'Resolution',300);
    fprintf('Picture %d plotted \n',j)

    clc;
    close all;

    % Empty working memory
    behalteVariablen = {'fotos', 'colors', 'buff','j'};
    alleVariablen = evalin('base', 'who');
    zuLoeschendeVariablen = setdiff(alleVariablen, behalteVariablen);
    for i = 1:length(zuLoeschendeVariablen)
        evalin('base', ['clear ', zuLoeschendeVariablen{i}]);
    end
end


