import data_viz
import gzip
import sys
import time
import argparse

def linear_search(key, L):
    """Searches a list for a key using a linear search
    """
    hit = -1
    for i in range(len(L)):
        curr = L[i]
        if key == curr:
            return i
    return -1
    pass


def binary_serach(key, D):
    """Searches a list for a key using a binary search
    """

    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if (key < D[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1

    pass


def main():

    parser = argparse.ArgumentParser(description='plot gene expression data '
                                     'from gtex files', prog='plot_gtex.py')

    parser.add_argument('--gene', type=str, help='Name of gene', required=True)

    parser.add_argument('--sample_info_file', type=str, help='Name of sample' ,
                        required=True)

    parser.add_argument('--group_type', type=str, help='group info',
                        required=True)

    parser.add_argument('--target_gene', type=str, help='Gene of interest to '
                        , required=True)

    parser.add_argument('--output_file_name', type=str, help='Name for file'
                        'output graph', required=True)

    args = parser.parse_args()

    data_file_name = args.gene_reads_file

    sample_info_file_name = args.sample_info_file



    group_col_name = args.group_data_by
    gene_name = args.target_gene
    sample_id_col_name = 'SAMPID'
    samples = []
    sample_info_header = None

    for l in open(sample_info_file_name):
        if sample_info_header is None:
            sample_info_header = l.rstrip().split('\t')
        else:
            samples.append(l.rstrip().split('\t'))


    group_col_idx = linear_search(group_col_name, sample_info_header)

    sample_id_col_idx = linear_search(sample_id_col_name, sample_info_header)

    groups = []
    members = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[group_col_idx]

        curr_group_idx = linear_search(curr_group, groups)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            members.append([])

        members[curr_group_idx].append(sample_name)

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    group_counts = [[] for i in range(len(groups))]

    for l in gzip.open(data_file_name, 'rt'):  # 'rt' needed for gzip file
        if version is None:
            version = l
            continue

        if dim is None:
            dim = [int(x) for x in l.rstrip().split()]
            continue


        if data_header is None:
            data_header = []
            i = 0
            for field in l.rstrip().split('\t'):
                data_header.append([field, i])
                i += 1
            data_header.sort(key=lambda tup: tup[0])
            continue
        t1_sort = time.time()

        A = l.rstrip().split('\t')


        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in members[group_idx]:
                    member_idx = binary_serach(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))
            break
        t1_search = time.time()

    sort_time = t1_sort - t0_sort
    search_time = t1_search - t0_search



    saved_plot_name = args.output_file_name
    title = str(gene_name)
    x_label = group_col_name
    y_label = "Gene read counts"
    data = group_counts
    foo = groups

    data_viz.boxplot(saved_plot_name, title, x_label, y_label, data, foo)

if __name__ == '__main__':
    main()
