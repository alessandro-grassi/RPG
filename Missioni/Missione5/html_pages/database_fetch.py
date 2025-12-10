import queryLib

queryLib.connetti()

personaggio_id = queryLib.execute('SELECT "id" FROM "personaggi";')
personaggio_Nome = queryLib.execute('SELECT "Nome" FROM "personaggi";')
personaggio_Lvl = queryLib.execute('SELECT "Livello" FROM "personaggi";')
personaggio_Vig = queryLib.execute('SELECT "Vigore" FROM "personaggi";')
personaggio_Frz = queryLib.execute('SELECT "Forza" FROM "personaggi";')
personaggio_Dez = queryLib.execute('SELECT "Destrezza" FROM "personaggi";')
personaggio_Iq = queryLib.execute('SELECT "Intelligenza" FROM "personaggi";')
personaggio_Fed = queryLib.execute('SELECT "Fede" FROM "personaggi";')
personaggio_id_clss = queryLib.execute('SELECT "id_classe" FROM "personaggi";')



queryLib.disconnetti()

print("ID = ",personaggio_id[0][0])
print("Nome = ",personaggio_Nome[0][0])
print("Livello = ",personaggio_Lvl[0][0])
print("Vigore = ",personaggio_Vig[0][0])
print("Forza = ",personaggio_Frz[0][0])
print("Destrezza = ",personaggio_Dez[0][0])
print("Intelligenza = ",personaggio_Iq[0][0])
print("Fede = ",personaggio_Fed[0][0])
print("ID Classe = ",personaggio_id_clss[0][0])
