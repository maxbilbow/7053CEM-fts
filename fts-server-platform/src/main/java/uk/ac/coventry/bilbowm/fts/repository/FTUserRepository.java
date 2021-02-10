package uk.ac.coventry.bilbowm.fts.repository;

import org.springframework.stereotype.Repository;
import uk.ac.coventry.bilbowm.fts.model.generated.FTUser;

@Repository
public interface FTUserRepository extends UserBaseRepository<FTUser> {

    void deleteByUsername(String username);
}
