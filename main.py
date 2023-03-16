import pandas as pd

# This program will compare the current approved subjects of some sutdents with the total subjects needed to check if they can graduate or not.

# Studnets Ids
ids = [65681270, 65681291, 65612876, 65612957, 65731232, 65127414, 65127504, 61257700, 65712710, 65128093, 65921265, 66112153, 66112581, 66112614, 66122375, 66312841, 66481234, 66491207]
processed = 0

# Read the pdf using pandas.
for item in ids:    
    # The PDF's name is the same id of the student.
    df = pd.read_excel(f"path_to_the_pdf/{item}.xlsx", header=None)
    # print(df)

    print(f"-------------------< Working on the id: {item} >-------------------")

    # Create a dictionary so you can access the value with the key and check if the value is over 3.0 (approved) or not.
    sheet_dict = {}

    # iter and over the rows and colomns and add the subject name, the quantity of creds awarded, and the final score of the student to the "sheet_dict{}"
    for index, row in df.iterrows():
        subject = row[0]
        creds = row[1]
        score = row[2]
        sheet_dict[subject] = [creds, score]
        
    # print(sheet_dict)

    # The dictionary that will contain the name of the total subjects, the minimum creds needed, and the minimum score needed.
    # The keys of the dictionaries need to be excatly like this.
    reference_keys = {"GESTION BASICA DE LA":[3,3],
                        "APRENDIZAJE AUTONOMO":[2,3],
                        "COMUNICACION ESCRITA Y": [2,3],
                        "COMUNICACION ORAL Y PROCESOS":[2,3,],
                        "FUNDAMENTOS DE MATEMATICAS":[3,3],
                        "FUNDAMENTOS EN MATEMATICAS":[3,3],
                        "PROYECTO DE VIDA":[2,3],
                        "FUNDAMENTOS E HISTORIA DE LA":[3,3],
                        "INTRODUCCIO A LA INVESTIGACION":[2,3],
                        "INTRODUCCION A LA INVESTIGACION":[2,3],
                        "BIOLOGIA":[3,3],
                        "CÁTEDRA MINUTO DE DIOS":[2,3],
                        "CATEDRA MINUTO DE DIOS VIRTUAL":[2,3],
                        "EPISTEMOLOGIA DE LA PSICOLOGIA":[3,3],
                        "PROCESOS PSICOLOGICOS BASICOS":[3,3],
                        "SOCIOLOGIA":[2,3],
                        "ESTADISTICA DESCRIPTIVA":[3,3],
                        "DESARROLLO SOCIAL":[2,3],
                        "ANALISIS EXPERIMENTAL DEL":[3,3],
                        "PROCESOS COGNITIVOS SUPERIORES":[3,3],
                        "NEUROPSICOLOGIA":[2,3],
                        "INVESTIGACION I CUANTITATIVA":[2,3],
                        "ESTADISTICA II INFERENCIAL":[3,3],
                        "ESTADISTICA INFERENCIAL":[3,3],
                        "RESPONSABILIDAD SOCIAL UNA":[3,3],
                        "LA RESPONSABILIDAD SOCIAL UNA":[3,3],
                        "TEORIA PSICOANALITICA":[3,3],
                        "PSICOLOGIA DEL DESARROLLO":[2,3],
                        "DIFERENCIA INDIVIDUALES":[2,3],
                        "TECNICAS DE ENTREVISTA":[2,3],
                        "INGLES I":[3,3],
                        "INGLES AI":[3,3],
                        "CONSTITUCIÓN POLÍTICA":[2,3],
                        "PSICOLOGIA COGNITIVA":[3,3],
                        "PROCESOS PSICOLOGICOS SOCIALES":[2,3],
                        "ADULTEZ VEJEZ Y MUERTE":[2,3],
                        "PSICOMETRIA":[2,3],
                        "INGLÉS II":[3,3],
                        "INGLES AI BI":[3,3],
                        "ÉTICA PROFESIONAL":[2,3],
                        "ETICA PROFESIONAL":[2,3],
                        "ELECTIVA DE PROFUNDIZACION Y":[2,3],
                        "ESTRUCTURAS Y PSICOPATOLOGIA":[2,3],
                        "MEDICION Y EVALUACION":[2,3],
                        "INVESTIGACION II CUALITATIVA":[3,3],
                        "INGLÉS III":[3,3],
                        "RESOLUCION CONFLICTOS":[2,3],
                        "PSICOLOGIA SOCIAL-COMUNITARIA":[3,3],
                        "PSICOLOGIA CLINICA":[3,3],
                        "PRUEBAS":[3,3],
                        "INNOVACION Y CREATIVIDAD PARA":[2,3],
                        "PSICOLOGIA JURIDICA":[3,3],
                        "PSICOLOGIA EDUCATIVA":[3,3],
                        "MODELOS DE INTERVENCION I":[3,3],
                        "PSICOLOGIA ORGANIZACIONAL":[3,3],
                        "PRACTICA INVESTIGATIVA":[2,3],
                        "ESTRUCTURA DE UN PLAN DE":[2,3],
                        "ELECTIVA 2 MODELOS DE":[3,3],
                        "ELECTIVA CPC":[3,3],
                        "PRACTICA PROFESIONAL I":[5,3],
                        "ELECTIVA CMD":[3,3],
                        "ESTUDIO DE CASOS":[2,3],
                        "OPCION DE GRADO":[3,3],
                        "PRACTICA PROFESIONAL II":[5,3],
    }

    # This counter will help check if the total creds of the students are less than it should be.
    total_creds = 0

    # Loop and compare the students pdf information with the total dictionary created above.
    for element in reference_keys:
        if element in sheet_dict:
            value = sheet_dict.get(element)
            reference = reference_keys.get(element)
            # Check if the creds are not the same
            if float(value[0]) != float(reference[0]):
                print("The creds are not the same")
                print(f"SS creds are {value[0]}, Normal creds are {reference[0]}")
                print(f"Check the element {element}")
                total_creds += value[0]
            # Sometimes the students don't have a quantity but a qualitative score.
            elif value[1] == "A":
                total_creds += value[0]
            # If the student value is higher than 3.0 it will be counted as approved.
            elif float(value[1]) >= float(reference[1]):
                total_creds += value[0]
            elif float(value[1]) < float(reference[1]):
                print(element, "Reproboado")
        else: 
            # When the student hasn't taken the course, this will inform.
            print(f"The students misses {element}")

    print(f"\nTotal creds are {total_creds}")

    processed += 1
print(f"Total processed: {processed}")

