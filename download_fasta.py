# -*- coding: utf-8 -*-

import requests
import gzip
import io

def download_fasta(api_url, output_file):
    try:
        # Faire la requête GET à l'API
        response = requests.get(api_url)
        
        # Vérifier que la requête a été réussie
        if response.status_code == 200:
            # Vérifier si le contenu est compressé
            if response.headers.get('Content-Encoding') == 'gzip':
                # Si les données sont compressées, les décompresser
                compressed_data = io.BytesIO(response.content)
                with gzip.GzipFile(fileobj=compressed_data) as decompressed_file:
                    data = decompressed_file.read().decode('utf-8')
            else:
                # Si les données ne sont pas compressées
                data = response.text
            
            # Enregistrer le résultat dans un fichier local
            with open(output_file, 'w') as file:
                file.write(data)
            
            print("Les données ont été enregistrées dans {}".format(output_file))
        else:
            print("Échec de la requête. Code de statut : {}".format(response.status_code))
    except Exception as e:
        print("Une erreur s'est produite : {}".format(e))

# URL de l'API
api_url = "https://rest.uniprot.org/idmapping/uniprotkb/results/stream/3dbb8bcade55cce38fc3f05884956f20f479184d?compressed=true&format=fasta"
# Nom du fichier de sortie
output_file = "resultat.fasta"

# Appeler la fonction pour interroger l'API et enregistrer le résultat
download_fasta(api_url, output_file)