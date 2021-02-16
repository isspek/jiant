# Directly download tasks when not available in HF Datasets, or HF Datasets version
#   is not suitable
SQUAD_TASKS = {"squad_v1", "squad_v2"}
DIRECT_SUPERGLUE_TASKS_TO_DATA_URLS = {
    "wsc": f"https://dl.fbaipublicfiles.com/glue/superglue/data/v2/WSC.zip",
    "multirc": f"https://dl.fbaipublicfiles.com/glue/superglue/data/v2/MultiRC.zip",
    "record": f"https://dl.fbaipublicfiles.com/glue/superglue/data/v2/ReCoRD.zip",
}

FAKENEWS_TASKS = {"fakenews_forecasting", "fakenews_unseen_1", "fakenews_unseen_2", "fakenews_unseen_3",
                  "fakenews_unseen_4", "fakenews_unseen_5",
                  "nela_unseen_1", "nela_unseen_2", "nela_unseen_3",
                  "nela_unseen_4", "nela_unseen_5", "fakenews_forecasting_reliability",
                  "fakenews_unseen_reliability_1", "fakenews_unseen_reliability_2", "fakenews_unseen_reliability_3",
                  "fakenews_unseen_reliability_4", "fakenews_unseen_reliability_5",
                  "fakenewscorpus_1", "fakenewscorpus_2", "fakenewscorpus_3", "fakenewscorpus_4", "fakenewscorpus_5",
                  "unseen_cind_satire_1", "unseen_cind_satire_2", "unseen_cind_satire_3", "unseen_cind_satire_4",
                  "unseen_cind_satire_5", "nela_satire_1", "nela_satire_2", "nela_satire_3",
                  "nela_satire_4", "nela_satire_5",
                  "fakenewscorpus_satire_1", "fakenewscorpus_satire_2", "fakenewscorpus_satire_3", "fakenewscorpus_satire_4", "fakenewscorpus_satire_5"
                  }

CLAIMBUSTER_TASKS = {'claimbuster_1', 'claimbuster_2', 'claimbuster_3', 'claimbuster_4', 'claimbuster_5'}

OTHER_DOWNLOAD_TASKS = {
    "abductive_nli",
    "fever_nli",
    "swag",
    "qamr",
    "qasrl",
    "newsqa",
    "mrqa_natural_questions",
    "piqa",
    "winogrande",
}

DIRECT_DOWNLOAD_TASKS = set(
    list(SQUAD_TASKS) + list(DIRECT_SUPERGLUE_TASKS_TO_DATA_URLS) + list(OTHER_DOWNLOAD_TASKS)
)
OTHER_HF_DATASETS_TASKS = {
    "snli",
    "commonsenseqa",
    "hellaswag",
    "cosmosqa",
    "socialiqa",
    "scitail",
    "quoref",
    "adversarial_nli_r1",
    "adversarial_nli_r2",
    "adversarial_nli_r3",
    "arc_easy",
    "arc_challenge",
}
