export default function createReportObject(employeesList) {
  return {
    // Réconstruit un objet avec les mêmes key/value
    allEmployees: {...employeesList},

    // Récupère le nombre de key
    getNumberOfDepartments(obj) {
        return Object.keys(obj).length
    },
  };
}
