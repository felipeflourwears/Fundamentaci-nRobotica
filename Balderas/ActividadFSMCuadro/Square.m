classdef Square
    properties
        x
        y
        z
        
    end
    methods
        % construtor
        function obj = Square(x_0,y_0)
            obj.x = x_0;
            obj.y = y_0;
            obj.z = 0;
        end
        
        % avanzar 
        % cordVector: Un vector de coordenadas ajustando a la posición en
        % función del desplazamiento y la rotación
        function obj =  advance(obj,colVector)
            obj.x = obj.x + colVector(1);
            obj.y = obj.y + colVector(2);
            obj.z = obj.z + colVector(3);

        end
        
        % obtener nuevo angulo de rotación
        function alpha = getRotationAngle(obj,targetAngle,stepsize)
            alpha = 0.0;
            while alpha <= targetAngle % ROTACIÓN -> ROTACIÓN
                %fprintf("rotando...");
                if alpha >= targetAngle
                    break;
                end
                alpha = alpha + stepsize;
            end
            if alpha ~= pi/2
                alpha = alpha -stepsize;
            end
            
        end
        
        % obtener un vector columna con las coordenadas del sistema del
        % coche
        function coord = getPosition(obj)
            coord = [obj.x;obj.y;obj.z];
        end
    end
end