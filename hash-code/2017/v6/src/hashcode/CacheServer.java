package hashcode;

import java.util.ArrayList;

public class CacheServer implements Comparable<CacheServer>{
	public int idCache;
	public int freeSize;
	public ArrayList<Integer> listOfVideos;
	public long totLatencyGain;

	public CacheServer(int id, int size) {
		idCache         = id;
		freeSize        = size;
		listOfVideos    = new ArrayList<Integer>();
		totLatencyGain  = 0;
	}

	@Override
	public int compareTo(CacheServer o) {
		long diff =  o.totLatencyGain - this.totLatencyGain;
		if (diff > 0)
			return 1;
		if (diff < 0)
			return -1;
		return 0;
	}
	
}
