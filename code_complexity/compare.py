from csv import QUOTE_ALL
from glob import glob
from pandas import concat
from pandas import read_csv
from subprocess import check_output
from subprocess import CalledProcessError
from subprocess import PIPE
from tempfile import NamedTemporaryFile
from tqdm import tqdm

tqdm.pandas()


def compare(id_code: int, input_code: str, target_code: str, work: int):
    try:
        with NamedTemporaryFile(prefix=f'{id_code}-{work}-') as input_temp, \
                NamedTemporaryFile(prefix=f'{id_code}-{work}-') as target_temp:
            input_temp.write(input_code.encode())
            input_temp.seek(0)
            target_temp.write(target_code.encode())
            target_temp.seek(0)
            jar = './cr-change-diff.jar'
            cmd = ['java', '-jar', jar, input_temp.name, target_temp.name]
            stdout = check_output(cmd, stderr=PIPE).decode()
            return int(stdout.strip())
    except CalledProcessError as cpe:
        stacktrace = cpe.stderr.decode()
        print(f'Instance {id_code} - CalledProcessError:\n{stacktrace}')
        return -1


def compare_row(row):
    return compare(row['id'], row['input'], row['target'], row['work'])


if __name__ == '__main__':
    datasets = glob('input/*.csv')
    df = concat((read_csv(dataset) for dataset in datasets))
    df['changes'] = df.progress_apply(compare_row, axis=1)
    df = df[df['changes'] > -1]
    df.to_csv('ast_diff.csv', index=False, quoting=QUOTE_ALL)
