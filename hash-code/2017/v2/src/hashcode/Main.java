package hashcode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
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

		try {

			fr = new FileReader("C:\\Users\\l.perico\\Downloads\\"+FILENAME+".in");
			br = new BufferedReader(fr);

			// read first line
			String[] firstLine = br.readLine().split(" ");

			int nVideos   = Integer.parseInt(firstLine[0]);
			int nEndpoint = Integer.parseInt(firstLine[1]);
			int nRequests = Integer.parseInt(firstLine[2]);
			int nCacheS   = Integer.parseInt(firstLine[3]);
			int cacheSize = Integer.parseInt(firstLine[4]);

			// read videos line
			String[] videosLine = br.readLine().split(" ");
			int[] videosSize = new int[nVideos];
			for(int i=0; i<videosLine.length; i++) {
				videosSize[i] = Integer.parseInt(videosLine[i]);
			}

			// save all endpoints
			ArrayList<Endpoint> endpoints = new ArrayList<Endpoint>(nEndpoint);
			for (int idEndpoint=0; idEndpoint<nEndpoint; idEndpoint++) {
				String[] l = br.readLine().split(" ");
				Endpoint e = new Endpoint();
				e.idEndpoint          = idEndpoint;
				e.latencyToDataCenter = Integer.parseInt(l[0]);
				e.nCacheS			  = Integer.parseInt(l[1]);

				for (int j=0; j<e.nCacheS; j++) {
					l = br.readLine().split(" ");

					EndpointCacheServer ecs  = new EndpointCacheServer();
					ecs.cacheServerId        = Integer.parseInt(l[0]);
					ecs.cacheEndpointLatency = Integer.parseInt(l[1]);

					e.cacheServers.add(ecs);
				}

				if (e.nCacheS > 0) {
					Collections.sort(e.cacheServers);
				}

				endpoints.add(e);
			}

			// save all requests
			for (int i=0; i<nRequests; i++) {
				String[] l = br.readLine().split(" ");

				Request r = new Request();
				r.idVideo = Integer.parseInt(l[0]);
				r.nRequests = Integer.parseInt(l[2]);

				Endpoint e = endpoints.get(Integer.parseInt(l[1]));
				e.videosRequested.add(r);
			}

			// calculate request priorities
			System.out.println("START CALCULATING RATINGS");
			for (int i=0; i<endpoints.size(); i++) {
				System.out.println("CALCULATING RATING - ENDPOINT " + (i +1) + " (" + endpoints.size() + ")");
				Endpoint e = endpoints.get(i);
				ArrayList<Request> videosRequested = e.videosRequested;

				for (int j=0; j<videosRequested.size(); j++) {
					int idVideo = videosRequested.get(j).idVideo;

					if (e.cacheServers != null && e.cacheServers.size() > 0) {
						long rating = e.latencyToDataCenter  * e.videosRequested.get(j).nRequests / e.nCacheS;

						Optimization o = new Optimization();
						o.idVideo      = idVideo;
						o.videoSize    = videosSize[idVideo];
						o.rating       = rating;
						o.endpoint     = i;
						o.nRequests    = videosRequested.get(j).nRequests;

						e.rating += rating;

						e.requestPriorities.add(o);
					}
				}

				Collections.sort(e.requestPriorities);
			}

			Collections.sort(endpoints);

			ArrayList<CacheServer> cacheServers = new ArrayList<CacheServer>();
			for (int i=0; i<nCacheS; i++) {
				cacheServers.add(new CacheServer(cacheSize));
			}

			for (int i=0; i<endpoints.size(); i++) {
				System.out.println("CALCULATING LIST OF VIDEOS - ENDPOINT " + (i +1) + " (" + endpoints.size() + ")");
				Endpoint e = endpoints.get(i);

				for (int k=0; k<e.requestPriorities.size(); k++) {
					Optimization o = e.requestPriorities.get(k);

					CacheServer c;

					while (o.attempts < e.cacheServers.size()) {
						c = cacheServers.get(e.cacheServers.get(o.attempts).cacheServerId);

						if (c.listOfVideos.contains(o.idVideo)) {
							break;
						}

						if (c.freeSize >= o.videoSize) {
							c.freeSize -= o.videoSize;
							c.listOfVideos.add(o.idVideo);
							break;
						} else {
							o.attempts++;
						}
					}
				}
			}

			// count cache servers used
			int cacheSUsed = 0;
			for (int i=0; i<cacheServers.size(); i++) {
				if (cacheServers.get(i).listOfVideos.size() > 0) {
					cacheSUsed++;
				}
			}

			try{
			    PrintWriter writer = new PrintWriter("C:\\Users\\l.perico\\Downloads\\"+FILENAME+".out", "UTF-8");
			    writer.println(cacheSUsed);

			    for (int i=0; i<cacheServers.size(); i++) {
					CacheServer c = cacheServers.get(i);

					if (c.listOfVideos.size() > 0) {
						writer.println(i + " " + listToString(c.listOfVideos));
					}
				}

			    writer.close();

			    System.out.println("DONE");
			} catch (IOException e) {
			   // do something
			}
		} catch (IOException e) {

			e.printStackTrace();

		} finally {

			try {

				if (br != null)
					br.close();

				if (fr != null)
					fr.close();

			} catch (IOException ex) {

				ex.printStackTrace();

			}
		}
	}
}
