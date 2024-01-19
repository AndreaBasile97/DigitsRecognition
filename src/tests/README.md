**README.md**

    {'Aspect Ratio': {'outliers_identifiers': [], 'lower_limit': 1.0, 'upper_limit': 1.0}, 'Area': {'outliers_identifiers': [], 'lower_limit': 784.0, 'upper_limit': 784.0}, 'Brightness': {'outliers_identifiers': array(['116', '169', '175', '183', '185', '179', '181', '183', '149',
       '151', '155', '250', '215', '210', '273', '299', '267', '271',
       '281', '291', '285', '287', '280', '348', '428', '441', '418',
       '452', '536', '617', '622', '622', '584', '685', '687', '660',
       '694', '746', '766', '713', '789', '797', '803', '824', '812',
       '847', '852', '853', '893', '833', '839', '849', '861', '879',
       '885', '841', '855', '950', '1015', '1016', '1018', '1021', '1064',
       '1038', '1108', '1141', '1137', '1091', '1113', '1157', '1159',
       '1173', '1179', '1192', '1193', '1197', '1213', '1155', '1167',
       '1171', '1173', '1185', '1191', '1226', '1229', '1242', '1257',
       '1263', '1312', '1297', '1352', '1367', '1379', '1397', '1410',
       '1440', '1409', '1429', '1449'], dtype='<U5'), 'lower_limit': 7.123724489795919, 'upper_limit': 63.276466836734684}, 'RMS Contrast': {'outliers_identifiers': array(['92', '184', '244', '480', '544', '617', '580', '676', '710',
       '768', '846', '852', '1014', '1039', '1064', '1104', '1186',
       '1162', '1214', '1170', '1302'], dtype='<U5'), 'lower_limit': 42.96824126927275, 'upper_limit': 111.31539726215065}, 'Mean Red Relative Intensity': 'Not enough non-null samples to calculate outliers.', 'Mean Green Relative Intensity': 'Not enough non-null samples to calculate outliers.', 'Mean Blue Relative Intensity': 'Not enough non-null samples to calculate outliers.'}



# Analisi dell'Output di deepchecks su MNIST Dataset

L'output fornito è il risultato dell'analisi utilizzando la libreria deepchecks sul dataset MNIST. Di seguito è riportata un'analisi dettagliata dei risultati ottenuti.

## Proprietà Analizzate

### 1. Rapporto d'Aspetto (Aspect Ratio)

- **Outliers Identificati:** Nessun outlier rilevato.
- **Limiti:** Lower Limit = 1.0, Upper Limit = 1.0.
- **Analisi:** Tutte le immagini nel dataset hanno un rapporto d'aspetto compreso tra 1.0, indicando una uniformità nella forma.

### 2. Area

- **Outliers Identificati:** Nessun outlier rilevato.
- **Limiti:** Lower Limit = 784.0, Upper Limit = 784.0.
- **Analisi:** Tutte le immagini nel dataset hanno un'area pari a 784 pixel, indicando uniformità nelle dimensioni.

### 3. Luminosità (Brightness)

- **Outliers Identificati:** Sono stati identificati outliers con valori numerici.
- **Limiti:** Lower Limit = 7.12, Upper Limit = 63.28.
- **Analisi:** Alcune immagini presentano valori di luminosità al di fuori dei limiti stabiliti, suggerendo una variazione significativa nella luminosità delle immagini.

### 4. Contrasto RMS (RMS Contrast)

- **Outliers Identificati:** Sono stati identificati outliers con valori numerici.
- **Limiti:** Lower Limit = 42.97, Upper Limit = 111.32.
- **Analisi:** Alcune immagini presentano valori di contrasto RMS al di fuori dei limiti stabiliti, indicando una variazione significativa nella nitidezza delle immagini.

### 5. Intensità Media Relativa (Mean Red, Green, Blue Relative Intensity)

- **Outliers Identificati:** Non ci sono abbastanza campioni non nulli per calcolare gli outliers.
- **Analisi:** Non sono disponibili dati sufficienti per determinare gli outliers per le intensità relative medie nei canali rosso, verde e blu.

## Conclusioni

L'analisi suggerisce che la maggior parte delle immagini nel dataset MNIST ha caratteristiche uniformi in termini di rapporto d'aspetto e area. Tuttavia, sono state identificate alcune immagini con variazioni significative nella luminosità e nel contrasto RMS. Si consiglia un'ulteriore indagine su queste immagini per comprendere meglio le differenze e garantire la coerenza nel dataset.

*Nota: L'analisi si basa sui limiti specificati e potrebbe richiedere ulteriori considerazioni in base al contesto dell'applicazione.*