f = fopen('dataAfraid.txt');
dataAfraid =textscan(f, ('%s'));
fclose(f);
variable = str2double(dataAfraid{1}(:,1));

a = fopen('dataScared.txt');
dataScared =textscan(a, ('%s'));
fclose(a);
variable2 = str2double(dataScared{1}(:,1));

b = fopen('dataConfused.txt');
dataConfused =textscan(b, ('%s'));
fclose(b);
variable3 = str2double(dataConfused{1}(:,1));

afraid = zeros(20,100);
confused = zeros(20,100);
scared = zeros(20,100);

j = 1;
k = 100;
for i=1 : 20
    afraid(i,:) = variable(j:k,1);
    scared(i,:) = variable2(j:k,1);
    confused(i,:) = variable3(j:k,1);
    
    j = k+1;
    k = k+100;
end


data2 = afraid;
data = scared;
data3 = confused;
options.handle     = figure(1);
options.color_area = [253 75 57]./255;    % red
options.color_line = [255 0 0]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data,options);
hold on
options.handle     = figure(1);
options.color_area = [36 180 247  ]./255;    %blue
options.color_line = [0 0 255  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data2,options);
hold on
options.handle     = figure(1);
options.color_area = [77 247 77  ]./255;    % green
options.color_line = [0 255 0  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data3,options);
title('Graphique de le qualité du belief states en fonction du temps (Layout Large filter)');
legend('Scared error','Scared','Afraid error','Afraid', 'Confused error', 'Confused' ,'Location','best')
xlabel ('incrément de temps [-]')
ylabel('qualité [-]')
hold off

f = fopen('dataAfraid2.txt');
dataAfraid =textscan(f, ('%s'));
fclose(f);
variable = str2double(dataAfraid{1}(:,1));

a = fopen('dataScared2.txt');
dataScared =textscan(a, ('%s'));
fclose(a);
variable2 = str2double(dataScared{1}(:,1));

b = fopen('dataConfused2.txt');
dataConfused =textscan(b, ('%s'));
fclose(b);
variable3 = str2double(dataConfused{1}(:,1));

afraid = zeros(20,100);
confused = zeros(20,100);
scared = zeros(20,100);

j = 1;
k = 100;
for i=1 : 20
    afraid(i,:) = variable(j:k,1);
    scared(i,:) = variable2(j:k,1);
    confused(i,:) = variable3(j:k,1);
    
    j = k+1;
    k = k+100;
end


data2 = afraid;
data = scared;
data3 = confused;
options.handle     = figure(2);
options.color_area = [253 75 57]./255;    % red
options.color_line = [255 0 0]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data,options);
hold on
options.handle     = figure(2);
options.color_area = [36 180 247  ]./255;    %blue
options.color_line = [0 0 255  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data2,options);
hold on
options.handle     = figure(2);
options.color_area = [77 247 77  ]./255;    % green
options.color_line = [0 255 0  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data3,options);
title('Graphique de la qualité du belief states en fonction du temps (Layout Large filter walls)');
legend('Scared error','Scared','Afraid error','Afraid', 'Confused error', 'Confused' ,'Location','best')
xlabel ('incrément de temps [-]')
ylabel('qualité [-]')
hold off


f = fopen('afraid_lf.txt');
dataAfraid =textscan(f, ('%s'));
fclose(f);
variable = str2double(dataAfraid{1}(:,1));

a = fopen('scared_lf.txt');
dataScared =textscan(a, ('%s'));
fclose(a);
variable2 = str2double(dataScared{1}(:,1));

b = fopen('confused_lf.txt');
dataConfused =textscan(b, ('%s'));
fclose(b);
variable3 = str2double(dataConfused{1}(:,1));

afraid = zeros(20,100);
confused = zeros(20,100);
scared = zeros(20,100);

j = 1;
k = 100;
for i=1 : 20
    afraid(i,:) = variable(j:k,1);
    scared(i,:) = variable2(j:k,1);
    confused(i,:) = variable3(j:k,1);
    
    j = k+1;
    k = k+100;
end


data2 = afraid;
data = scared;
data3 = confused;
options.handle     = figure(3);
options.color_area = [253 75 57]./255;    % red
options.color_line = [255 0 0]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data,options);
hold on
options.handle     = figure(3);
options.color_area = [36 180 247  ]./255;    %blue
options.color_line = [0 0 255  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data2,options);
hold on
options.handle     = figure(3);
options.color_area = [77 247 77  ]./255;    % green
options.color_line = [0 255 0  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data3,options);
title('Graphique de l''incertitude du belief state en fonction du temps (Layout Large filter)');
legend('Scared error','Scared','Afraid error','Afraid', 'Confused error', 'Confused' ,'Location','best')
xlabel ('incrément de temps [-]')
ylabel('incertitude [-]')
hold off

f = fopen('afraid_lfw.txt');
dataAfraid =textscan(f, ('%s'));
fclose(f);
variable = str2double(dataAfraid{1}(:,1));

a = fopen('scared_lfw.txt');
dataScared =textscan(a, ('%s'));
fclose(a);
variable2 = str2double(dataScared{1}(:,1));

b = fopen('confused_lfw.txt');
dataConfused =textscan(b, ('%s'));
fclose(b);
variable3 = str2double(dataConfused{1}(:,1));

afraid = zeros(20,100);
confused = zeros(20,100);
scared = zeros(20,100);

j = 1;
k = 100;
for i=1 : 20
    afraid(i,:) = variable(j:k,1);
    scared(i,:) = variable2(j:k,1);
    confused(i,:) = variable3(j:k,1);
    
    j = k+1;
    k = k+100;
end


data2 = afraid;
data = scared;
data3 = confused;
options.handle     = figure(4);
options.color_area = [253 75 57]./255;    % red
options.color_line = [255 0 0]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data,options);
hold on
options.handle     = figure(4);
options.color_area = [36 180 247  ]./255;    %blue
options.color_line = [0 0 255  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data2,options);
hold on
options.handle     = figure(4);
options.color_area = [77 247 77  ]./255;    % green
options.color_line = [0 255 0  ]./255;
options.alpha      = 0.3;
options.line_width = 2;
options.error      = 'c95';
plot_areaerrorbar(data3,options);
title('Graphique de l''incertitude du belief state en fonction du temps (Layout Large filter walls)');
legend('Scared error','Scared','Afraid error','Afraid', 'Confused error', 'Confused' ,'Location','best')
xlabel ('incrément de temps [-]')
ylabel('incertitude [-]')
hold off




