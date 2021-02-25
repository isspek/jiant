#echo Extracting concepts from fakenewscorpus
#python -m commonsense.utils \
#--source_dir trained_models/fakenewscorpus
#--extract \
#--dtype news

#echo Extracting concepts from forecasting_cind_reliability
#python -m commonsense.utils \
#--source_dir trained_models/forecasting_cind_reliability
#--extract \
#--dtype news
#
#echo Extracting concepts from nela
#python -m commonsense.utils \
#--source_dir trained_models/nela
#--extract \
#--dtype news
#
#echo Extracting concepts from unseen_cind_reliability
#python -m commonsense.utils \
#--source_dir trained_models/unseen_cind_reliability \
#--extract \
#--dtype news

#echo Extracting concepts from commonsenseqa
#python -m commonsense.utils \
#--source_dir ../trained_models/Commonsenseqa \
#--extract \
#--dtype commonsenseqa

echo Computing similarities on forecasting_cind_reliability
python -m commonsense.utils \
--target_dir ../trained_models/Commonsenseqa \
--source_dir ../trained_models/forecasting_cind_reliability \
--calculate \
--metric jaccard

echo Computing similarities on unseen_cind_reliability
python -m commonsense.utils \
--target_dir ../trained_models/Commonsenseqa \
--source_dir ../trained_models/unseen_cind_reliability \
--calculate \
--metric jaccard

echo Computing similarities on nela
python -m commonsense.utils \
--target_dir ../trained_models/Commonsenseqa \
--source_dir ../trained_models/nela \
--calculate \
--metric jaccard

echo Computing similarities on fakenewscorpus
python -m commonsense.utils \
--target_dir ../trained_models/Commonsenseqa \
--source_dir ../trained_models/fakenewscorpus \
--calculate \
--metric jaccard