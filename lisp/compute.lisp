(start-idyom)

(idyom-db:initialise-database)
(idyom-db:import-data :mid "TRAINFOLDER" "Train" TRAINID)
(idyom-db:import-data :mid "TESTFOLDER" "Test" TESTID)
(idyom:idyom TESTID '(cpitch) '(cpitch) :models :both :pretraining-ids '(TRAINID) :k 1 :detail 3 :output-path DATAOUTPUT :overwrite t)

(quit)
