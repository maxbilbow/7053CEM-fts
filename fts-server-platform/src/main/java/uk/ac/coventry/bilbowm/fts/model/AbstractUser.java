package uk.ac.coventry.bilbowm.fts.model;

import javax.persistence.*;


public abstract class AbstractUser {

    public abstract String getUsername();

    public abstract String getContract();

    @Transient
    public Contract constructContractObject() {
        return Contract.newContract(getUsername(), getContract());
    }
}
