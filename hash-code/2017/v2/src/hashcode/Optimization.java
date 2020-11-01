package hashcode;

public class Optimization implements Comparable<Optimization>{
	public int idVideo;
	public int videoSize;
	public int nRequests;
	public long rating;
	public int endpoint;
	public int attempts;

	@Override
	public int compareTo(Optimization o) {
		// RETURN INVERSE LOGIC FOR DESC ORDER
		long diff = o.rating - this.rating;
		int ris;

		if (diff == 0) {
			ris = this.videoSize - o.videoSize;
		} else if(diff > 0) {
			ris = 1;
		} else {
			ris = -1;
		}

		return ris;
	}
}
