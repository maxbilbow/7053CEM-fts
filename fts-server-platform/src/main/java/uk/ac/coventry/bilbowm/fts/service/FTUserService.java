package uk.ac.coventry.bilbowm.fts.service;

import uk.ac.coventry.bilbowm.fts.model.generated.FTUser;
import uk.ac.coventry.bilbowm.fts.repository.FTUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
@Transactional
public class FTUserService {

    private final FTUserRepository repository;

    @Autowired
    public FTUserService(FTUserRepository repository) {
        this.repository = repository;
    }

    public List<FTUser> listAll() {
        return repository.findAll();
    }
}
