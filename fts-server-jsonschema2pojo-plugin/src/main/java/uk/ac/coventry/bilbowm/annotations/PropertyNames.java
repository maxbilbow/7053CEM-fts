package uk.ac.coventry.bilbowm.annotations;

import javax.persistence.*;

class PropertyNames {
    static final String ANNOTATIONS = "javaxAnnotations";
    static final String A_COLUMN = "@" + Column.class.getSimpleName();
    static final String A_TRANSIENT = "@" + Transient.class.getSimpleName();
    static final String A_ID = "@" + Id.class.getSimpleName();
    static final String A_ENTITY = "@" + Entity.class.getSimpleName();
    static final String A_TABLE = "@" + Table.class.getSimpleName();
}
