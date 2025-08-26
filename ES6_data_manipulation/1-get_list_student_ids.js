export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  else {
    const ids = array.map(array => array.id)
    return ids;
  }
}
