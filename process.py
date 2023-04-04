from pypinyin import lazy_pinyin
from opencc import OpenCC
import pandas as pd
import sys


opencc = OpenCC('s2t.json')


def pinyinify_word(simp_word):
    '''将简体词 simp_word 转换为对应的拼音，不含声调，只输出最常见的一个读音。

    例如，「便宜」只输出 pian yi，不输出 bian yi。'''
    return ' '.join(lazy_pinyin(simp_word))


def tradify_word(simp_word):
    '''将简体字 simp_word 转换成对应的繁体写法。'''
    return opencc.convert(simp_word)


def process_file(file):
    df = pd.DataFrame(columns=['simp_word', 'trad_word', 'freq', 'pinyin'])
    with open(file, 'r') as f:
        for line in f:
            try:
                [simp_word, freq] = line.split()
            except:
                print('Cannot unpack line: ', line)
                continue
            try:
                freq = int(freq.strip())
            except:
                print('Cannot parse freq: ', line)
                continue
            trad_word = tradify_word(simp_word)
            pinyin = pinyinify_word(simp_word)
            df.loc[len(df)] = [simp_word, trad_word, freq, pinyin]
    return df


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    df = process_file(input_file)
    df.to_csv(output_file, index=False)

