package hashcode;

import java.util.ArrayList;

public class CacheServer implements Comparable<CacheServer>{
	public int idCache;
	public int freeSize;
	public ArrayList<Integer> listOfVideos;
	public int nRequests;

	public CacheServer(int id, int size) {
		idCache         = id;
		freeSize        = size;
		listOfVideos    = new ArrayList<Integer>();
		nRequests      = 0;
	}

	@Override
	public int compareTo(CacheServer o) {
		return o.nRequests - this.nRequests;
	}
	
}
