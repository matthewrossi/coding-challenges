package hashcode;

import java.util.ArrayList;

public class CacheServer implements Comparable<CacheServer>{
	public int idCache;
	public int freeSize;
	public ArrayList<Integer> listOfVideos;
	public int nEndpoints;

	public CacheServer(int id, int size) {
		idCache         = id;
		freeSize        = size;
		listOfVideos    = new ArrayList<Integer>();
		nEndpoints      = 0;
	}

	@Override
	public int compareTo(CacheServer o) {
		return o.nEndpoints - this.nEndpoints;
	}
	
}
