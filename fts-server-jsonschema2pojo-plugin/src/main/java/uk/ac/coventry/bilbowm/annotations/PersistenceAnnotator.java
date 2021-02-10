package uk.ac.coventry.bilbowm.annotations;

import com.fasterxml.jackson.databind.JsonNode;
import com.sun.codemodel.JAnnotationUse;
import com.sun.codemodel.JDefinedClass;
import com.sun.codemodel.JFieldVar;
import org.jsonschema2pojo.AbstractAnnotator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.persistence.*;

import static uk.ac.coventry.bilbowm.annotations.PropertyNames.*;

public class PersistenceAnnotator extends AbstractAnnotator {

    private static final Logger LOGGER = LoggerFactory.getLogger(PersistenceAnnotator.class);

    @Override
    public void propertyInclusion(JDefinedClass clazz, JsonNode schema) {
        if (!schema.has(ANNOTATIONS)) {
            return;
        }
        LOGGER.info("Class is a javax entity: {}", schema.toString());
        annotatedClass(clazz, schema.get(ANNOTATIONS));
    }

    @Override
    public void propertyField(JFieldVar field, JDefinedClass clazz, String propertyName, JsonNode propertyNode) {
        super.propertyField(field, clazz, propertyName, propertyNode);
        if (!propertyNode.has(ANNOTATIONS)) {
            return;
        }
        LOGGER.info("Property \"{}\" is a DB table column", propertyName);
        annotateField(field, propertyNode.get(ANNOTATIONS), propertyName);
    }

    private void annotatedClass(JDefinedClass clazz, JsonNode annotationsNode) {
        if (clazz.annotations().stream()
                .map(a -> a.getAnnotationClass().toString())
                .anyMatch(n -> n.contains("(Entity)"))) {
            LOGGER.info("Entity annotation already exists on class");
            return;
        }
        if (!annotationsNode.isObject()) {
            clazz.annotate(Entity.class);
            return;
        }

        LOGGER.info("Cass \"{}\" is a DB entity. Adding @Entity annotation", clazz);
        if (annotationsNode.has(A_TABLE)) {
            final JAnnotationUse table = clazz.annotate(Table.class);
            final JsonNode tableNode = annotationsNode.get(A_TABLE);
            if (tableNode.has("name")) {
                table.param("name", tableNode.get("name").asText());
            }
        }

        final JAnnotationUse entity = clazz.annotate(Entity.class);
        if (annotationsNode.has(A_ENTITY) && annotationsNode.get(A_ENTITY).isObject()) {
            final JsonNode entityNode = annotationsNode.get(A_ENTITY);
            if (entityNode.has("name")) {
                entity.param("name", entityNode.get("name").asText());
            }
        }
    }

    private void annotateField(JFieldVar field, JsonNode annotationsNode, String propertyName) {
        if (annotationsNode.isBoolean()) {
            field.annotate(Column.class);
            return;
        }
        if (annotationsNode.has(A_TRANSIENT)) {
            field.annotate(Transient.class);
            return;
        }
        final JAnnotationUse annotation = field.annotate(Column.class);
        final JsonNode column = annotationsNode.get(A_COLUMN);
        if (column != null && column.isObject()) {
            addColumnProps(annotation, column);
        }
        if (annotationsNode.has(A_ID)) {
            LOGGER.info("Property \"{}\" is a primary key. Adding @Id annotation", propertyName);
            field.annotate(Id.class);
        }
    }

    private void addColumnProps(JAnnotationUse annotation, JsonNode col) {
        if (col.has("name")) {
            annotation.param("name", col.get("name").textValue());
        }
        if (col.has("unique")) {
            annotation.param("unique", col.get("unique").asBoolean());
        }
    }
}
