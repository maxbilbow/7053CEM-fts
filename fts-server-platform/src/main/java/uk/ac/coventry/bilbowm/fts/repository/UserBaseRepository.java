package uk.ac.coventry.bilbowm.fts.repository;

import uk.ac.coventry.bilbowm.fts.model.AbstractUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserBaseRepository<T extends AbstractUser> extends JpaRepository<T, String> {

    void deleteByUsername(String username);
}
