package hashcode;

import java.util.ArrayList;

public class CacheServer {
	public int freeSize;
	public ArrayList<Integer> listOfVideos;
	public ArrayList<CacheServerRating> candidateVideos;

	public CacheServer(int size) {
		freeSize        = size;
		listOfVideos    = new ArrayList<Integer>();
		candidateVideos = new ArrayList<CacheServerRating>();
	}
}
