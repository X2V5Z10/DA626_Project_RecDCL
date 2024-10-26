import argparse
import wandb
from recbole.quick_start import run_recbole
import datetime

if __name__ == '__main__':
    wandb.login(key="b0a8278f5dac242213ceb41254ab62575cf95f34")

    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='BPR', help='name of models')
    parser.add_argument('--dataset', '-d', type=str, default='ml-100k', help='name of datasets')
    parser.add_argument('--config_files', type=str, default=None, help='config files')

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS

    project_name = f"RecDCL_{current_time}"

    args, _ = parser.parse_known_args()
    wandb.init(
        name='exp-' + args.dataset + '-' + args.model,
        project=project_name)
    config_file_list = args.config_files.strip().split(' ') if args.config_files else None
    run_recbole(model=args.model, dataset=args.dataset, config_file_list=config_file_list)
