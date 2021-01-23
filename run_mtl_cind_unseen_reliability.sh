#echo without commonsense nela fakenews_unseen_reliability task for fold 1
#python -m mt_trainer \
#--fold 1 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenewscorpus \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability task for fold 2
#python -m mt_trainer \
#--fold 2 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenewscorpus \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5

#echo without commonsense fakenews_unseen_reliability task for fold 3
#python -m mt_trainer \
#--fold 3 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenewscorpus \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability task for fold 4
#python -m mt_trainer \
#--fold 4 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenewscorpus \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability for fold 5
#python -m mt_trainer \
#--fold 5 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenewscorpus \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 1
python -m mt_trainer \
--fold 1 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 2
python -m mt_trainer \
--fold 2 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 3
python -m mt_trainer \
--fold 3 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 4
python -m mt_trainer \
--fold 4 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 5
python -m mt_trainer \
--fold 5 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 1
python -m mt_trainer \
--fold 1 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge physical \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 2
python -m mt_trainer \
--fold 2 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge physical \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 3
python -m mt_trainer \
--fold 3 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge physical \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 4
python -m mt_trainer \
--fold 4 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge physical \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 5
python -m mt_trainer \
--fold 5 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge physical \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 1
python -m mt_trainer \
--fold 1 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 2
python -m mt_trainer \
--fold 2 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 3
python -m mt_trainer \
--fold 3 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 4
python -m mt_trainer \
--fold 4 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

echo commonsense fakenews_unseen_reliability for fold 5
python -m mt_trainer \
--fold 5 \
--random_seed 42 \
--pretrained_model bert-base-uncased \
--use_commonsense_knowledge \
--commonsenseknowledge general \
--commonsense_max_len 128 \
--task_max_len 300 \
--train_batch_size 4 \
--eval_batch_size 1 \
--task_name fakenewscorpus \
--epochs 3 \
--use_gpu \
--learning_rate 2e-5

#echo without commonsense nela fakenews_unseen_reliability task for fold 1
#python -m mt_trainer \
#--fold 1 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name nela_unseen \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability task for fold 2
#python -m mt_trainer \
#--fold 2 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name nela_unseen \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability task for fold 3
#python -m mt_trainer \
#--fold 3 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name nela_unseen \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability task for fold 4
#python -m mt_trainer \
#--fold 4 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name nela_unseen \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo without commonsense fakenews_unseen_reliability for fold 5
#python -m mt_trainer \
#--fold 5 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name nela_unseen \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo commonsense fakenews_unseen_reliability for fold 1
#python -m mt_trainer \
#--fold 1 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--use_commonsense_knowledge \
#--commonsenseknowledge physical \
#--commonsense_max_len 128 \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenews_unseen_reliability \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo commonsense fakenews_unseen_reliability for fold 2
#python -m mt_trainer \
#--fold 2 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--use_commonsense_knowledge \
#--commonsenseknowledge physical \
#--commonsense_max_len 128 \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenews_unseen_reliability \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo commonsense fakenews_unseen_reliability for fold 3
#python -m mt_trainer \
#--fold 3 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--use_commonsense_knowledge \
#--commonsenseknowledge physical \
#--commonsense_max_len 128 \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenews_unseen_reliability \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo commonsense fakenews_unseen_reliability for fold 4
#python -m mt_trainer \
#--fold 4 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--use_commonsense_knowledge \
#--commonsenseknowledge physical \
#--commonsense_max_len 128 \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenews_unseen_reliability \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5
#
#echo commonsense fakenews_unseen_reliability for fold 5
#python -m mt_trainer \
#--fold 5 \
#--random_seed 42 \
#--pretrained_model bert-base-uncased \
#--use_commonsense_knowledge \
#--commonsenseknowledge physical \
#--commonsense_max_len 128 \
#--task_max_len 300 \
#--train_batch_size 4 \
#--eval_batch_size 1 \
#--task_name fakenews_unseen_reliability \
#--epochs 3 \
#--use_gpu \
#--learning_rate 2e-5