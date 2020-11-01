package hashcode;

public class Optimization implements Comparable<Optimization>{
	public int idVideo;
	public int videoSize;
	public long nRequests;
	
	@Override
	public int compareTo(Optimization o) {
		// RETURN INVERSE LOGIC FOR DESC ORDER
		double delta = (double)o.nRequests/(double)o.videoSize - (double)this.nRequests/(double)this.videoSize;
		if(delta > 0)
			return 1;
		if (delta < 0)
			return -1;
		return this.videoSize - o.videoSize;
	}

}
