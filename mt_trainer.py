from jiant.proj.simple import runscript as run
import jiant.scripts.download_data.runscript as downloader
import jiant.scripts.download_data.dl_datasets.files_tasks as files_tasks_download
import jiant.proj.main.tokenize_and_cache as tokenize_and_cache
import jiant.shared.caching as caching
import jiant.proj.main.scripts.configurator as configurator
import jiant.utils.python.io as py_io
import jiant.utils.display as display
import jiant.proj.main.export_model as export_model
import os
import jiant.proj.main.runscript as main_runscript
import argparse

DATASETS = {
    'fakenews_unseen': 'unseen_cind',
    'nela_unseen': 'nela',
    'fakenews_forecasting': 'forecasting_cind',
    'fakenews_forecasting_reliability': 'forecasting_cind_reliability',
    'fakenews_unseen_reliability': 'unseen_cind_reliability',
    'fakenewscorpus': 'fakenewscorpus'
}

COMMONSENSE_KNOWLEDGE = {
    'social': 'socialiqa',
    'general': 'commonsenseqa',
    'physical': 'piqa',

}

SATIRE_TASKS = {
    'nela_unseen': 'nela_satire',
    'fakenews_forecasting': 'forecasting_cind_satire',
    'fakenews_forecasting_reliability': 'forecasting_cind_satire',
    'fakenews_unseen_reliability': 'unseen_cind_satire',
    'fakenewscorpus': 'fakenewscorpus_satire'
}


def run_mtl(args):
    fold = args.fold
    random_seed = args.random_seed
    learning_rate = args.learning_rate
    pretrained_model = args.pretrained_model
    use_commonsense_knowledge = args.use_commonsense_knowledge
    train_batch_size = args.train_batch_size
    eval_batch_size = args.eval_batch_size
    task_name = f'{args.task_name}_{fold}' if fold else args.task_name
    epochs = args.epochs
    use_satire = args.use_satire
    commonsense_type = None
    if use_commonsense_knowledge:
        commonsense_type = COMMONSENSE_KNOWLEDGE[args.commonsenseknowledge]
        exp_name = f'../trained_models/{args.task_name}_{fold}_{commonsense_type}'
    else:
        exp_name = f'../trained_models/{args.task_name}_{fold}'

    task_data_path = f'../trained_models/{DATASETS[args.task_name]}'
    task_config_path = f'../trained_models/{DATASETS[args.task_name]}/configs/{task_name}_config.json'
    export_model.lookup_and_export_model(
        model_type=pretrained_model,
        output_base_path=f"../models/{pretrained_model}",
    )
    files_tasks_download.download_task_data_and_write_config(task_name, task_data_path, task_config_path)
    tokenize_and_cache.main(tokenize_and_cache.RunConfiguration(
        task_config_path=task_config_path,
        model_type=pretrained_model,
        model_tokenizer_path=f"../models/{pretrained_model}/tokenizer",
        output_dir=f'{exp_name}/cache/{task_name}',
        phases=['train', 'val', 'test'],
        max_seq_length=args.task_max_len,
    ))

    task_names = []
    task_names.append(task_name)

    if use_commonsense_knowledge:
        downloader.download_data([commonsense_type], f"{task_data_path}")
        tokenize_and_cache.main(tokenize_and_cache.RunConfiguration(
            task_config_path=f"{task_data_path}/configs/{commonsense_type}_config.json",
            model_type=pretrained_model,
            model_tokenizer_path=f"../models/{pretrained_model}/tokenizer",
            output_dir=f'{exp_name}/cache/{commonsense_type}',
            phases=['train', 'val'] if commonsense_type == 'socialiqa' else ['train', 'val', 'test'],
            max_seq_length=args.commonsense_max_len,
        ))
        task_names.append(commonsense_type)

    if use_satire:
        satire_task_name = SATIRE_TASKS[args.task_name]
        satire_task_name = f'{satire_task_name}_{fold}' if fold else satire_task_name
        satire_task_data_path = f'../trained_models/{SATIRE_TASKS[args.task_name]}'

        files_tasks_download.download_task_data_and_write_config(satire_task_name, satire_task_data_path,
                                                                 f"{task_data_path}/configs/{satire_task_name}_config.json")

        tokenize_and_cache.main(tokenize_and_cache.RunConfiguration(
            task_config_path=f"{task_data_path}/configs/{satire_task_name}_config.json",
            model_type=pretrained_model,
            model_tokenizer_path=f"../models/{pretrained_model}/tokenizer",
            output_dir=f'{exp_name}/cache/{satire_task_name}',
            phases=['train', 'val', 'test'],
            max_seq_length=args.satire_max_len,
        ))
        task_names.append(satire_task_name)

    jiant_run_config = configurator.SimpleAPIMultiTaskConfigurator(
        task_config_base_path=f"{task_data_path}/configs",
        task_cache_base_path=f'{exp_name}/cache/',
        train_task_name_list=task_names,
        val_task_name_list=task_names,
        test_task_name_list=task_names[0] if commonsense_type == 'socialiqa' else task_names,
        train_batch_size=train_batch_size,
        eval_batch_size=eval_batch_size,
        epochs=epochs,
        num_gpus=1,
    ).create_config()
    os.makedirs(f'{exp_name}/run_configs/', exist_ok=True)
    py_io.write_json(jiant_run_config, f'{exp_name}/run_configs/jiant_run_config.json')
    display.show_json(jiant_run_config)
    run_args = main_runscript.RunConfiguration(
        jiant_task_container_config_path=f'{exp_name}/run_configs/jiant_run_config.json',
        output_dir=f'{exp_name}/runs/',
        model_type=pretrained_model,
        model_tokenizer_path=f"../models/{pretrained_model}/tokenizer",
        model_path=f"../models/{pretrained_model}/model/{pretrained_model}.p",
        model_config_path=f"../models/{pretrained_model}/model/{pretrained_model}.json",
        learning_rate=learning_rate,
        seed=random_seed,
        do_train=True,
        do_val=True,
        write_test_preds=True,
        force_overwrite=True,
        write_val_preds=True,
        no_cuda=False,
    )
    main_runscript.run_loop(run_args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fold', type=int)
    parser.add_argument('--random_seed', type=int)
    parser.add_argument('--learning_rate', type=float)
    parser.add_argument('--pretrained_model', type=str)
    parser.add_argument('--use_commonsense_knowledge', action='store_true')
    parser.add_argument('--use_satire', action='store_true')
    parser.add_argument('--commonsenseknowledge', choices=['general', 'social', 'physical'])
    parser.add_argument('--use_gpu', action='store_true')
    parser.add_argument('--commonsense_max_len', type=int)
    parser.add_argument('--task_max_len', type=int)
    parser.add_argument('--satire_max_len', type=int)
    parser.add_argument('--train_batch_size', type=int)
    parser.add_argument('--eval_batch_size', type=int)
    parser.add_argument('--task_name', type=str,
                        choices=["fakenews_unseen", "claimbuster", "nela_unseen", "fakenews_forecasting",
                                 "fakenews_forecasting_reliability", "fakenews_unseen_reliability", "fakenewscorpus"])
    parser.add_argument('--epochs', type=int)
    args = parser.parse_args()
    run_mtl(args)
