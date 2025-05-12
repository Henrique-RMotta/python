import pyshorteners as ps

url = "https://secretariadigital.sp.senai.br/WebForms/Login.aspx?ReturnUrl=%2f"
u = ps.Shortener().tinyurl.short(url)
print(u)