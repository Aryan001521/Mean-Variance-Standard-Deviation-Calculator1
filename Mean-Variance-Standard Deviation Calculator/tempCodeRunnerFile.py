  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  list=np.array(list).reshape((3,3))