import pandas as pd
from box_plot import box_plot
import matplotlib.pyplot as plt

#ar_dataset = np.genfromtxt('arrhythmia.data', delimiter=',')

# Kolone nemaju ime pa im se dodjeljuje 0-279
col_names = [str(x) for x in range(280)]
col_names[279] = 'Klasa'
col_names[0] = 'Godine'
#col_names[2] = 'Visina'
# col_names[14] = 'Brzina otkucaja srca'
col_names[16] = 'Prosječna širina R vala'
col_names[161] = 'Amplituda R vala'
col_names[4] = 'Trajanje QRS-a'
col_names[3] = 'Težina'
col_names[20] = 'Broj unutrašnjih otklona'
data = pd.read_csv('arrhythmia.data')
data.columns = col_names

klase = ['Normal', 'Isemic Changes', 'Old Anterior Myocardial Infarction', 'Old Inferior Myocardial Infarction', 'Sinus Tachycardy', 'Sinus bradycardy','Ventricular Premature Contraction', 'Supraventricular Premature Contraction', 'Left bundle branch block', '1st degree AV block', '2nd degree AV block', '3rd degree AV block','Left ventricule hypertrophy', 'Artrial Fibrillation or Flutter', 'Others']


box_plot(data, 'Godine', 'Klasa', 'Aritmija srca', klase,'Starost')
box_plot(data, 'Težina', 'Klasa', 'Aritmija srca', klase, 'Težina [kg]')
box_plot(data, 'Broj unutrašnjih otklona', 'Klasa', 'Aritmija srca', klase, 'Broj otklona')
box_plot(data, 'Trajanje QRS-a', 'Klasa', 'Aritmija srca', klase, 'Prosječna dužina trajanja QRS-a [ms]')
box_plot(data, 'Prosječna širina R vala', 'Klasa', 'Aritmija srca', klase, 'Prosječna širina R vala [ms]')

#plt.legend(klase)




plt.show()