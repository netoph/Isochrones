import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#To save you time
#Plot radial Lick index in index-index diagram with the isochrones of the model of Thomas et al. 2003.


def plot_index_indexthomas03(dataframeentrada,name,indice_ejex,indice_ejey):
	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')
	plt.rc('xtick', labelsize='large')
	plt.rc('ytick', labelsize='large')
	#df=pd.read_csv(dataframeentrada,index_col=0)
	df=pd.read_csv(dataframeentrada,sep=',',index_col='ra') #plot radial data in dependence of radius from 20 to 40 arcsec etc..
	plt.errorbar(df[indice_ejex][20:40],df[indice_ejey][20:40],yerr=df[indice_ejey+'_err'][20:40], xerr=df[indice_ejex+'_err'][20:40], elinewidth=.5, fmt='*',markersize=7,label=' radial + [20:40]')
	plt.errorbar(df[indice_ejex][-40:-20],df[indice_ejey][-40:-20],yerr=df[indice_ejey+'_err'][-40:-20], xerr=df[indice_ejex+'_err'][-40:-20], elinewidth=.5, fmt='*',markersize=7,label='radial - [-40:-20]')

	#plt.plot(df[indice_ejex][89],df[indice_ejey][89],color='b',marker='*',ms=20,label='Second nuclei')
	plt.plot(df[indice_ejex][0],df[indice_ejey][0],color='g',marker='*',ms=20,label='Galaxy center')
	plt.errorbar(df[indice_ejex][-20:-10],df[indice_ejey][-20:-10],yerr=df[indice_ejey+'_err'][-20:-10], xerr=df[indice_ejex+'_err'][-20:-10], elinewidth=.5, fmt='*',markersize=7,label='radial - [-20:-10]')
	plt.errorbar(df[indice_ejex][-10:0],df[indice_ejey][-10:0],yerr=df[indice_ejey+'_err'][-10:0], xerr=df[indice_ejex+'_err'][-10:0], elinewidth=.5, fmt='*',markersize=7,label='radial - [-10:0]')
	plt.errorbar(df[indice_ejex][0:10],df[indice_ejey][0:10],yerr=df[indice_ejey+'_err'][0:10], xerr=df[indice_ejex+'_err'][0:10], elinewidth=.5, fmt='*',markersize=7,label='Central data [0:10]')
	plt.errorbar(df[indice_ejex][10:20],df[indice_ejey][10:20],yerr=df[indice_ejey+'_err'][10:20], xerr=df[indice_ejex+'_err'][10:20], elinewidth=.5, fmt='*',markersize=7,label='radial [10:20]')
	plt.errorbar(df[indice_ejex][40:110],df[indice_ejey][40:110],yerr=df[indice_ejey+'_err'][40:110], xerr=df[indice_ejex+'_err'][40:110], elinewidth=.5, fmt='*',markersize=7,label='radial [40:110]')
	plt.errorbar(df[indice_ejex][-110:-40],df[indice_ejey][-110:-40],yerr=df[indice_ejey+'_err'][-110:-40], xerr=df[indice_ejex+'_err'][-110:-40], elinewidth=.5, fmt='*',markersize=7,label='radial [-110:-40]')
#	for i in range(70,118):
#		plt.annotate('R='+str(df['R'][i]),(df[indice_ejex][i],df[indice_ejey][i]),fontsize=8)
	plt.title(name)
	plt.xlabel(indice_ejex+'(\AA)')
	plt.ylabel(indice_ejey+'(\AA)')
	if indice_ejex == 'NaD':		
		plt.xlim(0.5,5.5)
	elif indice_ejex == 'MgFe':
		plt.xlim(0.5,7)
		plt.xlabel(r'[MgFe]')
	elif indice_ejex == 'Mg2':
		plt.xlim(0,0.4)
		plt.xlabel(r'Mg$_{2}$ (Mag)')
	elif indice_ejex == 'B-V':
		plt.xlim(0.4,1.2)
		plt.xlabel(r'(B-V)$_{phot}$')
	elif indice_ejex == 'B-Vs':
		plt.xlim(0.4,1.2)
		plt.xlabel(r'(B-V)$_{syn}$')
		indice_ejex='B-V'
	elif indice_ejex == 'ML':
		plt.xlim(0,7)
		plt.xlabel(r'M/L')
	elif indice_ejex == 'MH':
		plt.xlim(-1.8,.40)
		plt.xlabel(r'[M/H]')
	elif indice_ejex == 'CN1':
		plt.xlim(-.18,0.3)
		plt.xlabel(r'CN1 (Mag)')


	if indice_ejey == 'HdA':		
		plt.ylim(-10.5,10.5)
		plt.ylabel(r'H$\delta$A'+'(\AA)')
	elif indice_ejey == 'NaD':		
		plt.ylim(0.5,5.5)
	elif indice_ejey == 'MgFe':
		plt.ylim(0.5,7)
		plt.ylabel(r'[MgFe]')
	elif indice_ejey == 'Hb':
		plt.ylim(-3.5,6)
		plt.ylabel(r'H$\beta$'+'(\AA)')
	elif indice_ejey == 'HgA':
		plt.ylim(-10,10)
		plt.ylabel(r'H$\gamma$A'+'(\AA)')
	elif indice_ejey == 'B-V':
		plt.ylim(0.4,1.2)
		plt.ylabel(r'(B-V)$_{phot}$')
	elif indice_ejey == 'B-Vs':
		plt.ylim(0.4,1.2)
		plt.ylabel(r'(B-V)$_{syn}$')
		indice_ejey='B-V'
	elif indice_ejey == 'MH':
		plt.ylim(-1.8,.40)
		plt.ylabel(r'[M/H]')
	elif indice_ejey == 'ML':
		plt.ylim(0,7)
		plt.ylabel(r'M/L')
	elif indice_ejey == 'Mg2':
		plt.ylim(0,0.4)
		plt.ylabel(r'Mg$_{2}$ (Mag)')
	elif indice_ejey == 'CN1':
		plt.ylim(-.18,0.12)
		plt.ylabel(r'CN1 (Mag)')


	df2=pd.read_csv('thomson03.csv',index_col=2) #Needs the file with Thomas et al. 2003 with the model. this case is alpha =0.3
	df3=pd.read_csv('thomson03.csv',index_col=1) #Needs the file with Thomas et al. 2003 with the model.
	plt.plot(df2[indice_ejex][-2.25],df2[indice_ejey][-2.25], '--', label='[Z/H]=-2.25')
	plt.plot(df2[indice_ejex][-2.25],df2[indice_ejey][-2.25], '.',label='_nolegend_')
	plt.annotate('1 Gyr',(float(df3[indice_ejex][1].values[0]),float(df3[indice_ejey][1].values[0])),fontsize=6)
	plt.annotate('1 Gyr',(float(df3[indice_ejex][1].values[1]),float(df3[indice_ejey][1].values[1])),fontsize=6)
	plt.annotate('1 Gyr',(float(df3[indice_ejex][1].values[2]),float(df3[indice_ejey][1].values[2])),fontsize=6)
	plt.annotate('1 Gyr',(float(df3[indice_ejex][1].values[3]),float(df3[indice_ejey][1].values[3])),fontsize=6)
	plt.annotate('1 Gyr',(float(df3[indice_ejex][1].values[4]),float(df3[indice_ejey][1].values[4])),fontsize=6)
	plt.annotate('1 Gyr',(float(df3[indice_ejex][1].values[5]),float(df3[indice_ejey][1].values[5])),fontsize=6)
	plt.annotate('5 Gyr',((float(df3[indice_ejex][5].values[0]),float(df3[indice_ejey][5].values[0]))),fontsize=6)
	plt.annotate('5 Gyr',((float(df3[indice_ejex][5].values[1]),float(df3[indice_ejey][5].values[1]))),fontsize=6)
	plt.annotate('5 Gyr',((float(df3[indice_ejex][5].values[2]),float(df3[indice_ejey][5].values[2]))),fontsize=6)
	plt.annotate('5 Gyr',((float(df3[indice_ejex][5].values[3]),float(df3[indice_ejey][5].values[3]))),fontsize=6)
	plt.annotate('5 Gyr',((float(df3[indice_ejex][5].values[4]),float(df3[indice_ejey][5].values[4]))),fontsize=6)
	plt.annotate('5 Gyr',((float(df3[indice_ejex][5].values[5]),float(df3[indice_ejey][5].values[5]))),fontsize=6)
	plt.annotate('10 Gyr',((float(df3[indice_ejex][10].values[0]),float(df3[indice_ejey][10].values[0]))),fontsize=6)
	plt.annotate('10 Gyr',((float(df3[indice_ejex][10].values[1]),float(df3[indice_ejey][10].values[1]))),fontsize=6)
	plt.annotate('10 Gyr',((float(df3[indice_ejex][10].values[2]),float(df3[indice_ejey][10].values[2]))),fontsize=6)
	plt.annotate('10 Gyr',((float(df3[indice_ejex][10].values[3]),float(df3[indice_ejey][10].values[3]))),fontsize=6)
	plt.annotate('10 Gyr',((float(df3[indice_ejex][10].values[4]),float(df3[indice_ejey][10].values[4]))),fontsize=6)
	plt.annotate('10 Gyr',((float(df3[indice_ejex][10].values[5]),float(df3[indice_ejey][10].values[5]))),fontsize=6)
	plt.annotate('12 Gyr',((float(df3[indice_ejex][12].values[0]),float(df3[indice_ejey][12].values[0]))),fontsize=6)
	plt.annotate('12 Gyr',((float(df3[indice_ejex][12].values[1]),float(df3[indice_ejey][12].values[1]))),fontsize=6)
	plt.annotate('12 Gyr',((float(df3[indice_ejex][12].values[2]),float(df3[indice_ejey][12].values[2]))),fontsize=6)
	plt.annotate('12 Gyr',((float(df3[indice_ejex][12].values[3]),float(df3[indice_ejey][12].values[3]))),fontsize=6)
	plt.annotate('12 Gyr',((float(df3[indice_ejex][12].values[4]),float(df3[indice_ejey][12].values[4]))),fontsize=6)
	plt.annotate('12 Gyr',((float(df3[indice_ejex][12].values[5]),float(df3[indice_ejey][12].values[5]))),fontsize=6)
	plt.annotate('15 Gyr',((float(df3[indice_ejex][12].values[0]),float(df3[indice_ejey][12].values[0]))),fontsize=6)
	plt.annotate('15 Gyr',((float(df3[indice_ejex][12].values[1]),float(df3[indice_ejey][12].values[1]))),fontsize=6)
	plt.annotate('15 Gyr',((float(df3[indice_ejex][12].values[2]),float(df3[indice_ejey][12].values[2]))),fontsize=6)
	plt.annotate('15 Gyr',((float(df3[indice_ejex][12].values[3]),float(df3[indice_ejey][12].values[3]))),fontsize=6)
	plt.annotate('15 Gyr',((float(df3[indice_ejex][12].values[4]),float(df3[indice_ejey][12].values[4]))),fontsize=6)
	plt.annotate('15 Gyr',((float(df3[indice_ejex][12].values[5]),float(df3[indice_ejey][12].values[5]))),fontsize=6)
	plt.plot(df2[indice_ejex][-1.35],df2[indice_ejey][-1.35], '--', label='[Z/H]=-1.35')
	plt.plot(df2[indice_ejex][-1.35],df2[indice_ejey][-1.35], '.',label='_nolegend_')
	plt.plot(df2[indice_ejex][-0.33],df2[indice_ejey][-0.33], '--', label='[Z/H]=-0.33')
	plt.plot(df2[indice_ejex][-0.33],df2[indice_ejey][-0.33], '.',label='_nolegend_')
	plt.plot(df2[indice_ejex][0],df2[indice_ejey][0], '--', label='[Z/H]=0.0')
	plt.plot(df2[indice_ejex][0],df2[indice_ejey][0], '.',label='_nolegend_')
	plt.plot(df2[indice_ejex][0.35],df2[indice_ejey][0.35], '--', label='[Z/H]=0.35')
	plt.plot(df2[indice_ejex][0.35],df2[indice_ejey][0.35], '.',label='_nolegend_')
	plt.plot(df2[indice_ejex][0.67],df2[indice_ejey][0.67], '--', label='[Z/H]=0.67')
	plt.plot(df2[indice_ejex][0.67],df2[indice_ejey][0.67], '.',label='_nolegend_')
	plt.legend(loc='best')

	plt.savefig('Resultados/'+name+indice_ejex+'VS'+indice_ejey+'.pdf', dpi=300)
	plt.show()
