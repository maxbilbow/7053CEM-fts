package uk.ac.coventry.bilbowm.fts.newfangled;

public class TestingStuff {
    static boolean TEXT_BLOCK;

    public Object test(Object o) {
        if (o instanceof String) {
            return switch ((String) o) {
                case "A", "B", "C" -> "BOOM";
                default -> {
                    System.out.println("default");
                    yield null;
                }
            };
        }
       else if (TEXT_BLOCK){
            return """
                    Balls!
                    ksdoa
                    """;
        } else {
            return null;
        }
    }
    strictfp float i(){
        return 0.0199990f;
    }


}