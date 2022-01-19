# sam-envmap

AWS::Serverless::FunctionのEnvironment:で、
JSONでまとめて渡せたら抜け漏れが防げて便利じゃね?
と思って作ったサンプル。

Python 3.8

あまり爽やかにはできなかった。
JSONを組み立てるわけだけど、SAM/CFnでエスケープしてくれないし。


# デプロイ

```sh
sam build
sam deploy --guided  # --guidedは最初の1回
```

`sam deploy --guided` は

```
HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
```

以外はデフォルトでいいです。


# スタックの削除

```sh
sam delete
```
で消えます。
