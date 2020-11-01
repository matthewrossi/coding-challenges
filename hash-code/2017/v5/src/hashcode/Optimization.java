package hashcode;

public class Optimization implements Comparable<Optimization>{
	public int idCache;
	public int idVideo;
	public int videoSize;
	public long rating;
	public int[] endpointsNumberOfRequest;
	
	public Optimization(int nEndpoints) {
		endpointsNumberOfRequest = new int[nEndpoints];
	}
	
	@Override
	public int compareTo(Optimization o) {
		// RETURN INVERSE LOGIC FOR DESC ORDER
		double delta = (double)o.rating/(double)o.videoSize - (double)this.rating/(double)this.videoSize;
		if(delta > 0)
			return 1;
		if (delta < 0)
			return -1;
		return this.videoSize - o.videoSize;
	}

}
