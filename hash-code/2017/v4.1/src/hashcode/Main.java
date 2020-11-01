package hashcode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class Main {
//	private static final String FILENAME = "me_at_the_zoo";
//	private static final String FILENAME = "trending_today";
//	private static final String FILENAME = "videos_worth_spreading";
	private static final String FILENAME = "kittens";

	private static String listToString(List<?> list) {
	    String result = "";
	    for (int i = 0; i < list.size(); i++) {
	        result += list.get(i);
	        if (i != list.size() -1) {
	        	result += " ";
	        }
	    }
	    return result;
	}

	public static void main(String[] args) {

		BufferedReader br = null;
		FileReader fr = null;
		PrintWriter writer = null;

		try {

			fr = new FileReader("C:\\Users\\Matt\\Documents\\Hash code\\Online-Qualification-Round-Problem-for-Google-Hash-Code-2017-Data-Sets\\"+FILENAME+".in");
			br = new BufferedReader(fr);

			String[] line = br.readLine().split(" ");

			// read problem dimension
			int nVideos       = Integer.parseInt(line[0]);
			int nEndpoint     = Integer.parseInt(line[1]);
			int nRequests     = Integer.parseInt(line[2]);
			int nCacheServers = Integer.parseInt(line[3]);
			int cacheSize     = Integer.parseInt(line[4]);

			// read videos dimension
			line = br.readLine().split(" ");
			int[] videosSize = new int[nVideos];
			for(int i=0; i<line.length; i++) {
				videosSize[i] = Integer.parseInt(line[i]);
			}
			
			// create cache servers
			ArrayList<CacheServer> cacheServers = new ArrayList<CacheServer>();
			for (int idCache = 0; idCache<nCacheServers; idCache++) {
				cacheServers.add(new CacheServer(idCache, cacheSize));
			}

			// read endpoints info
			ArrayList<Endpoint> endpoints = new ArrayList<Endpoint>(nEndpoint);			
			for (int idEndpoint = 0; idEndpoint < nEndpoint; idEndpoint++) {				
				line = br.readLine().split(" ");
				Endpoint e = new Endpoint(nCacheServers);
				e.idEndpoint = idEndpoint;
				e.latencyToDataCenter = Integer.parseInt(line[0]);
				e.nCaches = Integer.parseInt(line[1]);
				for (int j = 0; j < e.nCaches; j++) {					
					line = br.readLine().split(" ");
					int idCache = Integer.parseInt(line[0]);
					e.latencyToCacheServers[idCache] = Integer.parseInt(line[1]);
				}
				endpoints.add(e);
			}

			// read requests info
			for (int i=0; i<nRequests; i++) {
				line = br.readLine().split(" ");
				Request r = new Request();
				r.idVideo = Integer.parseInt(line[0]);
				r.nRequests = Integer.parseInt(line[2]);
				Endpoint e = endpoints.get(Integer.parseInt(line[1]));
				e.videosRequested.add(r);
				for (int idCache = 0; idCache < nCacheServers; idCache++) {
					if (e.latencyToCacheServers[idCache] > 0) {
						cacheServers.get(idCache).nRequests += r.nRequests;
					}
				}
			}
			
			// sort cache servers based on the #requests they get
			Collections.sort(cacheServers);
			
			// cache that satisfy a given request
			HashMap<Request, ArrayList<Integer>> satisfiedBy = new HashMap<Request, ArrayList<Integer>>();			
			// compute video caching latency improvements			
			for (int i = 0; i < nCacheServers; i++) {
				System.out.println("FIND VIDEOS WORTH STORING - CACHE " + (i+1) + " (" + nCacheServers + ")");
				CacheServer cacheServer = cacheServers.get(i);
				ArrayList<Optimization> candidateVideos = new ArrayList<Optimization>();
				HashMap<Integer, Integer> videosPosition = new HashMap<Integer, Integer>();
				for (int idEndpoint = 0; idEndpoint < endpoints.size(); idEndpoint++) {
					System.out.println("CALCULATING RATING - ENDPOINT " + (idEndpoint+1) + " (" + endpoints.size() + ")");
					Endpoint e = endpoints.get(idEndpoint);
					if (e.latencyToCacheServers[cacheServer.idCache] > 0) {
						for (int j = 0; j < e.videosRequested.size(); j++) {
							Request videoRequested = e.videosRequested.get(j);
							long latencyGain;
							if (!satisfiedBy.containsKey(videoRequested)) {
								// if a rqst has no cache associated to it, then the latency gain is computed as
								// the improvement that the current cache allow to obtain wrt the data center
								latencyGain = (e.latencyToDataCenter - e.latencyToCacheServers[cacheServer.idCache]) * videoRequested.nRequests;
							} else {
								// if a rqst has cache associated to it, then the latency gain is computed as
								// the improvement that the current cache allow to obtain wrt to them	
								ArrayList<Integer> caches = satisfiedBy.get(videoRequested);
								int minLatency = e.latencyToCacheServers[caches.get(0)];
								for (int k = 1; k < caches.size(); k++) {
									int kLatency = e.latencyToCacheServers[caches.get(k)];
									if (minLatency > kLatency) {
										minLatency = kLatency;
									}
								}
								latencyGain = (minLatency - e.latencyToCacheServers[cacheServer.idCache]) * videoRequested.nRequests;
							}
							if (!videosPosition.containsKey(videoRequested.idVideo)) {	
								// add a new video to the candidates
								Optimization o = new Optimization();
								o.idVideo = videoRequested.idVideo;
								o.videoSize = videosSize[videoRequested.idVideo];
								o.rating = latencyGain;
								o.candidateTo.add(videoRequested);
								videosPosition.put(videoRequested.idVideo, candidateVideos.size());
								candidateVideos.add(o);
							} else {
								// increase the ranking of an existing candidate
								Integer pos = videosPosition.get(videoRequested.idVideo);
								Optimization o = candidateVideos.get(pos);
								o.rating += latencyGain;
								o.candidateTo.add(videoRequested);
							}												
						}
					}
				}
				// sort candidates videos based on the latency gain density
				System.out.println("SORT - CACHE " + (i+1) + " (" + nCacheServers + ")");
				Collections.sort(candidateVideos);
				// put videos in the cache if they fits in it
				System.out.println("FILL - CACHE " + (i+1) + " (" + nCacheServers + ")");
				for (int j = 0; j < candidateVideos.size(); j++) {
					Optimization o = candidateVideos.get(j);
					if (cacheServer.freeSize >= o.videoSize) {
						cacheServer.freeSize -= o.videoSize;
						cacheServer.listOfVideos.add(o.idVideo);
						// add to the related requests, the cache that satisfy it
						for (int k = 0; k < o.candidateTo.size(); k++) {
							Request request = o.candidateTo.get(k);
							if (!satisfiedBy.containsKey(request)) {
								ArrayList<Integer> caches = new ArrayList<Integer>();
								caches.add(new Integer(cacheServer.idCache));
								satisfiedBy.put(request, caches);
							} else {
								ArrayList<Integer> caches = satisfiedBy.get(request);
								caches.add(new Integer(cacheServer.idCache));  // the same cache cannot be added to the same request more than once for construction 
							}
						}						
					}
				}		
			}

			// count cache servers used
			int cacheSUsed = 0;
			for (int i = 0; i < cacheServers.size(); i++) {
				if (cacheServers.get(i).listOfVideos.size() > 0) {
					cacheSUsed++;
				}
			}

		    writer = new PrintWriter("C:\\Users\\Matt\\Documents\\Hash code\\Online-Qualification-Round-Problem-for-Google-Hash-Code-2017-Data-Sets\\"+FILENAME+".out", "UTF-8");
		    writer.println(cacheSUsed);

		    for (int i = 0; i < cacheServers.size(); i++) {
				CacheServer c = cacheServers.get(i);

				if (c.listOfVideos.size() > 0) {
					writer.println(i + " " + listToString(c.listOfVideos));
				}
			}
		    System.out.println("DONE");
			    
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)
					br.close();
				if (fr != null)
					fr.close();
				if (writer != null)
					writer.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
	}
}
