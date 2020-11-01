package hashcode;

import java.util.ArrayList;

public class Optimization implements Comparable<Optimization>{
	public int idCache;
	public int idVideo;
	public int idEndpoint; // useful to compute the improvements we obtain
	public int nRequests;
	public int videoSize;
	public long rating;
	public ArrayList<Optimization> relatedRequests;
	
	public Optimization() {
		this.relatedRequests = new ArrayList<Optimization>();
	}

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
