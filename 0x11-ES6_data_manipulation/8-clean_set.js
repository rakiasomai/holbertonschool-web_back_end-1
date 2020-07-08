export default function cleanSet(set, str) {
  let val = '';
  for (const el of set) {
    if (el.startsWith(str)) {
      val += val.length === 0 ? el.replace(str, '') : el.replace(str, '-');
    }
  }
  return val;
}
