export default function getStudentIdsSum(array){
  const sum = array.reduce((sum, array) => sum + array.id, 0);
  return sum;
}
