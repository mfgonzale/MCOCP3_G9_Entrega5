from matplotlib.pylab import *
from matplotlib import cm
import numpy as np

a = 1.
b = 1.

Nx = 30
Ny = 30

dx = b/Ny
dy = a/Nx

if dx!=dy:
	print('Error de dominio')
	exit(-1)


coords = lambda i,j:(dx*i,dy*j)

#def coords(i,j):
#	return (dx*i,dy*j)

x,y=coords(4,2)

u_k = zeros((Nx+1,Ny+1),dtype=double)
u_km1 = zeros((Nx+1,Ny+1),dtype=double)

u_k[:,:] = 20.

dt = 0.01
K = 79.5
c = 450.
ρ = 7800.
α = K*dt/ (c * ρ * dx**2)

print(f'dx={dx}')
print(f'dy={dy}')
print(f'K={K}')
print(f'c={c}')
print(f'rho={ρ}')
print(f'alpha={α}')


minuto = 60.
hora = 60. * minuto
dia = 24. * hora

dt = 1. * minuto
dnext_t= 0.5*hora

next_t = 0
framenum = 0

Days = 5.* dia

def truncate(n,decimals=0):
	multiplier = 10 ** decimals
	return int(n*multiplier)/multiplier
def imshowbien(u):
	imshow(u.T[Nx::-1,:],cmap=cm.coolwarm,interpolation='bilinear')
	cbar=colorbar(extend='both')#,cmap=cm.coolwarm)
	ticks=arange(0,35,5)
	ticks_Text=[f'{deg}°' for deg in ticks]
	cbar.set_ticks(ticks)
	cbar.set_ticklabels(ticks_Text)
	clim(0,30)

	xlabel('x')
	ylabel('y',rotation='horizontal')
	xTicks_N = arange(0,Nx+1,3)
	yTicks_N = arange(0,Ny+1,3)
	xTicks = [coords(i,0)[0] for i in xTicks_N]
	yTicks = [coords(0,j)[1] for j in yTicks_N]
	xTicks_Text=['{0:.2f}'.format(tick) for tick in xTicks]
	yTicks_Text=['{0:.2f}'.format(tick) for tick in yTicks]
	xticks(xTicks_N,xTicks_Text,rotation='vertical')
	yticks(yTicks_N,yTicks_Text)
	margins(0,2)
	subplots_adjust(bottom=0.15)

'''
u_0N4 = zeros(int(Days/dt))
u_1N4 = zeros(int(Days/dt))
u_2N4 = zeros(int(Days/dt))
u_3N4 = zeros(int(Days/dt))
'''
Superficie = zeros(int(Days/dt))
P1 = zeros(int(Days/dt))
P2 = zeros(int(Days/dt))
P3 = zeros(int(Days/dt))


for k in range(int32(Days/dt)):
	t=dt*(k+1)
	dias = truncate(t/dia,0)
	horas = truncate((t - dias*dia)/hora,0)
	minutos = truncate((t -dias*dia - horas*hora)/minuto,0)
	titulo ='k = {0:04.0f}, t = {1:02.0f}d {2:02.0f}h {3:02.0f}m'.format(k,dias,horas,minutos)
	#print(titulo)

	#Condiciones de Borde

	#BI = 25.  #Borde Izquierdo
	BI = -0.*dx + u_k[1,:]#Borde izquierdo, gradiente = -5
	#BIn= 20. #Borde Inferior
	BIn= -0.*dy + u_k[:,1]#Borde Inferior,gradiente =  0
	BS = 20. + 10.*np.sin(2*np.pi*t/dia)#Borde Superior
	#print(t/dia)
	#BS = 0.
	BD = -0.*dx + u_k[-2,:]#Borde derecho, gradiente = -5
	#BD = 25.

	u_k[0,:] = BI  #Borde izquierdo
	u_k[:,0] = BIn #Brode inferior
	u_k[:,-1]= BS  #Borde superior
	u_k[-1,:]= BD  #Borde derecho


	#Loop en el espacio i = 1.... n-1
	for i in range(1,Nx):
		for j in range(1,Ny):
			#Algoritmo de diferencias finitas 2-D para difusion

			#Laplaciano
			nabla_u_k= (u_k[i-1,j] + u_k[i,j-1] + u_k[i+1,j] + u_k[i,j+1] - 4*u_k[i,j])/ dx**2

			#Foward Euler
			u_km1[i,j] = u_k[i,j] + α*nabla_u_k
	u_k = u_km1

	#CB de nuevo
	u_k[0,:] = BI  #Borde izquierdo
	u_k[:,0] = BIn #Brode inferior
	u_k[:,-1]= BS  #Borde superior
	u_k[-1,:]= BD  #Borde derecho

	'''
	u_0N4[k]=u_k[int(Nx/2),     -1    ]
	u_1N4[k]=u_k[int(Nx/2),int(1*Ny/4)]
	u_2N4[k]=u_k[int(Nx/2),int(2*Ny/4)]
	u_3N4[k]=u_k[int(Nx/2),int(3*Ny/4)]
	'''
	Superficie[k]=u_k[int(Nx/2)  ,-1 ]

	P1[k]=u_k[int(Nx/2)  ,int(2*Ny/4)]
	P2[k]=u_k[int(Nx/2)  ,int(3*Ny/4)]
	P3[k]=u_k[int(3*Nx/4),int(3*Ny/4)]
	if t>next_t:
		figure(1)
		imshowbien(u_k)
		title(titulo)
		savefig("Caso_7/frame_{0:04.0f}.png".format(framenum))
		framenum += 1
		next_t += dnext_t
		close(1)

figure(2)
'''
plot(arange(int32(Days/dt))*dt/hora,u_0N4,label='Superficie')
plot(arange(int32(Days/dt))*dt/hora,u_1N4,label='1N/4')
plot(arange(int32(Days/dt))*dt/hora,u_2N4,label='2N/4')
plot(arange(int32(Days/dt))*dt/hora,u_3N4,label='3N/4')
'''
plot(arange(int32(Days/dt))*dt/hora,Superficie,label='Superficie')
plot(arange(int32(Days/dt))*dt/hora,P1,label='P1')
plot(arange(int32(Days/dt))*dt/hora,P2,label='P2')
plot(arange(int32(Days/dt))*dt/hora,P3,label='P3')
title('Evolucion de temperatura en puntos')
legend()
xlabel('Tiempo [hora]')
ylabel('Temperatura [°C]')
savefig("Caso_7/Grafico.png")
show()