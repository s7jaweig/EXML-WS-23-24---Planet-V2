clc, clear, close, dbstop if error;

buff = 0.5;
colors = ["#0072BD","#D95319","#EDB120","#7E2F8E","#77AC30"];

fotos = [""];

for j = 1:length(fotos)
    dateiname = ['Ergebnis-', char(fotos(j)), '.txt'];
    
    
    Ergebnislondon = importfile(dateiname, [1, Inf]);
    
    KoordinatenX = zeros([5,5]);
    KoordinatenY = zeros([5,5]);
    Prop = zeros([5,1]);
    Celle = zeros([5,1]);
    
    for i = 1:5
        str1 = char(Ergebnislondon(i*4-3));
        doub1 = str2double(strsplit(str1(2:end-1),' '));
        str2 = char(Ergebnislondon(i*4-2));
        doub2 = str2double(strsplit(str2(2:end-1),' '));
        KoordinatenX(i,1:4)=doub1(1:4);
        KoordinatenY(i,1:4)=doub2(1:4);
        Prop(i) = str2double(char(Ergebnislondon(i*4-1)))*100;
        Celle(i) = str2double(char(Ergebnislondon(i*4)));
    end
    
    KoordinatenX(:,5) = KoordinatenX(:,1);
    KoordinatenY(:,5) = KoordinatenY(:,1);

    fprintf('Foto %d eingeladen \n',j)
    
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
    fprintf('- Uebersicht fertig \n');
    %%{
    for i =1:5
        buffX=(max(KoordinatenX(i,:))-min(KoordinatenX(i,:)))*buff;
        buffY=(max(KoordinatenY(i,:))-min(KoordinatenY(i,:)))*buff;
        
        subplot(2,3,i+1)
        geoplot(KoordinatenX(i,:),KoordinatenY(i,:),LineWidth=2,Color=colors(i))
        geolimits([min(KoordinatenX(i,:))-buffX,max(KoordinatenX(i,:)+buffX)],[min(KoordinatenY(i,:))-buffY,max(KoordinatenY(i,:)+buffY)])
        geobasemap streets
        title(sprintf('Cell %d with %.2f %%', Celle(i),Prop(i)))
        fprintf('- Plot %d von 5 fertig (%d) \n',i,j)
    end
    %}
    exportgraphics(gcf,[dateiname(1:end-8),'.jpg'],'Resolution',300);
    fprintf('Foto %d geplottet \n',j)

    clc;
    close all;
    % Liste der Variablennamen, die behalten werden sollen
    behalteVariablen = {'fotos', 'colors', 'buff','j'};
    
    % Hol dir eine Liste aller aktuellen Variablennamen im Workspace
    alleVariablen = evalin('base', 'who');
    
    % Finde die zu löschenden Variablennamen
    zuLoeschendeVariablen = setdiff(alleVariablen, behalteVariablen);
    
    % Lösche die unerwünschten Variablen
    for i = 1:length(zuLoeschendeVariablen)
        evalin('base', ['clear ', zuLoeschendeVariablen{i}]);
    end
end


