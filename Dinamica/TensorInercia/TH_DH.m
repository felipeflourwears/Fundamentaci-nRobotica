function Ti_j=TH_DH(a_i, alpha_i, theta_i, d_i)
    %syms a_i d_i theta_i alpha_i t l     % Parámetros DH
    syms t
    I4= sym(eye(4));                    % Transformación homogenea general
    Rx = I4;                            % Transformación homogenea de rotacion sobre eje X
    Rx(1:3,1:3) = [1 0 0; 0 cos(t) -sin(t); 0 sin(t) cos(t)];       
    Rx = subs(Rx, t, alpha_i);
    Dx=I4;
    Dx(1:3, 4)=[a_i; 0; 0];
    Rz = I4;                    % Transformación homogenea de rotacion sobre eje Z
    Rz(1:3,1:3) = [cos(t) -sin(t) 0; sin(t) cos(t) 0; 0 0 1];
    Rz = subs(Rz, t, theta_i);
    Dz = I4;                    % Transformación homogenea de desplazamiento sobre eje Z
    Dz(1:3,4) = [0; 0; d_i];
    Ti_j = Dz*Rz*Dx*Rx;
end