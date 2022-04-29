%Tensor de Inercia
function [JCMi_i]= TensorInercia(l_i, h_i, w_i, rho_i)
syms x y z 'real'  %Coordenadas
syms l h w 'real'  %geometría del objeto
syms rho           %Densidad del objeto

r=[x; y; z];        %Vector de posicion respecto al centro de (masa
J=(r'*r*sym(eye(3))-r*r')*rho; %La expresión dentro de la integral

J= int(int(int(J, x, -l/2, l/2), y, -h/2, h/2),z, -w/2, w/2);
JCMi_i=subs(J, [l,h,w,rho],[l_i, h_i,w_i,rho_i]);

end
