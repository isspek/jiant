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