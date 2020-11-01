package hashcode;

import java.util.ArrayList;

public class Endpoint{
	public int latencyToDataCenter;
	public int nCaches;
	public int [] latencyToCacheServers;
	public ArrayList<Request> videosRequested;

	public Endpoint(int TotalNumberOfCaches) {
		this.latencyToCacheServers = new int [TotalNumberOfCaches];
		this.videosRequested = new ArrayList<Request>();
	}

}
