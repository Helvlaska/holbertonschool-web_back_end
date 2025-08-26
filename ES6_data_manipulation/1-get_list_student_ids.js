export default function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  else {
    const ids = []
    for (let i in array) {
      ids.push(array[i].id);
    }
    return ids;
  }
}
