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

afraid = zeros(13,100);
confused = zeros(13,100);
scared = zeros(13,100);

j = 1;
k = 100;
for i=1 : 12
    afraid(i,:) = variable(j:k,1);
    scared(i,:) = variable2(j:k,1);
    confused(i,:) = variable3(j:k,1);
    
    j = k+1;
    k = k+100;
end

averageAfraid = zeros(100,1);
averageScared = zeros(100,1);
averageConfused = zeros(100,1);
varianceAfraid = zeros(100,1);
varianceScared = zeros(100,1);
varianceConfused = zeros(100,1);
for i = 1:100
    averageAfraid(i,1) = mean(afraid(:,i));
    varianceAfraid(i,1) = std(afraid(:,i));
    averageScared(i,1) = mean(scared(:,i));
    varianceScared(i,1) = std(scared(:,i));
    averageConfused(i,1) = mean(confused(:,i));
    varianceConfused(i,1) = std(confused(:,i));
end

figure(4)
x = 1:100;
errorbar(x, averageAfraid, varianceAfraid, 'r');
hold on
plot(x, averageAfraid, 'r');
title('Graphique de l incertitude du belief state en fonction du temps (Layout Large filter)');
%hold off

%figure(5)
errorbar(x, averageScared, varianceScared, 'b');
%hold on
plot(x, averageScared, 'b');
%title('Graph of quality of belief states for a ghost scared on layout large filter');
%hold off

%figure(6)
errorbar(x, averageConfused, varianceConfused, 'g');
%hold on
plot(x, averageConfused, 'g');
%title();
%hold off

xlabel ('incrément de temps [-]')
ylabel('incertitude [-]')
legend('Afraid error', 'Afraid','Scared error', 'Scared', 'Confused error', 'Confused')
hold off

    
