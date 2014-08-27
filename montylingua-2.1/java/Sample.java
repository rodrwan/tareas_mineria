import montylingua.JMontyLingua; // loads namespace

public class Sample {
	public static JMontyLingua j = new JMontyLingua();

	public static void main(String[] args) {
		Sample t = new Sample();
		String text = "California's officials were optimistic Monday about the full containment of the devastating wildfires that held 27,000 US residents displaced in southern California. All fires were expected to be surrounded by Tuesday, if not by Monday evening, said Andrea Tuttle, director of the California Department of Forestry and Fire Protection. Continued cooler weather associated with the rain, snow and freezing temperatures at night helped exhausted firefighters claimvictory over raging wildfires in the past days, Tuttle said, adding that \"the weather continues to be healthy for us.\"     About half of the 14,000 firefighters remained in the front tocombat forest fires in an area ranging from San Diego to San Bernardion in southern California till Monday. The Old Fire, the last of the wildfires that once threatened the populous ski resort of Lake Big Bear in the San Bernardino Mountains, was 83 percent contained. Fire engine crews sprayed smoky spots in some charred areas, and utility crews restrung lines to restore power. More than 27,000 people of about 80,000 evacuees remained displaced, most of whom are from the Lake Arrowhead area, where all roads west of state Highway 18 and state Highway 38 remained closed due to a threat of mudslides. Other areas closed to residents Monday include Crestline, Lake Gregory, Twin Peaks, Rimforest, Blue Jay, Cedar Glen, Skyforest, Running Springs, Arrowbear Lake, and Green Valley Lake.";
		System.out.println("\n\n-------------- Tags text -----------\n\n");
		System.out.println(j.tag_text(text));
		System.out.println("\n\n-------------- Chunks text -----------\n\n");
		System.out.println(j.chunk_text(text));
		System.out.println("\n\n-------------- Lemmatises text -----------\n\n");
		System.out.println(j.lemmatise_text(text));
		System.out.println("\n\n-------------- Jists text (Verb-Subj-Obj-Obj) -----------\n\n");
		System.out.println(j.jist_predicates(text));

	}
}