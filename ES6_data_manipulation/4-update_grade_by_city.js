export default function updateStudentGradeByCity(arrayStudents, location, arrayGrades) {
  // Récupère les étudiants de la location donnée
  const studentsInCity = arrayStudents.filter(student => student.location === location);

  // Retourne un nouveau tableau avec .map()
  const updateStudent = studentsInCity.map(student => {
    // Cherche l'id de l'étudiant dans le tableau de grade
    const gradeFound = arrayGrades.find(item => item.studentId === student.id);

    // Déclare une variable pour stocker le grade si trouvé
    let grade;
    // Vérifie si un grade existe
    if (gradeFound) {
        // Si oui, le récupère et le stock
        grade = gradeFound.grade;
    } else {
        // Sinon, grade = 'N/A'
        grade = "N/A";
    }

    // Retourne le nouvel objet avec le grade inclu
    return {
        ...student,     // Récupère les infos de l'étudiant
        grade: grade    // Ajout du grade dans l'objet
    };
  });

  // Retourne le tableau final
  return updateStudent;
}
