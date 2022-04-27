clc
close all
clear all

pause('on')


% coordenadas iniciales del carrito
x_0 = 20;
y_0 = 10;

% longitud de las aristas del cuadrado
targetDistance = 10;
% angulo de cada rotación
targetAngle = pi/2;

% stepsize: tamaño de los desplazamientos
stepSizeA = 1; % sobre las aristas
stepsizeB = pi/18; % sobre los angulos



% instancia del carrito
sq = Square(x_0,y_0);

% parametros para avanzar en cada iteración
d = 0; % DISTANCIA 
alpha = 0; % ANGULO DE ROTACIÓN
 
% COORDENADAS INICIALES
sqCoordinates = sq.getPosition();
x = sqCoordinates(1);
y = sqCoordinates(2);




for i = 1:4
    [d,alpha] = reset(); % estado: RESET
    % RESET -> ROTACIÓN
    alpha = sq.getRotationAngle(targetAngle*i,stepsizeB); % ESTADO ROTACIÓN}
    

    
    % ROTACIÓN -> AVANZAR
    while d < targetDistance % AVANZAR -> AVANZAR
       pause(0.5);
       d = d + stepSizeA;
       rotatedVector = getRotatedPosition(alpha,stepSizeA);
       sq = sq.advance(rotatedVector);
       cordVec = sq.getPosition();
       x = cordVec(1);
       y = cordVec(2);
       
       Y_LIM = [0 30];
       X_LIM = [0 30];
       plot(x,y,'bo')
       xlim(X_LIM)
       ylim(Y_LIM)
       hold on
       grid on
       
    end
        
end % AVANZAR -> RESET



% regresa un vector del componente x con la posición ajustada al giro de
% theta
function rotated = getRotatedPosition(theta,x)
    rotationMatrix = [cos(theta) -sin(theta) 0; sin(theta) cos(theta) 0; 0 0 1];
    vector = [x;0;0];
    rotated = rotationMatrix*vector;
end

function [d,alpha] = reset()
    d = 0;
    alpha = 0;
end
