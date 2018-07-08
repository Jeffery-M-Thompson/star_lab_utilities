
# SDSS utilities

def getWedge(position):
	b = position.galactic.b.deg
	if b >= 0:
		stripes = range(1, 45)
		nd = 95*u.deg
	else:
		stripes = range(61, 91)
		nd = 275*u.deg

	for strp in stripes:
		gc = coord.SDSSMuNu(stripe=strp, node = nd)
		nu = coord.radec_to_munu(position, gc).nu.deg
		if np.abs(nu)<=1.25:
			mu = coord.radec_to_munu(position,gc).mu.deg
			wedge = strp
			break
		else:
			mu = 999
			nu = 999
			wedge = 0

	return wedge, mu, nu
