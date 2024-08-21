import numpy as np

def salvar_histogramas(histogramas, nome_base):
    for i, hist in enumerate(histogramas):
        intensidade = np.arange(256)
        hist_data = np.hstack((intensidade.reshape(-1, 1), hist))
        np.savetxt(f'{nome_base}_hist{i}.csv', hist_data, delimiter=',', header='Intensidade,Contagem', comments='', fmt='%d')
