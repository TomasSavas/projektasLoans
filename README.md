# Vartojimo paskolų nemokumų prognozavimas

###Tikslas:
Sukurti logistinės regresijos modelį, kuris gebėtų suskirstyti klientus į gebančius grąžinti vartojimo kreditą 
ir nemokius.

### Duomenys:
Modelyje yra naudojami vieši duomenys apie vartojimo kreditus gavusius asmenis. Šiuos duomenis pateikia 
tarpusavio skolinimo platforma "Finbee" (https://www.finbee.lt/)

Modelyje naudoti duomenų kintamieji:
- 'Loan amount', (Paskolos suma)
- 'loan_number', (Turimų/turėtų paskolų skaičius)
- 'Family income', (Šeimos pajamos)
- 'Family liabilities', (Šeimos finansiniai įsipareigojimai)
- 'default', (Ar klientas tapo nemokus, 1 - taip, 0 - ne)
- 'Loan term', (Paskolos laikotarpis)
- 'Residential status', (Gyvenamos vietos statusas)
- 'Interest rate', (Palūkanų norma)
- 'Credit score', (Kredito reitingas)
- 'Gender' (Lytis)

### Finalinis modelis:
- XGBOOST logistinė regresija.
- Accuracy: 0.882073
- F1 score: 0.212014
- Roc_Auc_Score: 0.582396

### Išvada:
Pasiekti aukšto modelio tikslumo nepavyko, tačiau su turimais duomenimis pavyko padidinti benchmark modelyje turėtą 
ROC x iki 0.58. Modelis negali pakankamai tiksliai nuspėti, kuris klientas gavęs paskolą taps nemokus.
