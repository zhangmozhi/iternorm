# Iterative Normalization for Cross-Lingual Word Embeddings

This repository implements the Iterative Normalization method from our ACL 2019 paper:

Mozhi Zhang, Keyulu Xu, Ken-ichi Kawarabayashi, Stefanie Jegelka, Jordan Boyd-Graber. [_Are Girls Neko or Shōjo? Cross-Lingual Alignment of Non-Isomorphic Embeddings with Iterative Normalization_](https://arxiv.org/abs/1906.01622).

If you want to train cross-lingual word embeddings with a projection-based method (such as [MUSE](https://github.com/facebookresearch/MUSE)), we recommend applying Iterative Normalization on monolingual embeddings before learning the alignment. This preprocessing step consistently improves word translation accuracy, sometimes by a huge margin.

Given an embedding file, you can apply Iterative Normalization with the following command:
```
python iternorm.py [input_embedding_file] [output_path]
```
You can then align the normalized embeddings using libraries such as MUSE.

The code requires Python 2 and `numpy`.

If you find it helpful, please cite:
```
@inproceedings{zhang-2019-iternorm,
    Title = {Are Girls Neko or Sh\={o}jo? Cross-Lingual Alignment of Non-Isomorphic Embeddings with Iterative Normalization},
    Author = {Mozhi Zhang and Keyulu Xu and Ken-ichi Kawarabayashi and Stefanie Jegelka and Jordan Boyd-Graber},
    Booktitle = {Proceedings of the Association for Computational Linguistics},
    doi = "10.18653/v1/P19-1307",
    Year = {2019}
}
```

