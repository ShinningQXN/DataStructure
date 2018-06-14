def min_num_square(w, h):
	if w == h:
		return 1
	if w > h:
		w, h = h, w
	count = 1 + min_num_square(w, h - w)
	return count

print min_num_square(5, 6)


