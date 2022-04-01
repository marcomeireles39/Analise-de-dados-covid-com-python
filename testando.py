from DCovid import *

dados = ObsCovid("Confirmados")
dados2 = ObsCovid("Óbito")

dados.Pais("Brazil")
dados.Salvar_Dados()
dados.S_local