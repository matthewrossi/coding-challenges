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
	private static final String FILENAME = "videos_worth_spreading";
//	private static final String FILENAME = "kittens";

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

			// read endpoints info
			ArrayList<Endpoint> endpoints = new ArrayList<Endpoint>(nEndpoint);			
			for (int idEndpoint = 0; idEndpoint < nEndpoint; idEndpoint++) {				
				line = br.readLine().split(" ");
				Endpoint e = new Endpoint(nCacheServers);
				e.latencyToDataCenter = Integer.parseInt(line[0]);
				e.nCaches = Integer.parseInt(line[1]);
				for (int j = 0; j < e.nCaches; j++) {					
					line = br.readLine().split(" ");
					int cacheServerId = Integer.parseInt(line[0]);
					e.latencyToCacheServers[cacheServerId] = Integer.parseInt(line[1]);
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
			}
			
			// compute requests ranking
			HashMap<String, Integer> requestedVideoToCache = new HashMap<String, Integer>();
			ArrayList<Optimization> requestPriorities = new ArrayList<Optimization>();
			System.out.println("START CALCULATING RATINGS");
			for (int idEndpoint = 0; idEndpoint < endpoints.size(); idEndpoint++) {
				System.out.println("CALCULATING RATING - ENDPOINT " + (idEndpoint+1) + " (" + endpoints.size() + ")");
				Endpoint e = endpoints.get(idEndpoint);
				ArrayList<Request> videosRequested = e.videosRequested;
				for (int i = 0; i < videosRequested.size(); i++) {
					Request request = videosRequested.get(i);
					
					// create a request per connected cache
					ArrayList<Optimization> relatedRequests = new ArrayList<Optimization>();
					for (int idCache = 0; idCache < nCacheServers; idCache++){
						if (e.latencyToCacheServers[idCache] > 0) {
							long rating = (e.latencyToDataCenter - e.latencyToCacheServers[idCache]) * e.videosRequested.get(i).nRequests;
							String key = new String(""+request.idVideo+idCache);
							
							// check if the same request coming from another endpoint exists
							if (!requestedVideoToCache.containsKey(key)) {
								requestedVideoToCache.put(key, requestPriorities.size());
								Optimization o = new Optimization();
								o.idCache      = idCache;
								o.idVideo      = request.idVideo;
								o.idEndpoint   = idEndpoint;
								o.nRequests    = request.nRequests;
								o.videoSize    = videosSize[request.idVideo];
								o.rating       = rating;
								relatedRequests.add(o);
								requestPriorities.add(o);
							} else {
								Integer pos = requestedVideoToCache.get(key);
								Optimization o = requestPriorities.get(pos);
								o.rating += rating;
								relatedRequests.add(o); // TODO: not sure if this is right
							}
						}
					}
					
					// add bindings between the same request of the same endpoint to =/= caches
					for (int j = 0; j < relatedRequests.size(); j++) {
						ArrayList<Optimization> clone = new ArrayList<Optimization>(relatedRequests);
						clone.remove(j);
						relatedRequests.get(j).relatedRequests.addAll(clone);
					}
				}				
			}

			System.out.println("START SORTING REQUESTS");
			Collections.sort(requestPriorities);
			System.out.println("REQUESTS SORTED");

			ArrayList<CacheServer> cacheServers = new ArrayList<CacheServer>();
			for (int i=0; i<nCacheServers; i++) {
				cacheServers.add(new CacheServer(cacheSize));
			}

			System.out.println("START ASSIGNING VIDEOS");
			for (int i = 0; i < requestPriorities.size(); i++) {  // TODO: remove already satisfied requests from its relatives
				System.out.println("CALCULATING LIST OF VIDEOS - REQUEST " + (i+1) + " ("  + requestPriorities.size() + ")");
				Optimization o = requestPriorities.get(i);
				CacheServer c = cacheServers.get(o.idCache);				
				if (!c.listOfVideos.contains(o.idVideo)) {	// TODO: handle the video size on the single cache server, so maybe more complex data structure	(as a knapsack problem)					
					if (c.freeSize >= o.videoSize) {
						c.freeSize -= o.videoSize;
						c.listOfVideos.add(o.idVideo);
						// handle related requests relation
						for (int j = 0; j < o.relatedRequests.size(); j++) {
							Optimization relatedRequest = o.relatedRequests.get(j);
							relatedRequest.relatedRequests.remove(o);  // remove the satisfied requests from the related ones
							int old_pos = Collections.binarySearch(requestPriorities, relatedRequest);
							requestPriorities.remove(old_pos);
							Endpoint endpoint = endpoints.get(relatedRequest.idEndpoint);
							long rating = (endpoint.latencyToDataCenter - endpoint.latencyToCacheServers[o.idCache]) * relatedRequest.nRequests;
							relatedRequest.rating -= rating;  // reduce the improvement the related request has based on the improvement accomplished
							int new_pos = -Collections.binarySearch(requestPriorities, relatedRequest) - 1;  // TODO: can exist a = obj??
							if (new_pos < 0)
								System.out.println(j); // j == 4
							requestPriorities.add(new_pos, relatedRequest);
						}
					}
				}
			}
			System.out.println("VIDEOS ASSIGNED");

			// count cache servers used
			int cacheSUsed = 0;
			for (int i=0; i<cacheServers.size(); i++) {
				if (cacheServers.get(i).listOfVideos.size() > 0) {
					cacheSUsed++;
				}
			}

		    writer = new PrintWriter("C:\\Users\\Matt\\Documents\\Hash code\\Online-Qualification-Round-Problem-for-Google-Hash-Code-2017-Data-Sets\\"+FILENAME+".out", "UTF-8");
		    writer.println(cacheSUsed);

		    for (int i=0; i<cacheServers.size(); i++) {
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
