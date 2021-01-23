#echo without commonsense fakenews forecasting prediction task
#python -m mt_trainer \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenews_forecasting \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5

echo with commonsense fakenews forecasting prediction task
python -m mt_trainer \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge physical \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenews_forecasting_reliability \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5