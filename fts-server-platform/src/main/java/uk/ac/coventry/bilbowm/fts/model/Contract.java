package uk.ac.coventry.bilbowm.fts.model;

public interface Contract {

    String name();

    String contract();

    static Contract newContract(String name, String contract) {
        return new Contract() {
            @Override
            public String name() {
                return name;
            }

            @Override
            public String contract() {
                return contract;
            }
        };
    }
}

