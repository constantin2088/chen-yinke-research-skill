"""Group declared source roots; this does not establish actual independence."""
def group_sources(records):
 groups={}
 for record in records:
  ident=record.get('id');origin=record.get('root')
  if not isinstance(ident,str) or not ident.strip():raise ValueError('source id required')
  if not isinstance(origin,str) or not origin.strip():raise ValueError('provenance root unknown; research it first')
  if any(ident in ids for ids in groups.values()):raise ValueError('duplicate source id')
  groups.setdefault(origin,[]).append(ident)
 return groups
