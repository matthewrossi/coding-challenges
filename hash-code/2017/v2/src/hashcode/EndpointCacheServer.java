package hashcode;

public class EndpointCacheServer implements Comparable<EndpointCacheServer> {
	public int cacheServerId;
	public int cacheEndpointLatency;

	@Override
	public int compareTo(EndpointCacheServer ecs) {
		return this.cacheEndpointLatency - ecs.cacheEndpointLatency;
	}
}
