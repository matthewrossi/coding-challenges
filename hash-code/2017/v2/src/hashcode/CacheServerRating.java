package hashcode;

public class CacheServerRating implements Comparable<CacheServerRating> {
	public int idVideo;
	public long rating;
	public int videoSize;

	@Override
	public int compareTo(CacheServerRating cr) {
		// RETURN INVERSE LOGIC FOR DESC ORDER
		if (cr.rating > this.rating)
			return 1;
		else if (cr.rating < this.rating)
			return -1;
		else
			return 0;
	}
}
