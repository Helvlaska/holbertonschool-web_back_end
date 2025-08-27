export default function getStudentsByLocation(array, location) {
  const arrayLocationStudent = array.filter(element => element.location === location);
  return arrayLocationStudent;
}
