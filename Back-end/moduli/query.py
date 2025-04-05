import queryLib

queryLib.connetti()
print(
    queryLib.execute("SELECT * FROM classi")
)
