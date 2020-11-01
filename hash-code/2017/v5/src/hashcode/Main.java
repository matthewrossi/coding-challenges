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
			int nEndpoints     = Integer.parseInt(line[1]);
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
			ArrayList<Endpoint> endpoints = new ArrayList<Endpoint>(nEndpoints);			
			for (int idEndpoint = 0; idEndpoint < nEndpoints; idEndpoint++) {				
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
			}
			
			// Not feasable for kittens due to memory bounds
			ArrayList<Optimization> requests = new ArrayList<Optimization>();
			HashMap<String, Optimization> requestByIDs = new HashMap<String, Optimization>();
			HashMap<Integer, ArrayList<Optimization>> requestByVideo = new HashMap<Integer, ArrayList<Optimization>>();
			for (int idEndpoint = 0; idEndpoint < nEndpoints; idEndpoint++) {
				System.out.println("CALCULATING RATING - ENDPOINT " + (idEndpoint+1) + " (" + endpoints.size() + ")");
				Endpoint endpoint = endpoints.get(idEndpoint);
				for (int i = 0; i < endpoint.videosRequested.size(); i++) {
					Request videoRequested = endpoint.videosRequested.get(i);
					for (int idCache = 0; idCache < nCacheServers; idCache++) {
						if (endpoint.latencyToCacheServers[idCache] > 0) {
							String key = new String(""+idCache+videoRequested.idVideo);
							if (!requestByIDs.containsKey(key)) {
								Optimization o = new Optimization(nEndpoints);
								o.idCache = idCache;
								o.idVideo = videoRequested.idVideo;
								o.videoSize = videosSize[videoRequested.idVideo];
								o.rating = (endpoint.latencyToDataCenter - endpoint.latencyToCacheServers[idCache]) * videoRequested.nRequests;
								o.endpointsNumberOfRequest[idEndpoint] = videoRequested.nRequests;
								requests.add(o); 
								requestByIDs.put(key, o);
								if (!requestByVideo.containsKey(videoRequested.idVideo)) {
									ArrayList<Optimization> os = new ArrayList<Optimization>();
									os.add(o);
									requestByVideo.put(videoRequested.idVideo, os);
								} else {
									ArrayList<Optimization> os = requestByVideo.get(videoRequested.idVideo);
									os.add(o);
								}
							} else {  // a new endpoint asks for the same video to be store at the same cache
								Optimization o = requestByIDs.get(key);
								o.rating += (endpoint.latencyToDataCenter - endpoint.latencyToCacheServers[idCache]) * videoRequested.nRequests;
								o.endpointsNumberOfRequest[idEndpoint] = videoRequested.nRequests;
							}
						}
					}
				}
			}
			
			// finding the max at each cycle should be more performing
			System.out.println("SORT REQUESTS");
			Collections.sort(requests);
			
			// create cache servers
			ArrayList<CacheServer> cacheServers = new ArrayList<CacheServer>();
			for (int idCache = 0; idCache<nCacheServers; idCache++) {
				cacheServers.add(new CacheServer(idCache, cacheSize));
			}
			
			int solvedRequests = 0, totRequests = requests.size();
			while (requests.size() > 0) {
				System.out.println("SATISFYING REQUESTS " + (solvedRequests+1) + " (" + totRequests + ")");
				Optimization o = requests.get(0);
				CacheServer cacheServer = cacheServers.get(o.idCache);
				ArrayList<Optimization> possiblyRelatedRequests = requestByVideo.get(o.idVideo);
				if (cacheServer.freeSize >= o.videoSize) {
					cacheServer.freeSize -= o.videoSize;
					cacheServer.listOfVideos.add(o.idVideo);
					// propagate changes and based on that reposition the requests
					for (int idEnpoint = 0; idEnpoint < nEndpoints; idEnpoint++) {
						Endpoint endpoint = endpoints.get(idEnpoint);
						if (o.endpointsNumberOfRequest[idEnpoint] > 0) {
							long achivedLatencyGain = (endpoint.latencyToDataCenter - endpoint.latencyToCacheServers[o.idCache]) * o.endpointsNumberOfRequest[idEnpoint];
							for (int i = 0; i < possiblyRelatedRequests.size(); i++) {
								Optimization possiblyRelatedRequest = possiblyRelatedRequests.get(i);
								if (possiblyRelatedRequest.endpointsNumberOfRequest[idEnpoint] > 0 && o != possiblyRelatedRequest) {
									// the request is actually related
									long latencyGain = (endpoint.latencyToDataCenter - endpoint.latencyToCacheServers[possiblyRelatedRequest.idCache]) * possiblyRelatedRequest.endpointsNumberOfRequest[idEnpoint];
									if (achivedLatencyGain > latencyGain) {
										achivedLatencyGain = latencyGain;
									}
									// remove the request
									requests.remove(possiblyRelatedRequest);
									// change its latency gain
									possiblyRelatedRequest.rating -= achivedLatencyGain;
									// add the request at the right spot
									int new_pos = Collections.binarySearch(requests, possiblyRelatedRequest);
									if (new_pos < 0) {
										new_pos = -new_pos - 1;
									}
									requests.add(new_pos, possiblyRelatedRequest);
								}
							}
						}
					}
				}
				requests.remove(0);
				possiblyRelatedRequests.remove(o);
				solvedRequests++;
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
