#En una institución educativa se realizará un torneo académico exclusivo para estudiantes que cumplan ciertos requisitos. Para poder participar, el estudiante debe tener una nota promedio igual o superior a 4.0 y una asistencia mínima del 85%. Sin embargo, existe una excepción: si el estudiante ha ganado algún reconocimiento académico durante el año, puede participar aunque no cumpla uno de los dos requisitos anteriores. El sistema debe evaluar si el estudiante puede participar o no en el torneo según esta información. Se deben pedir los datos necesarios y mostrar un mensaje claro indicando si puede o no participar.

nota_promedio_estudiante = float(input("Digite la nota promedio"))
asistencia_estudiante = int(input("DIgite en porcentaje la asistencia del estudiante"))
reconocimiento = "SI"
if nota_promedio_estudiante >= 4.0 and asistencia_estudiante >= 85:
    print ("el estudiante puede participar del torneo academico")

else:
    reconocimiento_estudiante = input ("El estudiante ha ganado algunreconocimiento? SI/NO").lower()
    if reconocimiento_estudiante == reconocimiento :
        print ("el estudiante puede participar del torneo academico")
    else:
        print ("el estudiante no puede participar del torneo academico")