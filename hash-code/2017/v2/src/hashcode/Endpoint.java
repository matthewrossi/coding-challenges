package hashcode;

import java.util.ArrayList;

public class Endpoint implements Comparable<Endpoint> {
	public int idEndpoint;
	public int latencyToDataCenter;
	public int nCacheS;
	public ArrayList<EndpointCacheServer> cacheServers;
	public ArrayList<Request> videosRequested;
	public int rating;
	public ArrayList<Optimization> requestPriorities;

	public Endpoint() {
		this.videosRequested   = new ArrayList<Request>();
		this.cacheServers      = new ArrayList<EndpointCacheServer>();
		this.requestPriorities = new ArrayList<Optimization>();
	}

	@Override
	public int compareTo(Endpoint e) {
		// RETURN INVERSE LOGIC FOR DESC ORDER
		return e.rating - this.rating;
	}
}
