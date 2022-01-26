import os
import shutil
import re
from tqdm import tqdm


def clear_folder(path):
    if os.path.exists(path):
        all_items_to_remove = [os.path.join(path, f) for f in os.listdir(path)]
        for item_to_remove in all_items_to_remove:
            if os.path.exists(item_to_remove) and not os.path.isdir(item_to_remove):
                os.remove(item_to_remove)
            else:
                shutil.rmtree(item_to_remove)

    if not os.path.exists(path):
        os.makedirs(path)


def copy_file(src_path, dst_path, fname, new_fname=None):
    if new_fname is None:
        new_fname = fname

    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    shutil.copyfile(os.path.join(src_path, fname), os.path.join(dst_path, new_fname))


def search_regex(path, pattern, include_empty_files=True):
    ret_files = list()
    for dirpath, dirnames, filenames in tqdm(os.walk(path), desc='Searching path'):
        if len(filenames) > 0:
            c_files = [os.path.join(dirpath, t) for t in filenames if re.search(pattern, t) is not None]
            if not include_empty_files:
                c_files = [p for p in c_files if os.stat(c_files[0]).st_size > 0]
            if len(c_files) > 0:
                ret_files += c_files
    return ret_files


def build_folders_tree(fname):
    if os.path.exists(fname):
        return True
    else:
        os.makedirs(os.path.dirname(fname))


if __name__ == '__main__':
    rootpath = r'\\10.0.9.220\Eagle\logs\swift_pro\70b.0896.136795'
    trgtpath = r'C:\work\Rosetta\logs_from_cycle'
    srcs = search_regex(rootpath, '.*Rosetta.*', False)
    trgts = [trgtpath + t.split(rootpath)[-1] for t in srcs]

    for idx in range(len(srcs)):
        src_path = os.path.dirname(srcs[idx])
        trgt_path = os.path.dirname(trgts[idx])
        fname = os.path.basename(srcs[idx])
        copy_file(src_path=src_path, dst_path=trgt_path, fname=fname)
